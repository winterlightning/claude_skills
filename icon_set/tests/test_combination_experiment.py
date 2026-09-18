import json
import unittest
import xml.etree.ElementTree as ET
from icon_set.scripts.refresh_combination_pairs import export_sub32
from icon_set.scripts.combination_experiment import DATA, POSITIONS, number, placement, render, custom_item

class CombinationExperimentTests(unittest.TestCase):
    def test_sub_export_normalizes_visible_ink(self):
        source = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" stroke-width="4"><path d="M4 4L44 44"/></svg>'
        output = ET.fromstring(export_sub32(source))
        self.assertEqual(output.get('width'), '32')
        self.assertEqual(output.get('viewBox'), '0 0 32 32')
        self.assertEqual(output.get('stroke-width'), '4')
        from svgpathtools import parse_path
        for actual,expected in zip(parse_path(next(iter(output)).get('d')).bbox(), (2,30,2,30)):
            self.assertAlmostEqual(actual,expected)

    def test_sub_lock_rounds_visible_extent_and_preserves_proportions(self):
        item={'bounds':[8,4,40,44],'canvas':48}
        auto=placement(item,32,(1,1),(0,0),size_lock='auto')
        self.assertEqual(auto['locked_axis'],'height')
        self.assertAlmostEqual(auto['painted_box']['h'],32)
        self.assertAlmostEqual((auto['painted_box']['w']-4)/(auto['painted_box']['h']-4),32/40)
        explicit=placement(item,32,(0,0),(0,0),size_lock='width',bound_size=24)
        self.assertAlmostEqual(explicit['painted_box']['w'],24)
        self.assertAlmostEqual(explicit['painted_box']['h'],29)
        for size in (24.5,4,33):
            with self.assertRaises(ValueError):placement(item,32,(0,0),(0,0),size_lock='width',bound_size=size)
        with self.assertRaises(ValueError):placement(item,32,(0,0),(0,0),size_lock='width',bound_size=32)
        with self.assertRaises(ValueError):placement(item,32,(0,0),(0,0),size_lock='invalid')

    def test_automatic_sub_bounds_fit_all_available_pairs(self):
        for row in json.loads(DATA.read_text())['rows']:
            for item in row['subs']:
                result=placement(item,32,(1,1),(0,0),size_lock='auto')
                box=result['painted_box']
                if item['family'] != 'sub':
                    self.assertAlmostEqual(result['locked_size'],round(result['locked_size']))
                self.assertLessEqual(max(box['w'],box['h']),32.000001)
                if result.get('target_keyshape'):
                    self.assertAlmostEqual(box['x']+box['w']/2,46)
                    self.assertAlmostEqual(box['y']+box['h']/2,46)
                    l,t,r,b=item['target_keyshape_bounds']
                    self.assertLessEqual(box['w'],r-l+1e-6)
                    self.assertLessEqual(box['h'],b-t+1e-6)
                else:
                    self.assertAlmostEqual(box['x']+box['w'],62)
                    self.assertAlmostEqual(box['y']+box['h'],62)

    def test_every_pair_every_anchor(self):
        for row in json.loads(DATA.read_text())['rows']:
            for ax,ay in POSITIONS.values():
                for role,size,anchor in [('mains',48,(1-ax,1-ay)),('subs',32,(ax,ay))]:
                    for item in row[role]:
                        box=placement(item,size,anchor,(0,0))['painted_box']
                        for k,e,a in [('x','w',anchor[0]),('y','h',anchor[1])]:
                            self.assertAlmostEqual(box[k]+box[e]*a,2+60*a)

    def test_keyshape_does_not_change_origin_or_scale(self):
        for w,h in [(36,36),(40,32),(32,40),(40,40)]:
            item={'bounds':[(48-w)/2,(48-h)/2,(48+w)/2,(48+h)/2],'canvas':48}
            p=placement(item,48,(0,0),(0,0))
            self.assertEqual(p['canvas_box'],dict(x=2,y=2,w=48,h=48))
            self.assertEqual(p['painted_box'],dict(x=2,y=2,w=w+4,h=h+4))
            shifted=placement(item,48,(0,0),(2.5,3))
            self.assertEqual(shifted['painted_box'],dict(x=4.5,y=5,w=w+4,h=h+4))

    def test_zero_padding_and_invalid_padding(self):
        item={'bounds':[4,4,44,44],'canvas':48}
        self.assertEqual(placement(item,48,(0,0),(0,0),padding=0)['painted_box']['x'],0)
        row=json.loads(DATA.read_text())['rows'][0]
        for padding in [-1,9]:
            with self.assertRaises(ValueError):render({'id':row['id'],'padding':padding})

    def test_invalid_manual_uploads(self):
        for document in ['not svg','<!DOCTYPE svg><svg/>',
                         '<svg viewBox="0 0 48 32"/>',
                         '<svg viewBox="0 0 48 48"><script>alert(1)</script></svg>']:
            with self.assertRaises(ValueError):custom_item({'document':document},'main')

    def test_reject_invalid_values(self):
        for v in ['invalid','NaN','Infinity',100]:
            with self.assertRaises(ValueError):number(v)
        with self.assertRaises(ValueError):render({'id':'not-a-pair'})

if __name__=='__main__':unittest.main()
