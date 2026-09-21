"""Body detection must follow semantic glyph geometry, not the 48px canvas."""
import tempfile
import unittest
from pathlib import Path
from icon_set.model.icons.registry import create
from icon_set.model.typeface import measure_glyph
from icon_set.scripts.typeface_gallery import stage_typeface


class TypefaceTests(unittest.TestCase):
    def test_bowls_exclude_ascenders_and_descenders(self):
        expected={'o':(6,42),'b':(16,44),'d':(16,44),'p':(4,32),'q':(4,32),'g':(4,32)}
        for char, band in expected.items():
            with self.subTest(char=char):
                m=measure_glyph(create('letter-'+char))
                self.assertEqual((m['body_top'],m['baseline']),band)
                self.assertEqual(m['measurement'],'closed-body-contour')

    def test_dots_do_not_change_body_height(self):
        m=measure_glyph(create('letter-i'))
        self.assertEqual((m['body_top'],m['baseline']),(18,44))
        self.assertEqual(m['bounds'][1],4)

    def test_authored_bands_distinguish_hook_from_body(self):
        m=measure_glyph(create('letter-j'))
        self.assertEqual((m['body_top'],m['baseline']),(18,36))
        self.assertEqual(m['bounds'][3],44)
        self.assertEqual(m['measurement'],'authored-body-band')

    def test_both_o_sizes_normalize_to_same_body(self):
        small=measure_glyph(create('letter-o'))
        large=measure_glyph(create('letter-o-large'))
        self.assertEqual(small['body_height'],36)
        self.assertEqual(large['body_height'],40)
        self.assertFalse(large['preferred'])

    def test_composer_uses_independent_lettering_not_legacy_icon_exports(self):
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)
            stage_typeface(path,[{'icon_id':'letter-b','svg_sha256':'stale'}],{})
            import json
            data=json.loads((path/'typeface.json').read_text())
            self.assertEqual(data['geometry_policy'],'fixed-centerline-6x20')
            self.assertEqual(len(data['glyphs']),107)
            r=next(g for g in data['glyphs'] if g['character']=='r')
            self.assertAlmostEqual(r['bounds'][2]-r['bounds'][0],6)
            self.assertAlmostEqual(r['bounds'][3]-r['bounds'][1],20)
            self.assertNotIn('__TYPEFACE_', (path/'text-combine.html').read_text())

    def test_invalid_band_is_rejected(self):
        icon=create('letter-b')
        icon.typeface={'character':'b','body_band':(44,16)}
        with self.assertRaisesRegex(ValueError,'invalid body band'):
            measure_glyph(icon)

    def test_capitals_measure_full_height_not_only_the_bowl(self):
        for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            with self.subTest(char=char):
                m=measure_glyph(create('letter-'+char.lower()+'-uppercase'))
                self.assertEqual(m['kind'],'uppercase')
                self.assertEqual(m['character'],char)
                if char=='Q':
                    self.assertEqual((m['body_top'],m['baseline']),(4,40))
                    self.assertEqual(m['bounds'][3],44)
                else:
                    self.assertEqual(m['body_top'],m['bounds'][1])
                    self.assertEqual(m['baseline'],m['bounds'][3])
