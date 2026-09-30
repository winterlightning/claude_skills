#!/usr/bin/env python3
"""Find icons disapproved two or more times on production and report them for run_pipeline.sh.

Read-only: lists /api/work/disapproved, counts disapproval episodes in each icon's
/api/work/history, downloads the current drawing as a --ref file, and writes
report.html, icons.json and batches/batch-NNN.sh (10 icons each). It never claims, uploads or runs the pipeline.

A disapproval episode starts at a disapproval (feedback / review with status pending)
after the icon was last fixed (work_done, upload, or review -> ready / re-generated /
approve); several notes in one review session count once.

The count is work_queue.disapproval_count: episodes as below, distinct disapproved drawings,
and a fix that was disapproved again counts as twice.

Usage: python3 new-pipeline-test/fetch_repeat_disapproved.py [--min 2] [--family solo|all] [--limit N]
       python3 new-pipeline-test/fetch_repeat_disapproved.py --keys LIST.txt [--batch-size 10] [--out DIR]
                                                          # only these icon keys, no history calls
       python3 new-pipeline-test/fetch_repeat_disapproved.py --all   # every current disapproved icon
Output: new-pipeline-test/disapproved/<YYYYMMDD-HHMM>/
"""
import argparse
import hashlib
import html
import json
import os
import re
import shlex
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "icon_set" / "scripts"))
import work_queue  # noqa: E402
from work_queue import ApiError, call, default_base_url  # noqa: E402

PAGE = 500
DISAPPROVE = ("pending", "disapprove")
FIXED_REVIEW = ("ready", "re-generated", "approve")
REASONS = {"bad-stroke": "Bad stroke", "meaning": "Meaning", "manual-fix-request": "Manual fix request", "other": "Other"}


def fetch_disapproved(base, family, limit):
    items, offset = [], 0
    while offset is not None:
        page = call(base, "GET", "/api/work/disapproved",
                    query={"family": family, "limit": PAGE, "offset": offset})
        items += page["items"]
        offset = page.get("next_offset")
        if limit and len(items) >= limit:
            return items[:limit]
    return items


def episodes(history):
    """Group the event log into disapproval episodes, each with its feedback notes."""
    texts = {f["id"]: f for rev in history["revisions"] for f in rev["feedback"]}
    found, fixed_since = [], True
    for event in history["events"]:
        action, d = event["action"], event.get("details") or {}
        status = d.get("status")
        if action in ("work_done", "upload") or (action == "review" and status in FIXED_REVIEW):
            if found:
                found[-1]["fixed"] = found[-1]["fixed"] or event
            fixed_since = True
            continue
        if action not in ("feedback", "review") or status not in DISAPPROVE:
            continue
        if fixed_since:
            found.append({"at": event["at"], "by": event["user"], "notes": [], "fixed": None})
            fixed_since = False
        if action == "feedback":
            text = texts.get(d.get("feedback_id")) or {}
            found[-1]["notes"].append({"at": event["at"], "by": event["user"], "reason": d.get("reason"),
                                       "feedback": text.get("feedback")})
    return found


def latest_only(item):
    """--all: one episode built from the queue item's latest disapproval, no history call."""
    note = {"at": item.get("disapproved_at"), "by": item.get("feedback_by") or item.get("disapproved_by"),
            "reason": item.get("reason"), "feedback": item.get("feedback")}
    return {"episodes": [{"at": item.get("disapproved_at"), "by": item.get("disapproved_by"),
                          "notes": [note] if note["reason"] or note["feedback"] else [], "fixed": None}]}


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-") or "icon"


PUBLISHED = HERE.parent / "published"


def fetch_svg(base, item, path):
    """Copy the local published SVG when it is production's revision; download otherwise. Returns True if local."""
    name, sha = item["key"].split("/")[-1], item.get("svg_sha256")
    for local in sorted(PUBLISHED.glob(f"[!.]*/{name}.svg")):
        data = local.read_bytes()
        if sha and hashlib.sha256(data).hexdigest() == sha:
            path.write_bytes(data)
            return True
    download_svg(base, item["key"], path)
    return False


