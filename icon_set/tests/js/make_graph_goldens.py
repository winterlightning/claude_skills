"""Write graph-goldens.json: svg_graph.graph_from_svg on the combined drawings of container-goldens.json and on
shapes that exercise every converter (rects with corners, circles, ellipses, polylines, quadratics, smooth curves,
rotated arcs, relative commands, coordinates on 1/32 that round half to even), for svg-graph.test.mjs.

    /opt/homebrew/bin/python3 icon_set/tests/js/make_graph_goldens.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2]))
from icon_set.scripts.svg_graph import graph_from_svg  # noqa: E402

HEAD = ('<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64" fill="none" '
        'stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">')
SHAPES = [
    '<g id="container"><rect x="2" y="6" width="60" height="52" rx="6"/></g><g id="symbol"><circle cx="32" cy="32" r="9.5"/></g>',
    '<g id="container"><rect x="4" y="4" width="56" height="56"/><line x1="4" y1="20" x2="60" y2="20"/></g>'
    '<g id="symbol"><ellipse cx="32" cy="40" rx="12" ry="7"/><polyline points="20,30 32,22 44,30"/></g>',
    '<g id="container"><polygon points="32 2 62 58 2 58"/></g><g id="symbol"><path d="M24 36Q32 20 40 36T56 36"/></g>',
    '<g id="symbol"><path d="M10 10C14 4 22 4 26 10S38 16 42 10"/><path d="m40 40 l8 0 l0 8 z"/></g>',
    '<g id="symbol"><path d="M20 32A12 6 30 0 1 44 32"/><path d="M20 44A12 12 0 1 0 44 44"/></g>',
    '<g id="container"><path d="M2.03125 4.09375L61.96875 4.15625H40.0003125"/></g><g><path d="M8 8h4v4"/></g>',
    '<title>t</title><path d="M8 56L56 8"/><rect x="10" y="10" width="8" height="8" rx="2" ry="3" stroke="none"/>',
    '<g id="symbol"><path d="M10 10L20 10M20 10L30 20M40 40L50 50L40 50Z"/></g>',
]


def main():
    cases = []
    for i, body in enumerate(SHAPES):
        svg = HEAD + body + '</svg>'
        cases.append({'name': f'shape-{i + 1}', 'svg': svg, 'graph': graph_from_svg(
            svg, canvas=64, family='container_combination64', icon_id=f'shape-{i + 1}', name='Shape', profile='CONTAINER64')})
    for c in json.loads((HERE / 'container-goldens.json').read_text()):
        if c.get('error'):
            continue
        svg = c['python']['svg']
        cases.append({'name': c['reference_id'], 'svg': svg, 'graph': graph_from_svg(
            svg, canvas=64, family='container_combination64', profile='CONTAINER64')})
    (HERE / 'graph-goldens.json').write_text(json.dumps(cases, separators=(',', ':')) + '\n')
    print(len(cases), 'graph cases')


if __name__ == '__main__':
    main()
