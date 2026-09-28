import json
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET
from icon_set.scripts.side_text import native_text, glyph_map, compose
from icon_set.scripts.side_components import build

class NativeSideTextTests(unittest.TestCase):
    def test_native_paths_and_exact_four_unit_gaps(self):
        glyphs=glyph_map()
        document,w,h,placements=native_text('A1W%\nERROR',glyphs)
        root=ET.fromstring(document)
        self.assertEqual(root.get('stroke-width'),'4')
        groups=[g for g in root if g.tag.endswith('}g')]
        for g,p in zip(groups,placements):
            self.assertEqual(p['scale'],1)
            self.assertEqual([x.get('d') for x in g],glyphs[p['character']]['paths'])
            self.assertNotIn('scale',g.get('transform'))
            l,t,r,b=p['ink_bounds']
            self.assertGreaterEqual(l,-1e-8);self.assertGreaterEqual(t,-1e-8)
            self.assertLessEqual(r,w+1e-8);self.assertLessEqual(b,h+1e-8)
        for a,b in zip(placements,placements[1:]):
            if a['line']==b['line']:self.assertAlmostEqual(b['ink_bounds'][0]-a['ink_bounds'][2],4)
        self.assertAlmostEqual(placements[0]['ink_bounds'][3]-placements[0]['ink_bounds'][1],19,places=3)
        self.assertAlmostEqual(placements[1]['ink_bounds'][3]-placements[1]['ink_bounds'][1],glyphs['1']['ink_height'],places=3)

    def test_wide_composition_expands_without_scaling(self):
        sub,w,h,_=native_text('ERROR',glyph_map())
        main='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="black" stroke-width="4"><path d="M2 2H46V46H2Z"/></svg>'
        svg,cw,ch=compose(main,sub,'br','main','sub')
        self.assertGreaterEqual(cw+1e-8,w+4)
        self.assertGreaterEqual(ch+1e-8,h+4)
        root=ET.fromstring(svg)
        subgroup=next(e for e in root if e.get('id')=='state-icon')
        self.assertIn('scale(1)',subgroup.get('transform'))
        self.assertTrue(any(e.get('id')=='main-icon-clipped' for e in root))
        self.assertFalse(any(e.tag.endswith('clipPath') for e in root.iter()))
        self.assertEqual([e.get('d') for e in subgroup.iter() if e.tag.endswith('path')],
                         [e.get('d') for e in ET.fromstring(sub).iter() if e.tag.endswith('path')])

    def test_text_is_linked_by_source_id_on_sub_page(self):
        uid='source'
        combinations={'references':{uid:{'concept':'ABC'},'main':{}},'rows':[{'kind':'side','id':'pair','concept':'ABC pair','main_id':'main','sub_id':uid}]}
        row=dict(icon_id='abc',key='text/abc',family='text',profile='TEXT_NATIVE_V2',canvas_width=44,canvas_height=19,source_ids=[uid],validation={'status':'valid'},preview_url='../text-native-v2/abc.svg')
        result=build(combinations,[row],[],root=Path('/nonexistent'))
        self.assertEqual(result['subs'][0]['status'],'done')
        self.assertEqual(result['subs'][0]['drawings'][0]['profile'],'TEXT_NATIVE_V2')
