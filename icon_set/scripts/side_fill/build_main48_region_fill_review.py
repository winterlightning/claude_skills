"""Build isolated 48px side-main fill drafts while preserving saved variants."""

from __future__ import annotations

from .paths import DATA, FILL_ENGINE, WORK  # noqa: F401
import argparse
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
import html
import io
import json
from pathlib import Path
import shutil

import cairosvg
from PIL import Image, ImageChops

from .build_sub32_region_fill_review import draft_one, sha


ROOT = WORK
SOURCE = DATA / "data/latest-side-main-48"
PRESERVED = DATA / "data/preserved-main-fill-48-20261026"
DECISIONS = DATA / "data/main48-region-fill-review-decisions.json"
MARKS = DATA / "data/main48-user-review-marks.json"
OUTPUT = WORK / "main48-region-fill-review"


def visual_duplicates(record: dict, current: dict | None,
                      alternates: list[dict], cache: dict) -> tuple[dict | None, list[dict]]:
    """Hide only variants indistinguishable at the native 48px display size."""
    def rendered(path: Path):
        key = str(path)
        if key not in cache:
            image = Image.open(io.BytesIO(cairosvg.svg2png(
                url=key, output_width=48, output_height=48))).convert("RGBA")
            cache[key] = image
        return cache[key]

    def same(a, b):
        difference = ImageChops.difference(a, b)
        histogram = difference.histogram()
        total = sum((index % 256) * count for index, count in enumerate(histogram))
        if total > 2000:
            return False
        return sum(max(pixel) > 16 for pixel in difference.getdata()) <= 12

    name = record["name"]
    representative = [("script", rendered(OUTPUT / "proposals/svg" / f"{name}.svg"))]
    current = dict(current) if current else None
    if current:
        image = rendered(PRESERVED / current["path"])
        current["duplicate_of"] = next((label for label, earlier in representative
                                         if same(image, earlier)), None)
        if not current["duplicate_of"]:
            representative.append(("current", image))
    result = []
    for item in alternates:
        item = dict(item)
        image = rendered(PRESERVED / item["path"])
        item["duplicate_of"] = next((label for label, earlier in representative
                                     if same(image, earlier)), None)
        if not item["duplicate_of"]:
            representative.append((f'approved:{item["variant"]}', image))
        result.append(item)
    return current, result


def saved_variants() -> tuple[dict, dict]:
    manifest = json.loads((PRESERVED / "manifest.json").read_text())
    current = {item["name"]: item for item in manifest["current_fills"]}
    alternates = defaultdict(list)
    for item in manifest["approved_alternates"]:
        alternates[item["name"]].append(item)
    return current, alternates


def selected_bytes(name: str, source_hash: str, proposal: bytes,
                   current: dict | None, alternates: list[dict], mark: dict | None) -> tuple[bytes, str, str | None]:
    if not mark or mark.get("source_sha256") != source_hash:
        return proposal, "script", None
    action = mark.get("action")
    if action == "retain":
        return (SOURCE / f"{name}.svg").read_bytes(), "original", None
    if action == "keep_current" and current:
        path = PRESERVED / current["path"]
        data = path.read_bytes()
        if sha(data) != current["sha256"]:
            raise ValueError(f"Preserved current fill changed: {name}")
        return data, "current_fill", None
    if action == "keep_variant":
        variant = mark.get("variant")
        item = next((item for item in alternates if item["variant"] == variant
                     and item["inventory_source_sha256"] == source_hash), None)
        if item:
            data = (PRESERVED / item["path"]).read_bytes()
            if sha(data) != item["sha256"]:
                raise ValueError(f"Preserved approved variant changed: {name} {variant}")
            return data, "approved_variant", variant
    if "script" in mark.get("removed_variants", []):
        return (SOURCE / f"{name}.svg").read_bytes(), "original", None
    return proposal, "script", None


