"""Shared optical forms must match their published typeface paths exactly."""
import json
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET
from icon_set.model.icons.sub._base import Sub32
from icon_set.typeface.reference_forms import draw_open_dollar, draw_small_open_dollar, draw_narrow_pound, draw_curved_hryvnia
from icon_set.typeface.sub32 import (PROFILE_VARIANTS, draw_dollar,
    draw_bitcoin, draw_registered_r, draw_hryvnia)


class Glyph(Sub32):
    icon_id = 'test-optical-glyph'

    def build(self):
        pass


class CompactTypefaceTests(unittest.TestCase):
    def test_profile_variants_match_shared_drawings(self):
        forms = {
            'symbol-dollar-open-source32': lambda m: draw_open_dollar(m,16,10),
            'symbol-dollar-open-small-source32': lambda m: draw_small_open_dollar(m,16,10),
            'symbol-pound-portrait-source32': draw_narrow_pound,
            'symbol-hryvnia-curved-source32': draw_curved_hryvnia,
            'symbol-bitcoin-compact32': draw_bitcoin,
            'letter-r-registered32': draw_registered_r,
            'symbol-hryvnia-compact32': draw_hryvnia,
            'symbol-dollar-compact32': lambda m: draw_dollar(m,10),
            'symbol-dollar-compact32-short-tick': lambda m: draw_dollar(m,10,1),
        }
        for uid, draw in forms.items():
            with self.subTest(variant=uid):
                model = Glyph()
                draw(model)
                paths = [p.get('d') for p in ET.fromstring(model.to_svg()) if p.get('d')]
                self.assertEqual(paths, PROFILE_VARIANTS[uid]['paths'])

    def test_catalog_preserves_optical_forms_separately(self):
        data = json.loads((Path(__file__).resolve().parents[1]/'typeface/glyphs.json').read_text())
        self.assertEqual(data['profile_variants'], PROFILE_VARIANTS)
        parents = {g['icon_id'] for g in data['glyphs']}
        for variant in PROFILE_VARIANTS.values():
            self.assertIn(variant['parent_glyph'], parents)
            self.assertEqual(variant['stroke_width'], 4)