def download_svg(base, key, path):
    url = base.rstrip("/") + "/api/icon-artwork/svg?icon=" + quote(key, safe="")
    with work_queue.open_url(url, timeout=30) as response:
        path.write_bytes(response.read())


def when(stamp):
    return (stamp or "")[:16].replace("T", " ")


def render(icons, base, minimum, generated):
    esc = html.escape
    cards = []
    for icon in icons:
        preview = icon["ref"] or (base.rstrip("/") + "/api/icon-artwork/svg?icon=" + quote(icon["key"], safe=""))
        timeline = []
        for n, ep in enumerate(icon["episodes"], 1):
            notes = "".join(
                f'<li><span class="tag">{esc(REASONS.get(note["reason"], note["reason"] or "no reason"))}</span> '
                f'<span class="meta">{esc(note["by"] or "?")} · {esc(when(note["at"]))}</span>'
                f'<div class="fb">{esc(note["feedback"] or "(feedback text cleared)")}</div></li>'
                for note in ep["notes"]) or '<li class="meta">Status set to Disapproved without a note</li>'
            fixed = (f'<div class="meta fixed">then fixed: {esc(ep["fixed"]["action"].replace("_", " "))} by '
                     f'{esc(ep["fixed"]["user"] or "?")} · {esc(when(ep["fixed"]["at"]))}</div>') if ep["fixed"] else ""
            timeline.append(f'<li><b>#{n}</b> <span class="meta">{esc(ep["by"] or "?")} · {esc(when(ep["at"]))}</span>'
                            f'<ul>{notes}</ul>{fixed}</li>')
        command = icon["command"]
        cards.append(f'''<article class="card">
  <div class="pic"><img src="{esc(preview)}" alt=""></div>
  <div class="body">
    <h2>{esc(icon["name"] or icon["key"])} {f'<span class="count">×{icon["count"]}</span>' if icon["count"] else ""}</h2>
    <div class="meta"><code>{esc(icon["key"])}</code> · source {esc(icon.get("source_icon_id") or "MISSING")} · {esc(icon["family"] or "")} · {esc(icon["category"] or "")} ·
      work: {esc(icon["work_state"] or "open")}</div>
    <ol class="timeline">{"".join(timeline)}</ol>
    {f'<div class="cmd"><code>{esc(command)}</code><button type="button" data-cmd="{esc(command)}">Copy</button></div>' if command else ""}
  </div>
</article>''')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Repeat Disapprovals</title>
<style>
:root {{ --bg:#f6f6f4; --card:#fff; --ink:#1b1b1b; --muted:#6b6b6b; --line:#e2e2de; --accent:#b3261e; --code:#f0f0ec; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg:#161616; --card:#212121; --ink:#ececec; --muted:#9a9a9a; --line:#333; --accent:#ff8a80; --code:#2a2a2a; }} }}
:root[data-theme="dark"] {{ --bg:#161616; --card:#212121; --ink:#ececec; --muted:#9a9a9a; --line:#333; --accent:#ff8a80; --code:#2a2a2a; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; padding:24px 16px; background:var(--bg); color:var(--ink); font:14px/1.45 -apple-system, system-ui, sans-serif; }}
main {{ max-width:1000px; margin:0 auto; }}
h1 {{ font-size:20px; margin:0 0 4px; }}
.meta {{ color:var(--muted); font-size:12px; }}
.card {{ display:flex; gap:16px; background:var(--card); border:1px solid var(--line); border-radius:10px; padding:16px; margin:12px 0; }}
.pic {{ flex:0 0 96px; }}
.pic img {{ width:96px; height:96px; background:#fff; border:1px solid var(--line); border-radius:6px; }}
.body {{ flex:1; min-width:0; }}
h2 {{ font-size:16px; margin:0 0 2px; }}
.count {{ color:var(--accent); }}
.timeline {{ padding-left:18px; margin:8px 0; }}
.timeline > li {{ margin:6px 0; }}
.timeline ul {{ padding-left:16px; margin:4px 0; }}
.tag {{ display:inline-block; font-size:11px; padding:0 6px; border-radius:4px; background:var(--code); }}
.fb {{ white-space:pre-wrap; margin:2px 0 4px; }}
.fixed {{ font-style:italic; }}
.cmd {{ display:flex; gap:8px; align-items:flex-start; margin-top:8px; }}
code {{ background:var(--code); padding:2px 5px; border-radius:4px; font-size:12px; overflow-wrap:anywhere; }}
.cmd code {{ flex:1; padding:6px 8px; }}
button {{ font:inherit; font-size:12px; padding:5px 10px; border:1px solid var(--line); border-radius:6px; background:var(--card); color:var(--ink); cursor:pointer; }}
@media (max-width:560px) {{ .card {{ flex-direction:column; }} }}
</style></head><body><main>
<h1>{"Current disapproved icons" if minimum is None else f"Icons disapproved {minimum}+ times"}</h1>
<div class="meta">{len(icons)} icons · {esc(base)} · generated {esc(generated)}. Nothing has been run; copy a command or run a script in batches/.</div>
{"".join(cards) or "<p>No icons match.</p>"}
</main>
<script>
document.addEventListener('click', e => {{
  const b = e.target.closest('button[data-cmd]'); if (!b) return;
  navigator.clipboard.writeText(b.dataset.cmd).then(() => {{ const label = b.textContent; b.textContent = 'Copied'; setTimeout(() => b.textContent = label, 1200); }});
}});
</script></body></html>
'''


UUID_RE = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", re.I)
ROOT = HERE.parent


def load_catalog():
    path = ROOT / "published" / "gallery" / "icons.json"
    data = json.loads(path.read_text())
    items = data if isinstance(data, list) else data.get("icons", data)
    return {item["key"]: item for item in (items.values() if isinstance(items, dict) else items)}


def attach_sources(icons):
    """Set source_icon_id (the model's SOURCE_ICON_ID, else the UUID in the original source's
    file name), original_ref (the original reference if on disk) and the run_pipeline item."""
    catalog = load_catalog()
    for icon in icons:
        record = catalog.get(icon["key"]) or {}
        uuid = None
        module = ROOT / ((record.get("python_source") or {}).get("path") or "")
        if module.is_file():
            m = re.search(r"^SOURCE_ICON_ID\s*=\s*['\"]([^'\"]+)['\"]", module.read_text(), re.M)
            uuid = m.group(1) if m and UUID_RE.fullmatch(m.group(1)) else None
        original = None
        for source in record.get("original_sources") or []:
            for candidate in (ROOT / (source.get("source_path") or ""), ROOT / "published" / "gallery" / (source.get("url") or "")):
                if candidate.is_file() and candidate.suffix.lower() in (".svg", ".png") and original is None:
                    original = candidate
            if uuid is None:
                m = UUID_RE.search(source.get("source_path") or "")
                uuid = m.group(0) if m else None
        icon["source_icon_id"] = uuid.lower() if uuid else None
        icon["original_ref"] = str(original.relative_to(ROOT)) if original else None
        ref = icon["original_ref"] or icon.get("ref_abs")
        icon["pipeline_item"] = (f'{shlex.quote(icon["name"] or icon["key"])} {icon["source_icon_id"]}'
                                 + (f" {shlex.quote(ref)}" if ref else "")) if uuid else ""
        icon["command"] = ("new-pipeline-test/run_pipeline.sh " + icon["pipeline_item"]) if uuid else ""
    return icons


def icons_command(icons, with_ref=True):
    """run_pipeline.sh with NAME SOURCE_ID [REFERENCE] items; with_ref=False drops the references."""
    parts = [i["pipeline_item"] if with_ref else f'{shlex.quote(i["name"] or i["key"])} {i["source_icon_id"]}'
             for i in icons if i.get("pipeline_item")]
    return "new-pipeline-test/run_pipeline.sh \\\n  " + " \\\n  ".join(parts) if parts else ""


def write_batches(out, icons, size):
    """batches/batch-NNN.sh: one run_pipeline.sh command per `size` icons. Written, never run."""
    folder = out / "batches"
    folder.mkdir(exist_ok=True)
    for old in folder.glob("batch-*.sh"):
        old.unlink()
    # Another worker holds these right now; redrawing them would collide with that fix.
    held = [i for i in icons if i.get("work_state") == "working"]
    (folder / "claimed-skipped.txt").write_text(
        "# Left out: claimed by another worker when fetched.\n"
        + "".join(f"{i['key']}\t{i.get('worker') or ''}\n" for i in held))
    icons = [i for i in icons if i.get("work_state") != "working"]
    missing = [i for i in icons if not i.get("pipeline_item")]
    (folder / "needs-source-id.txt").write_text(
        "# No SOURCE_ICON_ID found (model or original source); left out of the batches.\n"
        "# Add them by hand as: NAME SOURCE_ID [REFERENCE]\n"
        + "".join(f"{i['key']}\t{i['name'] or ''}\t{i.get('ref_abs') or ''}\n" for i in missing))
    icons = [i for i in icons if i.get("pipeline_item")]
    # Two catalog icons can share one original (bridge-pose / bridge-pose-solo); draw it once.
    seen, unique, same_source = set(), [], []
    for i in icons:
        (same_source if i["source_icon_id"] in seen else unique).append(i)
        seen.add(i["source_icon_id"])
    (folder / "same-source-skipped.txt").write_text(
        "# Left out: another icon in the batches already has this source id.\n"
        + "".join(f"{i['key']}\t{i['source_icon_id']}\n" for i in same_source))
    icons = unique
    chunks = [icons[i:i + size] for i in range(0, len(icons), size)]
    for n, chunk in enumerate(chunks, 1):
        keys = "".join(f"#   {i['key']}  source {i['source_icon_id']}"
                       + ("" if i["original_ref"] else "  (reference: current drawing, original not on disk)") + "\n" for i in chunk)
        path = folder / f"batch-{n:03d}.sh"
        path.write_text(f"#!/bin/bash\n# Batch {n}/{len(chunks)}: {len(chunk)} icons as NAME SOURCE_ID [REFERENCE]; generated by fetch_repeat_disapproved.py.\n"
                        f"{keys}cd {shlex.quote(str(HERE.parent))}\n{icons_command(chunk) or '# no reference files'}\n")
        path.chmod(0o755)
    (out / "batches.html").write_text(render_batches(out, chunks, missing, same_source, held))
    return len(chunks)


def render_batches(out, chunks, missing, same_source=(), held=()):
    """batches.html: one card per batch of 10 with its thumbnails and a copy button for the command."""
    esc = html.escape
    rel = lambda p: os.path.relpath(ROOT / p if not os.path.isabs(p) else p, out)  # noqa: E731
    cards = []
    for n, chunk in enumerate(chunks, 1):
        cd = f"cd {shlex.quote(str(ROOT))} && "
        with_ref, no_ref = cd + icons_command(chunk), cd + icons_command(chunk, with_ref=False)
        thumbs = []
        for i in chunk:
            pics = "".join(f'<img src="{esc(rel(p))}" alt="" loading="lazy" title="{t}">'
                           for p, t in ((i["original_ref"], "original reference"), (i.get("ref_abs"), "current (disapproved)")) if p)
            thumbs.append(f'<li><div class="pics">{pics}</div><div class="nm">{esc(i["name"] or i["key"])}</div>'
                          f'<div class="id">{esc(i["source_icon_id"])}</div></li>')
        cards.append(f'''<section class="batch" id="b{n}" data-n="{n}">
  <header><label><input type="checkbox" class="done"> <b>Batch {n:03d}</b></label>
    <span class="meta">{len(chunk)} icons</span>
    <span class="copies"><button type="button" class="copy" data-kind="ref" data-cmd="{esc(with_ref)}">Copy with reference</button>
    <button type="button" class="copy alt" data-kind="noref" data-cmd="{esc(no_ref)}">Copy without reference</button></span></header>
  <ul class="icons">{"".join(thumbs)}</ul>
  <details><summary>Show commands</summary><div class="meta">With reference</div><pre>{esc(with_ref)}</pre>
    <div class="meta">Without reference</div><pre>{esc(no_ref)}</pre></details>
</section>''')
    skipped = "".join(f"<li><code>{esc(i['key'])}</code> {esc(i['name'] or '')}</li>" for i in missing)
    total = sum(len(c) for c in chunks)
    dup_list = "".join(f"<li><code>{esc(i['key'])}</code> {esc(i['source_icon_id'])}</li>" for i in same_source)
    held_list = "".join(f"<li><code>{esc(i['key'])}</code> {esc(i.get('worker') or '')}</li>" for i in held)
    folder = shlex.quote(os.path.relpath(out, ROOT))
    upload = (f"cd {shlex.quote(str(ROOT))} && /opt/homebrew/bin/python3 new-pipeline-test/claim_liked.py "
              f"--finished {folder} --worker thuan-mac")
    upload_card = f'''<section class="batch upload">
  <header><b>Upload + done</b><span class="meta">after a batch finishes (safe to rerun: finished icons are skipped)</span>
    <span class="copies"><button type="button" class="copy" data-cmd="{esc(upload)} --dry-run">Copy dry run</button>
    <button type="button" class="copy alt" data-cmd="{esc(upload)}">Copy upload + done</button></span></header>
  <p class="meta">Claims each icon of this list that has a finished <code>_redraw.svg</code> in output_png, uploads the production
  drawing as before and the redraw (+ module, validation) as after, then reports done: the revision goes back to Ready.
  Change <code>--worker</code> to your name.</p>
  <details><summary>Show command</summary><pre>{esc(upload)}</pre></details>
</section>'''
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pipeline Batches</title>
<style>
:root {{ --bg:#f6f6f4; --card:#fff; --ink:#1b1b1b; --muted:#6b6b6b; --line:#e2e2de; --accent:#1f6feb; --ok:#1a7f37; --code:#f0f0ec; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg:#161616; --card:#212121; --ink:#ececec; --muted:#9a9a9a; --line:#333; --accent:#58a6ff; --ok:#3fb950; --code:#2a2a2a; }} }}
:root[data-theme="dark"] {{ --bg:#161616; --card:#212121; --ink:#ececec; --muted:#9a9a9a; --line:#333; --accent:#58a6ff; --ok:#3fb950; --code:#2a2a2a; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; padding:24px 16px 64px; background:var(--bg); color:var(--ink); font:14px/1.45 -apple-system, system-ui, sans-serif; }}
main {{ max-width:1100px; margin:0 auto; }}
h1 {{ font-size:20px; margin:0 0 4px; }}
.meta {{ color:var(--muted); font-size:12px; }}
.bar {{ position:sticky; top:0; z-index:2; background:var(--bg); padding:10px 0; display:flex; gap:12px; align-items:center; flex-wrap:wrap; border-bottom:1px solid var(--line); margin-bottom:8px; }}
.progress {{ flex:1; min-width:160px; height:8px; background:var(--line); border-radius:4px; overflow:hidden; }}
.progress i {{ display:block; height:100%; width:0; background:var(--ok); }}
.batch {{ background:var(--card); border:1px solid var(--line); border-radius:10px; padding:12px 14px; margin:12px 0; }}
.batch.is-done {{ opacity:.55; }}
.batch.is-done header b {{ color:var(--ok); }}
.batch.is-next {{ border-color:var(--accent); box-shadow:0 0 0 1px var(--accent); }}
header {{ display:flex; gap:10px; align-items:center; flex-wrap:wrap; }}
header label {{ display:flex; gap:6px; align-items:center; cursor:pointer; font-size:15px; }}
.copies {{ margin-left:auto; display:flex; gap:6px; flex-wrap:wrap; }}
button {{ font:inherit; font-size:13px; padding:6px 12px; border:1px solid var(--line); border-radius:6px; background:var(--card); color:var(--ink); cursor:pointer; }}
.copy {{ background:var(--accent); border-color:var(--accent); color:#fff; font-weight:600; }}
.copy.alt {{ background:var(--card); color:var(--accent); }}
.copy.copied {{ background:var(--ok); border-color:var(--ok); }}
.icons {{ list-style:none; padding:0; margin:10px 0 4px; display:grid; grid-template-columns:repeat(auto-fill, minmax(96px, 1fr)); gap:10px; }}
.icons li {{ min-width:0; }}
.pics {{ display:flex; gap:3px; }}
.pics img {{ width:46px; height:46px; background:#fff; border:1px solid var(--line); border-radius:5px; padding:3px; }}
.nm {{ font-size:12px; margin-top:3px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }}
.id {{ font:10px ui-monospace, monospace; color:var(--muted); overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }}
details summary {{ cursor:pointer; color:var(--muted); font-size:12px; }}
pre {{ background:var(--code); padding:8px 10px; border-radius:6px; font-size:11px; overflow-x:auto; margin:6px 0 0; }}
code {{ background:var(--code); padding:1px 4px; border-radius:3px; font-size:12px; }}
</style></head><body><main>
<h1>Pipeline batches</h1>
<div class="meta">{total} icons in {len(chunks)} batches of up to 10 · each command runs <code>run_pipeline.sh</code> with NAME SOURCE_ID REFERENCE items.
Run one batch at a time. Thumbnails: original reference, then the current disapproved drawing.</div>
<div class="bar"><button type="button" class="next copy" data-kind="ref">Copy next · with reference</button>
  <button type="button" class="next copy alt" data-kind="noref">Copy next · without reference</button>
  <span id="count" class="meta"></span><div class="progress"><i id="fill"></i></div>
  <label class="meta"><input type="checkbox" id="hide"> hide done</label>
  <button type="button" id="reset">Reset ticks</button></div>
{"".join(cards)}
{upload_card}
{f'<details><summary>{len(held)} icons left out: claimed by another worker</summary><ul>{held_list}</ul></details>' if held else ""}
{f'<details><summary>{len(missing)} icons left out: no source id</summary><ul>{skipped}</ul></details>' if missing else ""}
{f'<details><summary>{len(same_source)} icons left out: same source id as an icon already in a batch</summary><ul>{dup_list}</ul></details>' if same_source else ""}
</main>
<script>
const KEY = 'pipeline-batches:' + location.pathname;
let done = new Set();
try {{ done = new Set(JSON.parse(localStorage.getItem(KEY) || '[]')); }} catch (e) {{}}
const save = () => {{ try {{ localStorage.setItem(KEY, JSON.stringify([...done])); }} catch (e) {{}} }};
const cards = [...document.querySelectorAll('.batch:not(.upload)')];
function paint() {{
  const hide = document.getElementById('hide').checked;
  let next = null;
  for (const c of cards) {{
    const isDone = done.has(c.dataset.n);
    c.querySelector('.done').checked = isDone;
    c.classList.toggle('is-done', isDone);
    c.hidden = hide && isDone;
    if (!isDone && !next) next = c;
    c.classList.toggle('is-next', c === next);
  }}
  document.getElementById('count').textContent = done.size + ' / ' + cards.length + ' done';
  document.getElementById('fill').style.width = (100 * done.size / cards.length) + '%';
  return next;
}}
function copy(button) {{
  const text = button.dataset.cmd;
  const ok = () => {{ const label = button.textContent; button.textContent = 'Copied'; button.classList.add('copied');
    setTimeout(() => {{ button.textContent = label; button.classList.remove('copied'); }}, 1400); }};
  if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).then(ok, () => fallback(text, ok));
  else fallback(text, ok);
}}
function fallback(text, ok) {{
  const t = document.createElement('textarea'); t.value = text; t.style.position = 'fixed'; t.style.opacity = '0';
  document.body.append(t); t.select(); try {{ document.execCommand('copy'); ok(); }} catch (e) {{}} t.remove();
}}
document.addEventListener('click', e => {{
  const b = e.target.closest('button.copy');
  if (b && !b.classList.contains('next')) {{ copy(b); const n = b.closest('.batch').dataset.n; if (n) {{ done.add(n); save(); paint(); }} }}
}});
document.addEventListener('change', e => {{
  if (e.target.classList.contains('done')) {{ const n = e.target.closest('.batch').dataset.n;
    e.target.checked ? done.add(n) : done.delete(n); save(); paint(); }}
  if (e.target.id === 'hide') paint();
}});
document.querySelectorAll('button.next').forEach(button => button.addEventListener('click', e => {{
  const next = paint(); if (!next) return;
  next.scrollIntoView({{block: 'center', behavior: 'smooth'}});
  const b = next.querySelector('button.copy[data-kind="' + button.dataset.kind + '"]'); button.dataset.cmd = b.dataset.cmd; copy(button);
  done.add(next.dataset.n); save(); paint();
}}));
document.getElementById('reset').addEventListener('click', () => {{ done.clear(); save(); paint(); }});
paint();
</script></body></html>
'''


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--min", type=int, default=2, help="minimum disapproval episodes (default 2)")
    parser.add_argument("--family", default="solo", help="icon family, or 'all' (default solo)")
    parser.add_argument("--limit", type=int, default=0, help="only inspect the first N disapproved icons")
    parser.add_argument("--base-url", default=None, help="production gallery (default: $PICTOGRAPHIC_API or the tunnel)")
    parser.add_argument("--all", action="store_true",
                        help="every current disapproved icon; skips the per-icon history calls (fast)")
    parser.add_argument("--batch-size", type=int, default=10, help="icons per batches/batch-NNN.sh (default 10)")
    parser.add_argument("--rebuild", metavar="DIR", help="rewrite report + batches of an earlier fetch from its icons.json (offline)")
    parser.add_argument("--keys", metavar="FILE",
                        help="only these icon keys (one per line, # comments); no history calls")
    parser.add_argument("--workers", type=int, default=2, help="parallel history requests (default 2)")
    parser.add_argument("--no-download", action="store_true", help="do not save reference SVGs")
    parser.add_argument("--out", default=None, help="output folder (default new-pipeline-test/disapproved/<stamp>)")
    args = parser.parse_args(argv)

    if args.rebuild:
        out = Path(args.rebuild)
        data = json.loads((out / "icons.json").read_text())
        for icon in data["icons"]:
            if icon.get("ref"):
                icon["ref_abs"] = str((out / icon["ref"]).resolve())
        attach_sources(data["icons"])
        (out / "icons.json").write_text(json.dumps(data, indent=2))
        (out / "commands.sh").unlink(missing_ok=True)
        batches = write_batches(out, data["icons"], args.batch_size)
        (out / "report.html").write_text(render(data["icons"], data["base_url"], data.get("min") if data["icons"] and data["icons"][0].get("count") else None, data["generated"]))
        missing = sum(1 for i in data["icons"] if not i.get("pipeline_item"))
        print(f"{len(data['icons'])} icons: {batches} batch scripts, {missing} without a source id (batches/needs-source-id.txt)")
        return

    base = args.base_url or default_base_url()
    family = None if args.family == "all" else args.family
    try:
        items = fetch_disapproved(base, family, args.limit)
    except ApiError as error:
        raise SystemExit(f"error: {error}")
    wanted = None
    if args.keys:
        wanted = [line.split()[0] for line in Path(args.keys).read_text().splitlines()
                  if line.strip() and not line.lstrip().startswith("#")]
        live = {item["key"] for item in items}
        gone = [key for key in wanted if key not in live]
        if gone:
            print(f"{len(gone)} listed keys are no longer disapproved: " + ", ".join(gone[:10])
                  + (" …" if len(gone) > 10 else ""), file=sys.stderr)
        keep = set(wanted)
        items = [item for item in items if item["key"] in keep]
    print(f"{len(items)} disapproved icons on {base}" + ("" if args.all or wanted else "; reading histories…"), file=sys.stderr)

    def history(item):
        if args.all or wanted:
            return item, latest_only(item)
        try:
            return item, call(base, "GET", "/api/work/history", query={"icon": item["key"]})
        except ApiError as error:
            print(f"  skip {item['key']}: {error}", file=sys.stderr)
            return item, None

    with ThreadPoolExecutor(max_workers=1 if args.all or wanted else max(1, args.workers)) as pool:
        results = list(pool.map(history, items))

    stamp = datetime.now().strftime("%Y%m%d-%H%M")
    out = Path(args.out) if args.out else HERE / "disapproved" / stamp
    refs = out / "refs"
    refs.mkdir(parents=True, exist_ok=True)

    icons, used, local = [], set(), 0
    for item, hist in results:
        if hist is None:
            continue
        eps = episodes(hist) if "events" in hist else hist["episodes"]
        count = work_queue.disapproval_count(hist) if "events" in hist else None
        if count is not None and count < args.min:
            continue
        slug = slugify(item.get("name") or item["key"].split("/")[-1])
        while slug in used:
            slug += "-2"
        used.add(slug)
        ref = ref_abs = None
        if not args.no_download:
            path = refs / f"{slug}.svg"
            try:
                local += fetch_svg(base, item, path)
                ref, ref_abs = f"refs/{slug}.svg", str(path.resolve())
            except OSError as error:
                print(f"  no svg for {item['key']}: {error}", file=sys.stderr)
        icons.append({
            "key": item["key"], "name": item.get("name"), "family": item.get("family"),
            "category": item.get("category"), "svg_sha256": item.get("svg_sha256"),
            "work_state": (item.get("work") or {}).get("state"), "worker": (item.get("work") or {}).get("worker"),
            "count": count,
            "episodes": eps, "ref": ref, "ref_abs": ref_abs,
        })
    icons.sort(key=lambda i: (-(i["count"] or 0), i["key"]))
    attach_sources(icons)

    generated = datetime.now().isoformat(timespec="seconds")
    (out / "icons.json").write_text(json.dumps({"base_url": base, "generated": generated, "min": args.min,
                                                "inspected": len(items), "icons": icons}, indent=2))
    batches = write_batches(out, icons, args.batch_size)
    (out / "report.html").write_text(render(icons, base, None if args.all or wanted else args.min, generated))
    print(f"{len(icons)} current disapproved icons" if args.all or wanted
          else f"{len(icons)} of {len(items)} disapproved icons were disapproved >= {args.min} times")
    print(f"reference svgs: {local} copied from published/, {sum(1 for i in icons if i['ref']) - local} downloaded")
    print(f"scripts: {batches} x batches/batch-NNN.sh ({args.batch_size} icons each); "
          f"{sum(1 for i in icons if not i.get('pipeline_item'))} without a source id in batches/needs-source-id.txt")
    print(f"report: {out / 'report.html'}")


if __name__ == "__main__":
    main()
