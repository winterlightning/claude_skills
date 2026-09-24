#!/usr/bin/env python3
"""Report page for every primitive-make-ray run: failed, review and passed icons.

Scans icon_set/work/primitive-make-ray/<source-uuid>/<run>/result.json, takes the
newest run per source, and writes a self-contained index.html (plus report.json)
next to this script. Reference artwork is rendered to small PNGs; results are
inlined as SVG so the page works from file:// or any static server.

    python3 icon_set/work/primitive-make-ray-report/build_report.py
"""
from __future__ import annotations

import base64
import html
import json
import re
import sqlite3
import sys
import urllib.request
from collections import Counter
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
RUNS = REPO / 'icon_set' / 'work' / 'primitive-make-ray'
REFS = REPO / 'icon_set' / 'work' / 'todo-references'
ORIGINALS = REPO / 'pictographic-primitives'
CATALOG = REPO / 'published' / 'gallery' / 'primitives.json'
DATABASE = REPO / 'icon_set' / 'state' / 'feedback.sqlite3'
API = 'http://127.0.0.1:8000'
UUID = re.compile(r'([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})', re.I)
sys.path.insert(0, str(REPO))


def fetch_json(url, fallback):
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            return json.load(response)
    except Exception:
        return fallback()


def load_catalog():
    def from_file():
        return json.loads(CATALOG.read_text(encoding='utf-8')) if CATALOG.is_file() else {'rows': []}
    return fetch_json(API + '/gallery/primitives.json', from_file)


def load_statuses():
    def from_db():
        if not DATABASE.is_file():
            return {}
        from icon_set.scripts.primitive_status import load_status
        with closing(sqlite3.connect(DATABASE, timeout=10)) as connection:
            return load_status(connection)
    return fetch_json(API + '/api/primitives/status', from_db)


def effective(row, statuses):
    if not row:
        return 'unknown'
    if row.get('state') == 'generated':
        return 'generated'
    if statuses.get(row['uuid']):
        return 'skip'
    if row.get('models') or row.get('state') in ('model_only', 'build_failed'):
        return 'drawn'
    return 'todo'


def render_png(svg_path: Path, size=96) -> str:
    try:
        import cairosvg
        data = cairosvg.svg2png(url=str(svg_path), output_width=size, output_height=size)
        return 'data:image/png;base64,' + base64.b64encode(data).decode()
    except Exception:
        return ''


def findings_of(result: dict, run: Path) -> list[str]:
    lines = []
    text = result.get('validation_findings')
    if isinstance(text, str) and text.strip():
        lines = text.splitlines()
    else:
        for key in ('validation_errors', 'validation_warnings'):
            value = result.get(key)
            if isinstance(value, list):
                lines += [str(v) for v in value]
        if not lines and (run / 'validation.txt').is_file():
            lines = (run / 'validation.txt').read_text(encoding='utf-8', errors='replace').splitlines()
    lines = [l.strip() for l in lines if l.strip() and not l.strip().lower().startswith('status:')]
    return lines


def result_svg(result: dict, run: Path) -> str:
    candidates = []
    artifacts = result.get('artifacts')
    if isinstance(artifacts, dict):
        for key in ('svg', 'icon_svg', 'result_svg'):
            if isinstance(artifacts.get(key), str):
                candidates.append(artifacts[key])
        candidates += [v for v in artifacts.values() if isinstance(v, str) and v.endswith('.svg')]
    if isinstance(result.get('svg'), str):
        candidates.append(result['svg'])
    for name in candidates:
        path = run / name
        if path.is_file() and not path.name.startswith('reference'):
            return path.read_text(encoding='utf-8', errors='replace')
    for path in sorted(run.glob('*.svg')):
        if not path.name.startswith('reference') and 'debug' not in path.name:
            return path.read_text(encoding='utf-8', errors='replace')
    return ''


def clean_svg(svg: str) -> str:
    svg = re.sub(r'<\?xml[^>]*\?>', '', svg)
    svg = re.sub(r'<title>.*?</title>', '', svg, flags=re.S)
    svg = re.sub(r'\s(width|height)="[^"]*"', '', svg, count=2)
    return svg.strip()


def reference_for(uuid: str, row: dict | None) -> Path | None:
    for path in REFS.glob(f'*_{uuid}.svg'):
        return path
    if row and row.get('path') and (ORIGINALS / row['path']).is_file():
        return ORIGINALS / row['path']
    return None


def bucket(status: str) -> str:
    return {'valid': 'passed', 'review': 'review', 'invalid': 'failed', 'error': 'failed'}.get(status, 'failed')