def select_one(record: dict, mark: dict | None, current: dict | None,
               alternates: list[dict], output: Path = OUTPUT,
               script_variants: list[dict] | None = None) -> dict:
    name = record["name"]
    proposal_path = output / "proposals/svg" / f"{name}.svg"
    source_hash = record["source_sha256_at_run"]
    proposal = proposal_path.read_bytes()
    data, selection, variant = selected_bytes(name, source_hash, proposal, current, alternates, mark)
    target = output / "svg" / f"{name}.svg"
    target.write_bytes(data)
    record = dict(record)
    record["proposal_status"] = record["status"]
    record["proposal_output"] = f"proposals/svg/{name}.svg"
    record["proposal_sha256"] = sha(proposal)
    record["output"] = f"svg/{name}.svg"
    record["output_sha256"] = sha(data)
    record["selected_kind"] = selection
    record["selected_variant"] = variant
    active_mark = mark if mark and mark.get("source_sha256") == source_hash else {}
    removed_ids = list(dict.fromkeys(active_mark.get("removed_variants", [])))
    selected_ids = [item for item in dict.fromkeys(active_mark.get("selected_variants", []))
                    if item not in removed_ids]
    variants = {"script": proposal}
    script_variants = [item for item in (script_variants or []) if item["source_sha256"] == source_hash]
    for item in script_variants:
        variants[f'script:{item["variant"]}'] = (output / item["path"]).read_bytes()
    if current:
        saved = (PRESERVED / current["path"]).read_bytes()
        if sha(saved) != current["sha256"]:
            raise ValueError(f"Preserved current fill changed: {name}")
        variants["current"] = saved
    for item in alternates:
        if item["inventory_source_sha256"] == source_hash:
            saved = (PRESERVED / item["path"]).read_bytes()
            if sha(saved) != item["sha256"]:
                raise ValueError(f"Preserved approved variant changed: {name} {item['variant']}")
            variants[f'approved:{item["variant"]}'] = saved
    selected_dir = output / "selected-variants" / name
    if selected_dir.exists():
        shutil.rmtree(selected_dir)
    selected_outputs = []
    for identifier in selected_ids:
        if identifier not in variants:
            continue
        selected_dir.mkdir(parents=True, exist_ok=True)
        filename = identifier.replace(":", "--") + ".svg"
        selected_path = selected_dir / filename
        selected_path.write_bytes(variants[identifier])
        selected_outputs.append({"variant": identifier,
                                 "path": str(selected_path.relative_to(output)),
                                 "sha256": sha(variants[identifier])})
    record["selected_variants"] = [item["variant"] for item in selected_outputs]
    record["selected_variant_outputs"] = selected_outputs
    record["removed_variants"] = removed_ids
    if selection == "original":
        record["status"] = "retained_original"
    elif selection == "current_fill":
        record["status"] = "kept_existing_fill"
    elif selection == "approved_variant":
        record["status"] = "kept_approved_variant"
    record["current_fill"] = current
    record["approved_alternates"] = alternates
    record["script_variants"] = script_variants
    return record


