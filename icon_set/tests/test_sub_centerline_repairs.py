"""Smooth joins must be checked on centerlines, not inferred from rounded paint."""
import math
import unittest
from svgpathtools import parse_path
from icon_set.model.icons.registry import create
from icon_set.renderers.svg import build_paths

# Deliberate corners are excluded explicitly; each listed junction should be smooth.
SMOOTH = {
    'baby-head-sub32-v2': {'path-1-1': None},
    'container-content-text-f824dc04-sub32-v2': {'path-3-1': None},
    'human-ear-4681f30b-sub32-v2': {'path-1-1': None, 'path-2-1': None},
    'ice-skate-boot-sub32-v2': {'path-1-1': {2, 3}},
    'icon-0-text-in-circle-sub32-v2': {'path-2-1': None},
    'quill-sub32-v2': {'feather': {2, 3}},
    'shinto-torii-gate-sub32-v2': {'path-3-1': None, 'path-4-1': None},
    'six-lobed-cog-66a27160-f0ef-48c6-8ce3-c2ea9255ad5b-sub32-v2': {'cog': None},
    'lines-sub32-v3': {'connector': None},
    'hidden-sub32-v3': {'eye': {1,2,3,5,6,7}},
    'ice-cream-cone-sub32-v3': {'scoop': None},
    'cloud-sub32-v2': {'path-1-1': None},
    'dna-sub32-v2': {'path-1-1': None, 'path-2-1': None},
    'folder-sub32-v2': {'path-1-1': {3,4,5,6,7,8,9,10}},
    'forward-arrow-sub32-v2': {'path-2-1': None},
    'glue-sub32-v2': {'path-1-1': None, 'path-2-1': None},
    'hairpin-turn-right-sub32-v2': {'shaft': None},
    'lines-sub32-v2': {'path-1-1': None},
    'previous-arrow-sub32-v2': {'path-3-1': None},
    'quotation-marks-sub32-v2': {'path-2-1': None, 'path-4-1': None},
    'arrow-bottom-symbol-sub32-v3': {'path-1-1': None, 'path-2-1': None},
    'arrow-right-curved-sub32-v3': {'path-2-1': None},
    'bean-sub32-v3': {'path-1-1': None},
    'bell-sub32-v3': {'path-1-1': None},
    'bench-sub32-v3': {'path-3-1': None, 'path-4-1': None},
    'camera-video-sub32-v3': {'path-1-1': None},
    'cart-e3de8236-sub32-v3': {'path-1-1': {4, 5, 6, 7}},
}


class SubCenterlineRepairs(unittest.TestCase):
    def test_intended_smooth_junctions_have_matching_forward_tangents(self):
        for uid, targets in SMOOTH.items():
            paths = build_paths(create(uid).draw())
            self.assertTrue(set(targets).issubset({p["id"] for p in paths}), uid)
            for path in paths:
                if path['id'] not in targets:
                    continue
                segments = list(parse_path(path['d']))
                pairs = list(zip(segments, segments[1:]))
                if segments[-1].end == segments[0].start:
                    pairs.append((segments[-1], segments[0]))
                for index, (a, b) in enumerate(pairs, 1):
                    if targets[path['id']] is not None and index not in targets[path['id']]:
                        continue
                    with self.subTest(icon=uid, path=path['id'], join=index):
                        u, v = a.derivative(1-1e-8), b.derivative(1e-8)
                        self.assertGreater(abs(u)*abs(v), 0)
                        cross = abs(u.real*v.imag-u.imag*v.real)/(abs(u)*abs(v))
                        self.assertLess(cross, 1e-6)
                        self.assertGreater(u.real*v.real+u.imag*v.imag, 0)