def main() -> int:
    catalog = load_catalog()
    statuses = load_statuses()
    rows = {r['uuid']: r for r in catalog.get('rows', [])}
    for r in catalog.get('rows', []):
        for alias in r.get('aliases', []) or []:
            rows.setdefault(alias.get('uuid'), r)
    sources = []
    for source_dir in sorted(RUNS.iterdir()):
        if not source_dir.is_dir():
            continue
        match = UUID.search(source_dir.name)
        if not match:
            continue
        uuid = match.group(1).lower()
        runs = []
        for run in source_dir.iterdir():
            result_path = run / 'result.json'
            if not run.is_dir() or not result_path.is_file():
                continue
            try:
                result = json.loads(result_path.read_text(encoding='utf-8'))
            except ValueError:
                result = {'validation_status': 'error', 'icon_id': '', 'error': 'unreadable result.json'}
            lines = findings_of(result, run)
            runs.append({'run': run.name, 'dir': run, 'result': result,
                         'status': str(result.get('validation_status') or 'error'),
                         'errors': sum(l.startswith('ERROR') for l in lines),
                         'warnings': sum(l.startswith('WARN') for l in lines),
                         'findings': lines, 'mtime': result_path.stat().st_mtime})
        row = rows.get(uuid)
        ref = reference_for(uuid, row)
        concept = (row or {}).get('old_concept') or (ref.name.rsplit('_', 1)[0] if ref else source_dir.name)
        if not runs:
            sources.append({'uuid': uuid, 'concept': concept, 'category': (row or {}).get('category', ''),
                            'gallery': effective(row, statuses), 'bucket': 'failed', 'status': 'no result',
                            'runs': [], 'latest': None, 'svg': '', 'reference': ref, 'dir': source_dir})
            continue
        runs.sort(key=lambda r: r['mtime'])
        latest = runs[-1]
        sources.append({'uuid': uuid, 'concept': concept, 'category': (row or {}).get('category', ''),
                        'gallery': effective(row, statuses), 'bucket': bucket(latest['status']),
                        'status': latest['status'], 'runs': runs, 'latest': latest,
                        'svg': clean_svg(result_svg(latest['result'], latest['dir'])), 'reference': ref, 'dir': source_dir})

    order = {'failed': 0, 'review': 1, 'passed': 2}
    sources.sort(key=lambda s: (order[s['bucket']], s['concept'].lower()))
    counts = Counter(s['bucket'] for s in sources)
    gallery_counts = Counter(s['gallery'] for s in sources)
    generated = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

    esc = html.escape
    cards = []
    for s in sources:
        latest = s['latest']
        ref_png = render_png(s['reference']) if s['reference'] else ''
        ref_html = f'<img src="{ref_png}" alt="" width="96" height="96">' if ref_png else '<span class="none">no reference</span>'
        res_html = s['svg'] or '<span class="none">no svg</span>'
        run_dir = s['dir'].relative_to(HERE.parent) if latest is None else latest['dir'].relative_to(HERE.parent)
        icon_id = (latest or {}).get('result', {}).get('icon_id', '') if latest else ''
        author = (latest or {}).get('result', {}).get('author', '') if latest else ''
        findings = (latest or {}).get('findings', []) if latest else []
        badges = []
        if latest:
            if latest['errors']:
                badges.append(f'<b class="err">{latest["errors"]} error{"s" if latest["errors"] != 1 else ""}</b>')
            if latest['warnings']:
                badges.append(f'<b class="warn">{latest["warnings"]} warning{"s" if latest["warnings"] != 1 else ""}</b>')
        badges.append(f'<b class="gal {esc(s["gallery"])}">{esc(s["gallery"])}</b>')
        runs_html = ''.join(
            f'<li><a href="../{esc(str(r["dir"].relative_to(HERE.parent)))}/">{esc(r["run"])}</a> · {esc(r["status"])}'
            f'{" · " + str(r["errors"]) + " err" if r["errors"] else ""}{" · " + str(r["warnings"]) + " warn" if r["warnings"] else ""}</li>'
            for r in reversed(s['runs']))
        find_html = ('<details><summary>Findings</summary><pre>' + esc('\n'.join(findings)) + '</pre></details>') if findings else ''
        search = ' '.join([s['concept'], s['uuid'], icon_id, s['category'], s['status'], s['gallery'], author]).lower()
        cards.append(
            f'<article class="card {s["bucket"]}" data-bucket="{s["bucket"]}" data-category="{esc(s["category"])}" '
            f'data-gallery="{esc(s["gallery"])}" data-search="{esc(search)}">'
            f'<div class="art"><figure><div class="ref">{ref_html}</div><figcaption>reference</figcaption></figure>'
            f'<figure><div class="res">{res_html}</div><figcaption>{esc(s["status"])}</figcaption></figure></div>'
            f'<h3>{esc(s["concept"])}</h3>'
            f'<p class="meta">{esc(icon_id)}{" · " if icon_id and s["category"] else ""}{esc(s["category"])}{" · " + esc(author) if author else ""}</p>'
            f'<p class="badges">{"".join(badges)}</p>'
            f'{find_html}'
            f'<details><summary>{len(s["runs"])} run{"s" if len(s["runs"]) != 1 else ""} · <code>{esc(s["uuid"])}</code></summary><ul class="runs">{runs_html}</ul></details>'
            f'<p class="links"><a href="../{esc(str(run_dir))}/">open run folder</a></p>'
            f'</article>')

    categories = sorted({s['category'] for s in sources if s['category']}, key=str.lower)
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Make-ray results</title>
<meta name="description" content="Failed, review and passed icons from every primitive-make-ray run, newest run per source.">
<style>
:root{{--bg:#f6f7f4;--card:#fff;--ink:#1c211e;--muted:#66706a;--line:#dfe4de;--fail:#c2413a;--fail-bg:#fbeceb;--warn:#a8690f;--warn-bg:#fbf1dc;--pass:#2c7a3f;--pass-bg:#e6f3e8;--accent:#2f5d8a;--chip:#eceee9}}
@media(prefers-color-scheme:dark){{:root:not([data-theme=light]){{--bg:#151816;--card:#1e2320;--ink:#e8ebe6;--muted:#9aa39d;--line:#2d3430;--fail:#f08c85;--fail-bg:#3a2321;--warn:#e6b25a;--warn-bg:#3a2f18;--pass:#7fcf92;--pass-bg:#1f3527;--accent:#8fb6dd;--chip:#2a302c}}}}
:root[data-theme=dark]{{--bg:#151816;--card:#1e2320;--ink:#e8ebe6;--muted:#9aa39d;--line:#2d3430;--fail:#f08c85;--fail-bg:#3a2321;--warn:#e6b25a;--warn-bg:#3a2f18;--pass:#7fcf92;--pass-bg:#1f3527;--accent:#8fb6dd;--chip:#2a302c}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:14px/1.5 system-ui,-apple-system,Segoe UI,sans-serif}}
main{{max-width:1500px;margin:0 auto;padding:24px 16px 60px}}h1{{font-size:26px;margin:0 0 4px}}.sub{{color:var(--muted);margin:0 0 18px}}
.stats{{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:18px}}.stat{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 14px;min-width:130px}}
.stat span{{display:block;color:var(--muted);font-size:12px}}.stat strong{{font-size:22px}}.stat.failed strong{{color:var(--fail)}}.stat.review strong{{color:var(--warn)}}.stat.passed strong{{color:var(--pass)}}
.toolbar{{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:16px;position:sticky;top:0;background:var(--bg);padding:10px 0;z-index:2}}
.chip{{border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:999px;padding:6px 14px;cursor:pointer;font:inherit}}.chip[aria-pressed=true]{{background:var(--ink);color:var(--bg);border-color:var(--ink)}}
input,select{{font:inherit;padding:7px 10px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--ink)}}input{{min-width:220px;flex:1}}
.count{{color:var(--muted);margin-left:auto}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,300px),1fr));gap:12px}}
.card{{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--line);border-radius:10px;padding:12px;min-width:0}}
.card.failed{{border-left-color:var(--fail)}}.card.review{{border-left-color:var(--warn)}}.card.passed{{border-left-color:var(--pass)}}
.art{{display:flex;gap:10px}}figure{{margin:0;flex:1;text-align:center}}figcaption{{font-size:11px;color:var(--muted);margin-top:4px}}
.ref,.res{{height:112px;display:grid;place-items:center;border:1px solid var(--line);border-radius:8px;background:#fff;color:#111}}
.res svg{{width:96px;height:96px}}.ref img{{image-rendering:auto}}
@media(prefers-color-scheme:dark){{:root:not([data-theme=light]) .res{{background:#111;color:#fff}}}}:root[data-theme=dark] .res{{background:#111;color:#fff}}
.none{{color:var(--muted);font-size:12px}}h3{{font-size:15px;margin:10px 0 2px;overflow-wrap:anywhere}}.meta{{margin:0;color:var(--muted);font-size:12px;overflow-wrap:anywhere}}
.badges{{margin:6px 0}}.badges b{{display:inline-block;font-weight:600;font-size:11px;border-radius:6px;padding:2px 7px;margin:0 6px 4px 0}}
.err{{color:var(--fail);background:var(--fail-bg)}}.warn{{color:var(--warn);background:var(--warn-bg)}}.gal{{background:var(--chip);color:var(--muted)}}.gal.generated{{color:var(--pass);background:var(--pass-bg)}}.gal.todo{{color:var(--fail);background:var(--fail-bg)}}
details{{margin:4px 0}}summary{{cursor:pointer;color:var(--accent);font-size:12px}}pre{{white-space:pre-wrap;overflow-wrap:anywhere;font-size:11px;background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:8px;margin:6px 0 0;max-height:220px;overflow:auto}}
.runs{{margin:4px 0 0;padding-left:18px;font-size:12px}}code{{font-size:11px}}a{{color:var(--accent)}}.links{{margin:4px 0 0;font-size:12px}}
.card[hidden]{{display:none}}.empty{{color:var(--muted);padding:30px;text-align:center}}
</style></head><body><main>
<h1>primitive-make-ray results</h1>
<p class="sub">Newest run per source across {len(sources)} sources · {sum(len(s["runs"]) for s in sources)} runs · built {generated}. Failed = invalid or error, review = warnings only, passed = valid. The gallery badge is the source's current Progression status.</p>
<div class="stats"><div class="stat failed"><span>Failed</span><strong>{counts["failed"]}</strong></div><div class="stat review"><span>Review</span><strong>{counts["review"]}</strong></div><div class="stat passed"><span>Passed</span><strong>{counts["passed"]}</strong></div>
<div class="stat"><span>Passed but still TODO in gallery</span><strong>{sum(1 for s in sources if s["bucket"] == "passed" and s["gallery"] == "todo")}</strong></div><div class="stat"><span>Generated (promoted)</span><strong>{gallery_counts["generated"]}</strong></div></div>
<div class="toolbar" role="group" aria-label="Filters">
<button class="chip" data-bucket="failed" aria-pressed="true">Failed</button><button class="chip" data-bucket="review" aria-pressed="false">Review</button><button class="chip" data-bucket="passed" aria-pressed="false">Passed</button><button class="chip" data-bucket="" aria-pressed="false">All</button>
<select id="category" aria-label="Category"><option value="">All categories</option>{"".join(f'<option value="{esc(c)}">{esc(c)}</option>' for c in categories)}</select>
<select id="gallery" aria-label="Gallery status"><option value="">Any gallery status</option><option value="todo">TODO</option><option value="generated">Generated</option><option value="drawn">Drawn</option><option value="skip">Skip</option></select>
<input id="q" type="search" placeholder="Search concept, icon id, uuid, author" aria-label="Search">
<span class="count" id="count"></span></div>
<div class="grid" id="grid">{"".join(cards)}</div><p class="empty" id="empty" hidden>Nothing matches.</p>
<script>
const cards=[...document.querySelectorAll('.card')],chips=[...document.querySelectorAll('.chip')];let bucket='failed';
function apply(){{const q=document.getElementById('q').value.trim().toLowerCase(),cat=document.getElementById('category').value,gal=document.getElementById('gallery').value;let n=0;
for(const c of cards){{const show=(!bucket||c.dataset.bucket===bucket)&&(!cat||c.dataset.category===cat)&&(!gal||c.dataset.gallery===gal)&&(!q||c.dataset.search.includes(q));c.hidden=!show;if(show)n++;}}
document.getElementById('count').textContent=n+' shown';document.getElementById('empty').hidden=n>0;}}
chips.forEach(b=>b.onclick=()=>{{bucket=b.dataset.bucket;chips.forEach(x=>x.setAttribute('aria-pressed',String(x===b)));apply();}});
for(const id of ['q','category','gallery'])document.getElementById(id).addEventListener('input',apply);
const p=new URLSearchParams(location.search);if(p.has('view')){{bucket=p.get('view');chips.forEach(x=>x.setAttribute('aria-pressed',String(x.dataset.bucket===bucket)));}}
apply();
</script></main></body></html>'''
    (HERE / 'index.html').write_text(page, encoding='utf-8')
    report = [{'uuid': s['uuid'], 'concept': s['concept'], 'category': s['category'], 'gallery_status': s['gallery'],
               'bucket': s['bucket'], 'status': s['status'],
               'icon_id': s['latest']['result'].get('icon_id', '') if s['latest'] else '',
               'latest_run': str(s['latest']['dir'].relative_to(REPO)) if s['latest'] else '',
               'errors': s['latest']['errors'] if s['latest'] else 0,
               'warnings': s['latest']['warnings'] if s['latest'] else 0,
               'findings': s['latest']['findings'] if s['latest'] else [],
               'runs': [str(r['dir'].relative_to(REPO)) for r in s['runs']]} for s in sources]
    (HERE / 'report.json').write_text(json.dumps({'built': generated, 'counts': dict(counts), 'sources': report}, indent=1), encoding='utf-8')
    print(f"{HERE / 'index.html'}: {counts['failed']} failed, {counts['review']} review, {counts['passed']} passed of {len(sources)} sources")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
