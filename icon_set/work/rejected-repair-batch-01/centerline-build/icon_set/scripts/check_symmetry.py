#!/usr/bin/env python3
"""Check ink-triggered centerline symmetry for registered icons.

Examples:
  python3 icon_set/scripts/check_symmetry.py --icon airmail
  python3 icon_set/scripts/check_symmetry.py --family solo
  python3 icon_set/scripts/check_symmetry.py

Writes JSON measurements and an HTML report. Exit 0: no mismatches;
1: centerline mismatch; 2: checker/input error. Does not change any icon.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import html
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from icon_set.validation.symmetry import RULES, analyze, failure_messages

# Inline HTML requires <svg>, not ElementTree's default <ns0:svg> tags.
ET.register_namespace('', 'http://www.w3.org/2000/svg')


def icon_preview(document):
    root = ET.fromstring(document)
    root.set('width', '240')
    root.set('height', '240')
    root.set('role', 'img')
    root.set('aria-label', 'SVG icon at its authored stroke width')
    return ET.tostring(root, encoding='unicode')


def overlay(document, axis):
    root = ET.fromstring(document)
    root.set('width', '320')
    root.set('height', '320')
    root.set('stroke', '#2563eb')
    root.set('stroke-width', '0.18')
    root.set('aria-label', 'Blue authored centerlines; red reflected centerlines')
    group = ET.SubElement(root, 'g', {'stroke': '#e11d48', 'opacity': '0.8'})
    coordinate = axis['coordinate']
    group.set('transform', f'translate({2*coordinate} 0) scale(-1 1)' if axis['axis'] == 'vertical'
              else f'translate(0 {2*coordinate}) scale(1 -1)')
    for child in list(root):
        if child is not group and child.tag.rsplit('}', 1)[-1] == 'path':
            clone = ET.fromstring(ET.tostring(child))
            clone.attrib.pop('id', None)
            group.append(clone)
    for mismatch in axis['mismatches']:
        x, y = mismatch['mirrored_point']
        ET.SubElement(root, 'circle', {'cx': str(x), 'cy': str(y), 'r': '0.8',
                                     'stroke': '#e11d48', 'stroke-width': '0.12', 'fill': 'none'})
    return ET.tostring(root, encoding='unicode')


def write_report(rows, output):
    summary = dict(Counter(row['status'] for row in rows))
    output.mkdir(parents=True, exist_ok=True)
    report = {'rules': RULES, 'summary': summary,
              'icons': [{k: v for k, v in row.items() if k != '_svg'} for row in rows]}
    (output/'results.json').write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    cards = []
    for row in sorted(rows, key=lambda r: (r['status'] not in ('fail', 'error'), r['icon_id'])):
        detail = []
        for axis in row.get('axes', []):
            if not axis['ink_symmetric']:
                continue
            detail.append(f"<h3>{axis['axis'].title()} axis {axis['coordinate']:g}: "
                          f"{axis['ink_iou']:.3%} ink overlap — {axis['status']}</h3>")
            detail.append(overlay(row['_svg'], axis))
            for item in axis['mismatches']:
                detail.append(f"<p><code>{html.escape(item['element_id'])}</code>: "
                              f"{item['distance']:.6g} units near {item['mirrored_point']}</p>")
        preview = ('<section class="icon-preview"><h3>SVG icon</h3>' + icon_preview(row['_svg']) + '</section>'
                   if row.get('_svg') else '')
        cards.append(f"<article><h2>{html.escape(row['icon_id'])} · {row['status']}</h2>" +
                     '<div class="comparison">' + preview + '<section>' + ''.join(detail) + '</section></div>' +
                     ''.join(f'<p>{html.escape(e)}</p>' for e in row.get('errors', [])) +
                     ('<p>No likely horizontal or vertical mirror axis.</p>' if row['status'] == 'not_applicable' else '') +
                     '</article>')
    (output/'index.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8">
<title>Icon symmetry check</title><style>
body{font:16px system-ui;margin:40px auto;max-width:1050px;padding:0 24px;background:#f5f6f8;color:#172033}
article{background:white;border:1px solid #ddd;border-radius:12px;padding:24px;margin:20px 0}
svg{display:block;width:320px;height:320px}code{background:#eee;padding:3px}h3{font-size:17px}
.comparison{display:flex;align-items:flex-start;gap:32px;flex-wrap:wrap}
.icon-preview{color:#172033;flex:0 0 240px}.icon-preview svg{width:240px;height:240px}
</style><h1>Icon symmetry check</h1>
<p>Ink overlap ≥ 98% triggers a centerline check on the same axis. Centerline tolerance: 0.0001 units.
Blue: authored paths. Red: reflected paths. Red circles mark mismatches.</p>
<p>Curve chord error ≤ 0.00001 units. Sampled geometry; horizontal and vertical axes only.
Near-symmetry is a heuristic and may flag deliberate small asymmetries.</p>''' +
        '<p>'+html.escape(str(summary))+'</p>' + ''.join(cards) + '</html>')
    return summary


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--icon', action='append', help='registered icon ID; repeat for multiple icons')
    parser.add_argument('--family', choices=['solo', 'sub', 'container'], action='append')
    parser.add_argument('--out', type=Path, default=ROOT/'work/symmetry-check')
    args = parser.parse_args(argv)
    from icon_set.model.icons.registry import factories
    registry = factories()
    unknown = set(args.icon or ()) - registry.keys()
    if unknown:
        parser.error('unknown icon IDs: ' + ', '.join(sorted(unknown)))
    selected = [(name, factory) for name, factory in sorted(registry.items())
                if (not args.icon or name in args.icon) and (not args.family or factory.family in args.family)]
    if not selected:
        parser.error('no icons match the requested selection')
    rows = []
    for index, (name, factory) in enumerate(selected, 1):
        try:
            icon = factory()
            document = icon.to_svg()
            result = analyze(icon, document=document)
            rows.append(dict(icon_id=name, family=factory.family, _svg=document,
                             svg_sha256=hashlib.sha256(document.encode()).hexdigest(), **result))
            for message in failure_messages(result):
                print(f'{name}: {message}', flush=True)
        except Exception as error:
            rows.append(dict(icon_id=name, family=factory.family, status='error',
                             errors=[f'{type(error).__name__}: {error}']))
            print(f'{name}: checker error: {error}', file=sys.stderr, flush=True)
        if index % 50 == 0:
            print(f'Checked {index}/{len(selected)}', flush=True)
    summary = write_report(rows, args.out)
    print(json.dumps(summary, indent=2))
    print(args.out/'index.html')
    return 2 if summary.get('error') else (1 if summary.get('fail') else 0)


if __name__ == '__main__':
    raise SystemExit(main())
