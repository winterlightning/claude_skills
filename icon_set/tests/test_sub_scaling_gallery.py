import unittest
import xml.etree.ElementTree as ET
from icon_set.scripts.sub_scaling_gallery import scaling_metrics, scaled_document
from icon_set.scripts.combination_experiment import placement


class ScalingInspectionTests(unittest.TestCase):
    def test_inspection_matches_actual_combination_sizing(self):
        item = {'bounds': [4, 8, 44, 40], 'canvas': 48}
        m = scaling_metrics(item)
        actual = placement(item, 32, (1, 1), (0, 0), size_lock='auto')['painted_box']
        self.assertAlmostEqual(m['ink_width'], actual['w'])
        self.assertAlmostEqual(m['ink_height'], actual['h'])
        self.assertAlmostEqual(m['scale'], .625)
        self.assertAlmostEqual(m['ink_width'], 29)
        self.assertAlmostEqual(m['ink_height'], 24)
        self.assertLessEqual(max(m['ink_width'], m['ink_height']), 32)

    def test_scaled_preview_preserves_path_and_final_stroke(self):
        source = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" stroke-width="4"><path stroke-width="4" d="M4 8L44 40"/></svg>'
        m = scaling_metrics({'bounds': [4, 8, 44, 40], 'canvas': 48})
        result = ET.fromstring(scaled_document(source, m))
        path = next(e for e in result.iter() if e.tag.endswith('path'))
        self.assertEqual(path.get('d'), 'M4 8L44 40')
        self.assertEqual(result.get('viewBox'), '0 0 32 32')
        self.assertAlmostEqual(float(path.get('stroke-width')) * m['scale'], 4)
        self.assertAlmostEqual(float(result.get('stroke-width')) * m['scale'], 4)

class KeyshapeInspectionTests(unittest.TestCase):
    def test_six_guides_follow_existing_profile_contract(self):
        from icon_set.scripts.sub_scaling_gallery import inspection_keyshapes
        shapes = inspection_keyshapes()
        self.assertEqual([s['name'] for s in shapes], ['CIRCLE','SQUARE','HRECT_L','HRECT_M','VRECT_L','VRECT_M'])
        self.assertEqual(shapes[2]['sub_bounds'], (0,4,32,28))
        self.assertEqual(shapes[2]['solo_bounds'], (2,6,46,42))

    def test_fit_distinguishes_envelope_match_from_containment(self):
        from icon_set.scripts.sub_scaling_gallery import inspection_keyshapes, keyshape_fit
        shapes = {s['name']:s for s in inspection_keyshapes()}
        metrics = dict(ink_width=32,ink_height=24)
        self.assertEqual(keyshape_fit(metrics,shapes['HRECT_L'],18),'matches')
        self.assertEqual(keyshape_fit(metrics,shapes['SQUARE'],18),'inside')
        self.assertEqual(keyshape_fit(metrics,shapes['HRECT_M'],18),'exceeds')
        self.assertEqual(keyshape_fit(metrics,shapes['CIRCLE'],18),'exceeds')
        self.assertEqual(keyshape_fit(metrics,shapes['CIRCLE'],16),'matches')

class RoundedProportionTests(unittest.TestCase):
    def test_ignores_keyshape_and_preserves_exact_ratio(self):
        item = dict(bounds=[4,8,44,40],canvas=48,family='solo',
                    target_keyshape='VRECT_M',target_keyshape_bounds=[6,0,26,32])
        result=scaling_metrics(item)
        self.assertEqual((result['ink_width'],result['ink_height']),(29,24))
        self.assertEqual(result['proportion_change'],0)

    def test_irrational_ratio_rounds_shorter_dimension(self):
        result=scaling_metrics(dict(bounds=[0,0,37.123,28.654],canvas=48,family='solo'))
        self.assertEqual((result['ink_width'],result['ink_height']),(32,26))
        self.assertLess(result['proportion_change'],2)

    def test_all_solo_options_have_whole_number_dimensions(self):
        import json
        from icon_set.scripts.combination_experiment import DATA
        for row in json.loads(DATA.read_text())['rows']:
            for item in row['subs']:
                if item['family']!='solo':continue
                result=scaling_metrics(item)
                for axis in ('ink_width','ink_height'):
                    self.assertAlmostEqual(result[axis],round(result[axis]))
                    self.assertLessEqual(result[axis],32)
                self.assertLess(result['proportion_change'],3)

class RoundedEnginePlacementTests(unittest.TestCase):
    def test_explicit_rounded_box_is_used_without_resnapping(self):
        import sys
        from pathlib import Path
        vendor=Path(__file__).resolve().parents[1]/'vendor/combination'
        sys.path.insert(0,str(vendor))
        from box_combine import fit_into, bbox
        segments=[[(0,0),(32,40)]]
        exact=fit_into(segments,(3,5,22,28),exact_box=True)
        self.assertEqual(bbox(exact),(3,5,25,33))
        ordinary=fit_into(segments,(3,5,22,28))
        bounds=bbox(ordinary)
        self.assertAlmostEqual((bounds[2]-bounds[0])/(bounds[3]-bounds[1]),.8)