def gallery(records: list[dict]) -> str:
    cards = []
    for row in records:
        name = row["name"]
        title = html.escape(name)
        source_hash = row.get("source_sha256_at_run", "")
        selected_url = f'svg/{name}.svg?v={row["output_sha256"][:12]}' if row.get("output_sha256") else ""
        proposal_url = f'proposals/svg/{name}.svg?v={row["proposal_sha256"][:12]}' if row.get("proposal_sha256") else ""
        current = row.get("current_fill")
        alternates = row.get("approved_alternates", [])
        removed = set(row.get("removed_variants", []))
        script_removed = ' removed' if 'script' in removed else ''
        current_card = ""
        if current:
            url = f'../../data/preserved-main-fill-48-20261026/{current["path"]}?v={current["sha256"][:12]}'
            duplicate = ' duplicate' if current.get('duplicate_of') else ''
            removed_class = ' removed' if 'current' in removed else ''
            current_card = (
                f'<figure class="saved-fill{duplicate}{removed_class}" data-variant-id="current"><img loading="lazy" src="' + html.escape(url, quote=True) + '" alt="Saved current Fill">'
                '<figcaption>Saved current Fill</figcaption><button type="button" data-action="toggle_variant" data-variant-id="current">Keep variant</button>'
                '<button type="button" data-action="toggle_remove_variant" data-variant-id="current">Remove</button></figure>'
            )
        alternate_cards = []
        for item in alternates:
            url = f'../../data/preserved-main-fill-48-20261026/{item["path"]}?v={item["sha256"][:12]}'
            variant = html.escape(item["variant"])
            duplicate = ' duplicate' if item.get('duplicate_of') else ''
            identifier = f'approved:{variant}'
            removed_class = ' removed' if f'approved:{item["variant"]}' in removed else ''
            alternate_cards.append(
                f'<figure class="saved-fill{duplicate}{removed_class}" data-variant-id="{identifier}"><img loading="lazy" src="{html.escape(url, quote=True)}" alt="Approved {variant}">'
                f'<figcaption>Approved {variant}</figcaption><button type="button" data-action="toggle_variant" data-variant-id="{identifier}">Keep variant</button>'
                f'<button type="button" data-action="toggle_remove_variant" data-variant-id="{identifier}">Remove</button></figure>'
            )
        script_cards = []
        for item in row.get("script_variants", []):
            url = f'{item["path"]}?v={item["sha256"][:12]}'
            variant = html.escape(item["variant"])
            identifier = f'script:{variant}'
            removed_class = ' removed' if f'script:{item["variant"]}' in removed else ''
            script_cards.append(
                f'<figure class="saved-fill{removed_class}" data-variant-id="{identifier}"><img loading="lazy" src="{html.escape(url, quote=True)}" alt="Script variant {variant}">'
                f'<figcaption title="{html.escape(item["reason"], quote=True)}">Script variant {variant}</figcaption><button type="button" data-action="toggle_variant" data-variant-id="{identifier}">Keep variant</button>'
                f'<button type="button" data-action="toggle_remove_variant" data-variant-id="{identifier}">Remove</button></figure>'
            )
        saved = "".join(script_cards) + current_card + "".join(alternate_cards)
        saved_section = (f'<div class="saved-grid">{saved}</div>') if saved else '<p class="no-saved">No saved Fill</p>'
        retained_hidden = '' if row.get('selected_kind') == 'original' else ' hidden'
        duplicate_count = int(bool(current and current.get('duplicate_of'))) + sum(
            bool(item.get('duplicate_of')) for item in alternates)
        duplicate_note = (f'<p class="duplicate-note">{duplicate_count} matching saved variant(s) hidden; files preserved.</p>'
                          if duplicate_count else '')
        note = (f'<p class="note">{html.escape(row["review_note"])}</p>' if row.get("review_note") else "")
        cards.append(
            f'<article data-name="{title}" data-status="{html.escape(row["status"])}" data-source-hash="{source_hash}">'
            f'<h2>{title}</h2><div class="selected{script_removed}" data-variant-id="script"><img loading="lazy" src="{html.escape(proposal_url, quote=True)}" alt="Script draft {title}">'
            '<span>Script draft</span><button type="button" data-action="toggle_variant" data-variant-id="script">Keep variant</button>'
            '<button type="button" data-action="toggle_remove_variant" data-variant-id="script">Remove</button></div>'
            f'<div class="retained-output"{retained_hidden}><img data-output-image loading="lazy" src="{html.escape(selected_url, quote=True)}" alt="Original output {title}"><span>Original output</span></div>'
            f'<p class="badge">{html.escape(row["status"].replace("_", " "))} · {len(row.get("selected_variants", []))} variant(s) selected · {len(removed)} removed</p>'
            f'<div class="preview-links"><a href="../../data/latest-side-main-48/{title}.svg" target="_blank">View original</a></div>'
            f'{saved_section}{duplicate_note}{note}'
            '<div class="mark-controls"><button type="button" data-action="retain">Retain original</button>'
            '<button type="button" data-action="fix_small_dot">Fix small dot</button>'
            '<button type="button" data-action="clear">Clear choice</button><span class="mark-state">Unmarked</span></div>'
            '<div class="feedback-controls"><label>Feedback<textarea rows="2" maxlength="2000" placeholder="What should change?"></textarea></label>'
            '<button type="button" data-action="save_feedback">Save feedback</button></div>'
            + (f'<p class="error">{html.escape(row["error"])}</p>' if row.get("error") else "")
            + '</article>'
        )
    counts = Counter(row["status"] for row in records)
    summary = " · ".join(f"{key.replace('_', ' ')} {value}" for key, value in sorted(counts.items()))
    total_duplicates = sum(int(bool(row.get("current_fill") and row["current_fill"].get("duplicate_of")))
                           + sum(bool(item.get("duplicate_of")) for item in row.get("approved_alternates", []))
                           for row in records)
    return f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Side main 48 · Fill outputs</title>
