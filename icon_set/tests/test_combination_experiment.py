import json
import math
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
                if item.get('sizing_mode') in ('typeface-native','side-32x48','side-one-axis32','side-source-fit','container-content-resize'):
                    canvas=max(64,math.ceil(max(item['canvas_width'],item['canvas_height'])+4-1e-8))
                    result=placement(item,32,(1,1),(0,0),size_lock='auto',canvas=canvas)
                    self.assertAlmostEqual(result['painted_box']['w'],item['bounds'][2]-item['bounds'][0]+4)
                    self.assertAlmostEqual(result['painted_box']['h'],item['bounds'][3]-item['bounds'][1]+4)
                    self.assertIsNone(result['locked_size'])
                    continue
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
                        canvas=max(64,math.ceil(max(item['canvas_width'],item['canvas_height'])+4-1e-8)) if item.get('sizing_mode') in ('typeface-native','side-32x48','side-one-axis32','side-source-fit','container-content-resize') else 64
                        box=placement(item,size,anchor,(0,0),canvas=canvas)['painted_box']
                        for k,e,a in [('x','w',anchor[0]),('y','h',anchor[1])]:
                            self.assertAlmostEqual(box[k]+box[e]*a,2+(canvas-4)*a)

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

MONITOR = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="4" '
           'stroke-linecap="round" stroke-linejoin="round"><title>monitor-upload</title>'
           '<path id="screen" d="M9 6L39 6A3 3 0 0 1 42 9L42 31A3 3 0 0 1 39 34L24 34L9 34A3 3 0 0 1 6 31L6 9A3 3 0 0 1 9 6Z"/>'
           '<path id="stand" d="M24 34L24 42"/><path id="foot" d="M16 42L24 42L32 42"/>'
           '<path id="arrowhead" d="M18 21L24 15L30 21"/><path id="shaft" d="M24 15L24 25"/></svg>')
CLOUD = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="4" '
         'stroke-linecap="round" stroke-linejoin="round"><path id="cloud" d="M8 14A8 8 0 0 1 24 14C28 14 30 16 30 20'
         'C30 24 28 26 24 26L8 26C4 26 2 24 2 20C2 16 4 14 8 14Z"/></svg>')
LAYOUT_ROW = {'id': 'layout-test', 'concept': 'monitor upload cloud', 'position': 'tr',
              'mains': [{'icon': 'monitor-upload', 'document': MONITOR, 'bounds': [6, 6, 42, 42], 'canvas': 48, 'sha256': 'm1'}],
              'subs': [{'icon': 'cloud', 'document': CLOUD, 'bounds': [2, 6, 30, 26], 'canvas': 32, 'sha256': 's1'}]}


class CombinationLayoutTests(unittest.TestCase):
    def default(self):
        return render({'id': 'layout-test', 'elements': True}, row=LAYOUT_ROW)

    @staticmethod
    def snapped(result):
        return {role: [{'paths': g['paths'], 'x': round(g['box'][0]), 'y': round(g['box'][1]),
                        'size': round(max(g['box'][2]-g['box'][0], g['box'][3]-g['box'][1]))} for g in c['groups']]
                for role, c in result['elements'].items()}

    def test_connected_elements(self):
        elements = self.default()['elements']
        self.assertEqual([g['paths'] for g in elements['main']['groups']], [[0, 1, 2], [3, 4]])
        self.assertEqual([g['paths'] for g in elements['sub']['groups']], [[0]])
        self.assertEqual(len(elements['main']['markup']), 5)

    def test_identity_layout_keeps_the_combination(self):
        import re
        base = self.default()
        adjusted = render({'id': 'layout-test', 'layout': self.snapped(base)}, row=LAYOUT_ROW)
        self.assertEqual([p['painted_box'] for p in base['placements']], [p['painted_box'] for p in adjusted['placements']])
        main = lambda svg: set(re.findall(r'M[\d.,]+L[\d.,]+', svg.split('id="state-icon"')[0]))
        self.assertEqual(main(base['svg']), main(adjusted['svg']))
        self.assertNotIn('elements', adjusted)

    def test_resized_element_snaps_and_keeps_stroke(self):
        layout = self.snapped(self.default())
        layout['main'][1] = {'paths': [3, 4], 'x': 14, 'y': 29, 'size': 8}
        layout['sub'][0]['x'] += 2
        result = render({'id': 'layout-test', 'layout': layout, 'elements': True}, row=LAYOUT_ROW)
        arrow = result['elements']['main']['groups'][1]['box']
        self.assertAlmostEqual(arrow[0], 14)
        self.assertAlmostEqual(arrow[1], 29)
        self.assertAlmostEqual(max(arrow[2]-arrow[0], arrow[3]-arrow[1]), 8)
        sub = result['placements'][1]['painted_box']
        self.assertEqual((sub['x'], sub['w']), (32, 32))
        root = ET.fromstring(result['svg'])
        for group in root:
            if group.get('stroke-width'):
                self.assertAlmostEqual(float(group.get('stroke-width')), 4)

    def test_rejects_invalid_layouts(self):
        good = self.snapped(self.default())
        cases = [{'main': [dict(good['main'][0], x=2.5), good['main'][1]]},
                 {'main': [good['main'][0]]},
                 {'main': [good['main'][0], good['main'][0]]},
                 {'main': [{'paths': [0, 1, 2, 3, 4], 'x': 40, 'y': 22, 'size': 36}]},
                 {'other': []}]
        for layout in cases:
            with self.subTest(layout=layout), self.assertRaises(ValueError):
                render({'id': 'layout-test', 'layout': layout}, row=LAYOUT_ROW)

    def test_stale_layout_is_ignored(self):
        from icon_set.scripts.combination_layouts import active
        entry = {'main': {'icon': 'monitor-upload', 'sha256': 'm1'}, 'sub': {'icon': 'cloud', 'sha256': 's1'}, 'layout': {'sub': []}}
        self.assertEqual(active(LAYOUT_ROW, entry)['sub'], 'cloud')
        self.assertIsNone(active(LAYOUT_ROW, {**entry, 'sub': {'icon': 'cloud', 'sha256': 'changed'}}))
        self.assertIsNone(active(LAYOUT_ROW, None))

if __name__=='__main__':unittest.main()
