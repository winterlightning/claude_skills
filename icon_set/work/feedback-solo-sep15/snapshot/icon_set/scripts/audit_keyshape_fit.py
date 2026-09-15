"""Audit all registered solo fitting candidates without modifying the library.

Run with python3 -m icon_set.scripts.audit_keyshape_fit.
"""
from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
import html
import json
from pathlib import Path

from icon_set.model.icons.registry import create, factories
from icon_set.model.keyshapes import Keyshape


def inspect_fit(icon_id, force_stretch=False):
    try:
        icon = create(icon_id)
        target = icon.keyshape
        if target.orientation == "landscape":
            target = Keyshape.HRECT_L
        elif target.orientation == "portrait":
            target = Keyshape.VRECT_L
        result = icon.fit_to_keyshape(target, force_stretch=force_stretch)
        report = result.report
        report["original_keyshape"] = icon.keyshape.name
        report["_before_svg"] = icon.to_svg()
        report["_after_svg"] = result.icon.to_svg()
        return report
    except Exception as error:
        return {"source_icon_id": icon_id, "validation": {
            "status": "error", "errors": [f"{type(error).__name__}: {error}"],
            "warnings": []}}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("icon_set/work/keyshape-fit-audit"))
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--force-stretch", action="store_true",
                        help="Stretch width and height independently for rectangular keyshapes")
    args = parser.parse_args(argv)
    if args.workers < 1:
        parser.error("--workers must be positive")
    ids = sorted(key for key, factory in factories().items() if factory.family == "solo")
    args.output.mkdir(parents=True, exist_ok=True)
    print(f"Auditing {len(ids)} solo icons with {args.workers} workers", flush=True)
    rows = []
    # Retain completed results even if an audit is interrupted.
    with (args.output / "progress.jsonl").open("w", encoding="utf-8") as progress:
        with ProcessPoolExecutor(max_workers=args.workers) as pool:
            futures = {pool.submit(inspect_fit, icon_id, args.force_stretch): icon_id for icon_id in ids}
            for future in as_completed(futures):
                row = future.result()
                icon_id = row["source_icon_id"]
                previews = {}
                for name in ("before", "after"):
                    document = row.pop(f"_{name}_svg", None)
                    if document is not None:
                        relative = Path("svg") / f"{icon_id}-{name}.svg"
                        (args.output / relative).parent.mkdir(parents=True, exist_ok=True)
                        (args.output / relative).write_text(document, encoding="utf-8")
                        previews[name] = relative.as_posix()
                row["previews"] = previews
                rows.append(row)
                progress.write(json.dumps(row) + "\n")
                progress.flush()
                if len(rows) % 25 == 0 or len(rows) == len(ids):
                    counts = Counter(r["validation"]["status"] for r in rows)
                    print(f"{len(rows)}/{len(ids)}: {dict(counts)}", flush=True)
    rows.sort(key=lambda r: r["source_icon_id"])
    statuses = Counter(r["validation"]["status"] for r in rows)
    failures = Counter()
    for row in rows:
        failures.update({error.split(":", 1)[0].split(" [", 1)[0]
                         for error in row["validation"]["errors"]})
    summary = {
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "mode": "force-stretch" if args.force_stretch else "uniform",
        "scope": ("All registered solo icons, including variants; "
                  + ("independent width/height stretching (circles retain radial fitting)" if args.force_stretch else "uniform fitting")
                  + " to the current keyshape orientation, then integer snapping and full QA."),
        "total": len(rows),
        "statuses": {name: statuses[name] for name in ("pass", "fail", "review", "error")},
        "icons_by_failure_check": dict(failures),
        "numeric_pass_with_internal_spacing_advisory": sum(
            r["validation"]["status"] == "pass" and bool(r["validation"].get("needs_review")) for r in rows),
        "note": "Failure categories overlap. Numeric passes still need visual review. Library files and exception flags were not changed.",
    }
    (args.output / "results.json").write_text(json.dumps({"summary": summary, "icons": rows}, indent=2) + "\n", encoding="utf-8")
    write_gallery(args.output, summary, rows)
    print(json.dumps(summary, indent=2), flush=True)