<style>
*{{box-sizing:border-box}}body{{margin:0;background:#edf1f3;color:#18252e;font:14px system-ui}}
header{{position:sticky;top:0;z-index:2;background:#fff;padding:16px 22px;box-shadow:0 2px 12px #0002}}
h1{{font-size:22px;margin:0 0 5px}}header p{{margin:4px 0 8px;line-height:1.4}}input,select{{font:inherit;padding:8px;border:1px solid #aab8c0;border-radius:5px}}
#search{{width:min(460px,100%)}}main{{padding:18px;display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px}}
article{{background:white;border-radius:9px;padding:13px;min-width:0;box-shadow:0 1px 5px #0001}}article[hidden]{{display:none}}
h2{{font-size:14px;overflow-wrap:anywhere;margin:0 0 7px}}.selected,.retained-output{{display:flex;align-items:center;flex-direction:column;gap:5px;background:#f5f7f7;padding:8px}}
.selected img,.retained-output img{{width:128px;height:128px;object-fit:contain}}.selected span,.retained-output span{{font-size:12px;color:#516572}}.retained-output[hidden]{{display:none}}
.badge{{font-size:12px;color:#566b78;margin:7px 0 4px}}
.preview-links{{font-size:12px;margin:0 0 8px}}.preview-links a{{color:#164c67}}
.saved-grid{{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}}.saved-fill{{margin:0;width:112px;text-align:center;background:#f6f8f9;padding:6px;border-radius:5px}}
.saved-fill img{{width:88px;height:88px;object-fit:contain}}.saved-fill figcaption{{font-size:11px;overflow-wrap:anywhere;min-height:30px}}
body:not(.show-duplicates) .saved-fill.duplicate{{display:none}}
body:not(.show-removed) .saved-fill.removed,body:not(.show-removed) .selected.removed{{display:none}}
body.show-removed .saved-fill.removed{{display:block}}
.duplicate-note{{font-size:11px;color:#68808d;margin:5px 0}}
.saved-fill button,.selected button,.mark-controls button,.feedback-controls button{{border:1px solid #9baeb8;border-radius:5px;background:#f7fafb;color:#18252e;padding:6px;cursor:pointer}}
.saved-fill button,.selected button{{margin:2px}}
button[data-action="toggle_remove_variant"]{{color:#8d2631}}
.saved-fill button[aria-pressed="true"],.selected button[aria-pressed="true"],.mark-controls button[aria-pressed="true"]{{background:#164c67;color:#fff;border-color:#164c67}}
.no-saved{{font-size:12px;color:#687c87}}.mark-controls{{display:flex;gap:5px;align-items:center;flex-wrap:wrap;margin:8px 0}}
.mark-state{{font-size:11px;color:#516572}}.feedback-controls{{display:flex;gap:5px;align-items:flex-end}}
.feedback-controls label{{flex:1;font-size:12px;color:#516572}}textarea{{display:block;width:100%;min-height:43px;resize:vertical;border:1px solid #9baeb8;border-radius:5px;padding:6px;font:12px system-ui}}
.feedback-controls button{{white-space:nowrap}}.note{{font-size:12px;color:#225b3d;background:#eaf5ee;padding:5px;border-radius:4px}}
article[data-has-feedback="true"] textarea{{border-color:#337458}}.error{{color:#a12323}}#save-status{{margin-left:8px}}
</style>
<body><header><h1>Side main 48 · Fill outputs</h1>
<p>{len(records)} current main sources · {summary}</p>
<p>Each visually distinct Fill is shown directly. {total_duplicates} near-duplicate saved views are hidden; every SVG remains preserved. Keep multiple variants or remove saved variants from this review.</p>
<input id="search" type="search" placeholder="Search main icon" aria-label="Search main icons">
<select id="mark-filter" aria-label="Filter review choices"><option value="all">All icons</option><option value="selected">With kept variants</option><option value="feedback">With feedback</option><option value="retain">Retain original</option><option value="fix_small_dot">Fix small dot</option><option value="unmarked">Unmarked</option></select>
<label><input id="show-duplicates" type="checkbox"> Show matching saved variants</label>
<label><input id="show-removed" type="checkbox"> Show removed variants</label>
<span id="shown"></span><span id="save-status" role="status"></span></header>
<main>{''.join(cards)}</main><script src="../../main48-review.js"></script></body></html>'''


def build(workers: int = 6) -> dict:
    if workers < 1:
        raise ValueError("workers must be positive")
    files = sorted(SOURCE.glob("*.svg"))
    if not files:
        raise ValueError("No 48px main sources")
    (OUTPUT / "proposals/svg").mkdir(parents=True, exist_ok=True)
    (OUTPUT / "svg").mkdir(parents=True, exist_ok=True)
    decisions = json.loads(DECISIONS.read_text()).get("decisions", {}) if DECISIONS.exists() else {}
    marks = json.loads(MARKS.read_text()).get("marks", {}) if MARKS.exists() else {}
    current, alternates = saved_variants()
    # A decision changes the script draft when it names an action; its "variants" are extra
    # reviewed script drafts (each its own region/stroke decision), offered beside the others.
    jobs = [(str(path), str(OUTPUT / "proposals"),
             decisions.get(path.stem) if decisions.get(path.stem, {}).get("action") else None)
            for path in files]
    variant_jobs = []
    for path in files:
        for variant, decision in decisions.get(path.stem, {}).get("variants", {}).items():
            (OUTPUT / "script-variants" / path.stem / variant / "svg").mkdir(parents=True, exist_ok=True)
            variant_jobs.append((path.stem, variant, decision.get("reason", ""),
                                 (str(path), str(OUTPUT / "script-variants" / path.stem / variant), decision)))
    with ProcessPoolExecutor(max_workers=workers) as pool:
        proposals = list(pool.map(draft_one, jobs, chunksize=4))
        drafted = list(pool.map(draft_one, [job for *_, job in variant_jobs], chunksize=1))
    script_variants = defaultdict(list)
    for (name, variant, reason, _job), row in zip(variant_jobs, drafted):
        if row["status"] == "error":
            raise ValueError(f"Script variant failed: {name} {variant}: {row.get('error')}")
        path = OUTPUT / "script-variants" / name / variant / "svg" / f"{name}.svg"
        script_variants[name].append({"variant": variant, "reason": reason, "status": row["status"],
                                      "source_sha256": row["source_sha256_at_run"],
                                      "path": str(path.relative_to(OUTPUT)), "sha256": sha(path.read_bytes())})
    records = []
    render_cache = {}
    for row in proposals:
        if row["status"] == "error":
            records.append(row)
            continue
        name = row["name"]
        saved_current, saved_alternates = visual_duplicates(
            row, current.get(name), alternates.get(name, []), render_cache)
        records.append(select_one(row, marks.get(name), saved_current, saved_alternates,
                                  script_variants=script_variants.get(name, [])))
    counts = dict(Counter(row["status"] for row in records))
    duplicate_count = sum(bool(row.get("current_fill") and row["current_fill"].get("duplicate_of"))
                          + sum(bool(item.get("duplicate_of")) for item in row.get("approved_alternates", []))
                          for row in records)
    manifest = {
        "schema": "side-main48-region-fill-review/v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_folder": str(SOURCE),
        "preserved_fill_folder": str(PRESERVED),
        "source_policy": "Working sources are re-read on every run; source hashes invalidate saved choices.",
        "review_status": "script_drafts_for_user_review; saved Fill variants preserved",
        "total": len(records), "counts": counts,
        "visual_duplicate_count": duplicate_count, "records": records,
    }
    (OUTPUT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    (OUTPUT / "errors.json").write_text(json.dumps([r for r in records if r["status"] == "error"], indent=2) + "\n")
    (OUTPUT / "index.html").write_text(gallery(records))
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=6)
    args = parser.parse_args()
    manifest = build(args.workers)
    print(json.dumps({"total": manifest["total"], "counts": manifest["counts"],
                      "output_folder": str(OUTPUT)}, indent=2))


if __name__ == "__main__":
    main()
