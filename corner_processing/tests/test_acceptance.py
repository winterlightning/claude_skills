"""Acceptance fixtures for the round and sharp outputs (PR #4 review): designed curves, broad arcs, inner corners
and the keyshape are kept as the README's rules say, and every output's check is ok.

    cd corner_processing && PYTHONPATH=.. python3 -m pytest tests -q
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
HEAD = ('<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" fill="none" stroke="currentColor" '
        'stroke-width="4" stroke-linecap="round" stroke-linejoin="round">')
ICONS = {
    # a designed curve (r 12 > 8): both outputs keep it
    'designed-round-square.svg': '<rect x="8" y="8" width="32" height="32" rx="12"/>',
    # a broad arc and the line closing it: the arc survives both outputs
    'broad-arc.svg': '<path d="M8 32A16 16 0 0 1 40 32"/><path d="M8 32H40"/>',
    # two L strokes, one inside the other: 90° corners, round r 4 / sharp points
    'inner-corner.svg': '<path d="M10 8V38H38"/><path d="M18 8V30H38"/>',
    # a square keyshape frame with a small fillet and a dot: the frame keeps the keyshape box
    'square-frame-dot.svg': '<rect x="6" y="6" width="36" height="36" rx="2"/><circle cx="24" cy="24" r="2" fill="currentColor" stroke="none"/>',
}


@pytest.fixture(scope='module')
def outputs(tmp_path_factory):
    base = tmp_path_factory.mktemp('corners')
    os.makedirs(base / 'in')
    for name, body in ICONS.items():
        (base / 'in' / name).write_text(HEAD + body + '</svg>\n', encoding='utf-8')
    env = {**os.environ, 'PYTHONPATH': os.path.dirname(ROOT)}
    for mode in ('round', 'sharp'):
        subprocess.run([sys.executable, f'{mode}_corner_processing.py', '--input', str(base / 'in'), '--out', str(base / 'out'),
                        '--no-report', '--jobs', '1'], cwd=ROOT, env=env, check=True, capture_output=True)
    toggles = json.loads((base / 'out' / 'toggle.json').read_text())['icons']
    svg = lambda mode, name: (base / 'out' / mode / name).read_text()
    return svg, toggles


def numbers(text):
    return [float(v) for v in re.findall(r'-?\d+(?:\.\d+)?', text)]


def paths(text):
    return re.findall(r'<path d="([^"]+)"', text)


@pytest.mark.parametrize('mode', ['round', 'sharp'])
def test_every_check_is_ok(outputs, mode):
    _, toggles = outputs
    assert {name: toggles[name][mode]['check']['status'] for name in ICONS} == {name: 'ok' for name in ICONS}


@pytest.mark.parametrize('mode', ['round', 'sharp'])
def test_designed_curve_is_kept(outputs, mode):
    svg, toggles = outputs
    assert svg(mode, 'designed-round-square.svg').count('A12 12') == 4
    log = toggles['designed-round-square.svg'][mode]['log']
    assert [e['status'] for e in log] == ['kept round'] * 4


@pytest.mark.parametrize('mode', ['round', 'sharp'])
def test_broad_arc_is_kept(outputs, mode):
    svg, _ = outputs
    assert 'A16 16' in svg(mode, 'broad-arc.svg')


def test_inner_corner_round_by_angle(outputs):
    svg, toggles = outputs
    d = paths(svg('round', 'inner-corner.svg'))
    assert len(d) == 2 and all('A4 4' in p for p in d), d          # 90° corners: r 4, inner stroke included
    assert [e['status'] for e in toggles['inner-corner.svg']['round']['log']] == ['rounded', 'rounded']


def test_inner_corner_sharp_points(outputs):
    svg, _ = outputs
    d = paths(svg('sharp', 'inner-corner.svg'))
    assert d == ['M10 6L10 38L40 38', 'M18 6L18 30L40 30'], d     # sharp points, flat ends lengthened 2 u


@pytest.mark.parametrize('mode', ['round', 'sharp'])
def test_keyshape_box_is_kept(outputs, mode):
    svg, _ = outputs
    text = svg(mode, 'square-frame-dot.svg')
    frame = [p for p in paths(text) if 'Z' in p]
    assert len(frame) == 1
    values = numbers(frame[0].replace('A4 4 0 0 1', ''))
    assert min(values) == 6 and max(values) == 42, frame               # the square keyshape's 6..42 box, no ink past it


def test_dot_is_round_in_round_and_square_in_sharp(outputs):
    svg, _ = outputs
    assert '<circle cx="24" cy="24" r="2"' in svg('round', 'square-frame-dot.svg')
    assert 'x="22" y="22" width="4" height="4"' in svg('sharp', 'square-frame-dot.svg')