def write_gallery(output, summary, rows):
    cards = []
    for row in rows:
        qa = row["validation"]
        messages = qa["errors"] + qa["warnings"] + row.get("notes", [])
        if qa.get("needs_review"):
            messages.append("Internal spacing advisory: review required")
        findings = "".join(f"<li>{html.escape(message)}</li>" for message in messages)
        icon_id = html.escape(row["source_icon_id"])
        previews = []
        for name, label in (("before", summary.get("before_label", "Original")),
                            ("after", summary.get("after_label", "Fitted candidate"))):
            relative = row.get("previews", {}).get(name)
            if relative:
                svg = (output / relative).read_text(encoding="utf-8")
                # Inline the renderer's SVG so currentColor follows the theme.
                svg = svg[svg.index("<svg"):]
                previews.append(f'<div class="preview"><a href="{html.escape(relative)}">{label}</a>'
                                f'<div class="large">{svg}</div><div class="native">{svg}</div>'
                                '<small>48 px</small></div>')
            else:
                previews.append(f'<div class="preview">{label}: preview unavailable</div>')
        status = qa["status"]
        repaired = row.get('previous_status') == 'fail' and status == 'pass'
        cards.append((status, repaired, f'<article data-status="{status}" data-repaired="{str(repaired).lower()}" data-name="{icon_id}">'
            f'<div class="card-head"><span class="badge {status}">{status.upper()}</span>'
            f'<span>{html.escape(row.get("target_keyshape", "—"))}</span></div>'
            f'<h2>{icon_id}</h2><div class="pair">{"".join(previews)}</div>'
            + ('<p class="advisory">Spacing advisory</p>' if qa.get("needs_review") else '')
            + (f'<details><summary>Findings ({len(messages)})</summary><ul>{findings}</ul></details>'
               if messages else '<p class="clean">All numeric checks passed</p>') + '</article>'))
    style = '''
    :root{color-scheme:light;--bg:#f3f5f8;--card:#fff;--ink:#172238;--line:#d9e0ea}
    body.dark{color-scheme:dark;--bg:#10151f;--card:#1a2332;--ink:#edf2fa;--line:#38455c}
    *{box-sizing:border-box}body{font:15px system-ui;background:var(--bg);color:var(--ink);margin:0;padding:32px}
    header,main{max-width:1500px;margin:auto}h1{font-size:30px;margin:0 0 8px}header p{line-height:1.5}
    a{color:inherit}nav{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin:24px 0}
    input,select,button{font:inherit;padding:10px 14px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--ink)}
    input{min-width:240px}#count{margin-left:auto}main{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:18px}
    article{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px;overflow:hidden}
    article[hidden]{display:none}.card-head{display:flex;justify-content:space-between;align-items:center;font-size:12px}
    .badge{padding:4px 9px;border-radius:6px;font-weight:700}.pass{background:#d5f4e2;color:#135836}.fail,.error{background:#ffe1df;color:#92271f}.review{background:#fff0c9;color:#725000}
    h2{font-size:16px;overflow-wrap:anywhere;min-height:40px;margin:14px 0}.pair{display:flex;gap:12px;justify-content:space-around}
    .preview{text-align:center;flex:1;min-width:0}.preview a{font-size:12px}.large{height:150px;display:grid;place-items:center}
    .large svg{width:144px;height:144px}.native svg{width:48px;height:48px}small{font-size:11px;opacity:.65}
    details{font-size:12px;line-height:1.5;margin-top:12px}li{margin-bottom:8px;overflow-wrap:anywhere}ul{padding-left:16px}
    .clean,.advisory{font-size:12px;margin-bottom:0}.advisory{color:#ab6910}
    @media(max-width:600px){body{padding:16px}main{grid-template-columns:1fr}#count{margin-left:0}}
    '''
    script = '''
    const cards=[...document.querySelectorAll('article')], filter=document.querySelector('#filter'), search=document.querySelector('#search');
    function update(){let n=0;for(const card of cards){const show=(filter.value==='all'||card.dataset.status===filter.value||(filter.value==='repaired'&&card.dataset.repaired==='true'))&&card.dataset.name.includes(search.value.trim().toLowerCase());card.hidden=!show;if(show)n++;}document.querySelector('#count').textContent=n+' icons shown';}
    filter.addEventListener('change',update);search.addEventListener('input',update);
    document.querySelector('#theme').addEventListener('click',()=>{const dark=document.body.classList.toggle('dark');document.querySelector('#theme').textContent=dark?'Light theme':'Dark theme';});update();
    '''
    counts = summary["statuses"]
    pages = [("index.html", "all"), ("passed.html", "pass"),
             ("failed.html", "fail"), ("review.html", "review")]
    if 'repaired_to_pass' in summary:
        pages.append(('repaired.html', 'repaired'))
    for filename, selected in pages:
        options = ''.join(f'<option value="{value}"{" selected" if value == selected else ""}>{label}</option>'
                          for value, label in [("all", f'All ({summary["total"]})'),
                                               ("pass", f'Passed ({counts["pass"]})'),
                                               ("fail", f'Failed ({counts["fail"]})'),
                                               ("review", f'Review ({counts["review"]})'),
                                               ("error", f'Errors ({counts["error"]})')]
                          + ([('repaired', f'Newly repaired ({summary["repaired_to_pass"]})')] if 'repaired_to_pass' in summary else []))
        content = ''.join(card if selected == "all" or status == selected or (selected == 'repaired' and repaired)
                          else card.replace('<article ', '<article hidden ', 1) for status, repaired, card in cards)
        (output / filename).write_text(
            '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>Solo fitting audit — SVG gallery</title><style>' + style + '</style></head><body><header>'
            f'<h1>Solo keyshape fitting — {html.escape(summary.get("mode", "uniform"))}</h1><p><strong>{counts["pass"]} passed · {counts["fail"]} failed · {counts["review"]} review · {counts["error"]} errors</strong> out of {summary["total"]} solo icons.<br>'
            'Before and after SVGs at 3× and native size. Numeric passes still need visual review; '
            f'{summary["numeric_pass_with_internal_spacing_advisory"]} passing icons have spacing advisories.</p>'
            '<p><a href="passed.html">View passing icons</a> · <a href="failed.html">Failed icons</a> · <a href="review.html">Icons needing review</a> · <a href="index.html">All icons</a> · <a href="results.json">Full JSON report</a>'
            + (' · <a href="repaired.html">Newly repaired icons</a>' if 'repaired_to_pass' in summary else '') + '</p>'
            '<nav><label>Status <select id="filter">' + options + '</select></label>'
            '<input id="search" type="search" placeholder="Search icon name" aria-label="Search icon name">'
            '<button id="theme">Dark theme</button><span id="count" aria-live="polite"></span></nav></header>'
            '<main>' + content + '</main><script>' + script + '</script></body></html>', encoding="utf-8")


if __name__ == "__main__":
    main()
