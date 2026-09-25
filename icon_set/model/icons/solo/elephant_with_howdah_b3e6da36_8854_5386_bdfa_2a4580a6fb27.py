"""Elephant with Howdah.

Plan: Left-facing elephant with descending trunk, a reduced curved ear fold, stout legs and roofed howdah. Remove eye, tusk, left roof overhang and interior saddle lines. Bounds (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3e6da36-8854-5386-bdfa-2a4580a6fb27'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/mysore dasara_b3e6da36-8854-5386-bdfa-2a4580a6fb27.svg'
AUTHOR = 'gpt-6'

class ElephantWithHowdah(Solo48):
    icon_id = 'elephant-with-howdah'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('elephant', 'with', 'howdah')

    def build(self):
        self.add_polyline('trunk',(4,40),(4,32),(4,24))
        self.add_arc('head-top',(4,24),(12,16),radius_x=8)
        self.add_polyline('back',(12,16),(20,16),(24,20),(40,20))
        self.add_arc('rump',(40,20),(44,24),radius_x=4)
        self.add_polyline('legs',(44,24),(44,40),(36,40),(36,32),(28,32),(28,40),(20,40),(20,32),(12,32),(12,40),(4,40))
        self.add_contour('elephant','trunk-1','trunk-2','head-top','back-1','back-2','back-3','rump',*[f'legs-{i}' for i in range(1,11)],closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ['trunk','back','legs']]
        self.add_arc('ear',(16,24),(12,32),radius_x=4,radius_y=8)
        self.relate('connect','elephant','ear')
        self.add_line('post-left',(24,20),(24,12));self.add_line('post-right',(40,20),(40,12))
        self.add_polyline('roof',(24,12),(32,8),(40,12),(44,12))
        for n in ['post-left','post-right']:
         self.relate('connect','elephant',n);self.relate('connect','roof',n)
