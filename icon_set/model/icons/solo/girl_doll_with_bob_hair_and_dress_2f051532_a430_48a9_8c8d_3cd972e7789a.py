"""Girl doll: bob-shaped blank head, dress, arms and legs.
VRECT_L reaches x8/40 y4/44. Mirror limbs about x24; head bottom16 and
dress apex24 give exact 4 ink gap. Human full_body_ref supplies dress/limbs;
Lucide baby supplies a single coherent head outline; omit facial/fringe detail.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2f051532-a430-48a9-8c8d-3cd972e7789a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_15/doll_2f051532-a430-48a9-8c8d-3cd972e7789a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'girl-doll-with-bob-hair-and-dress'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ['Girl Doll with Bob Hair and Dress']
    keywords = ['doll', 'girl', 'toy', 'hair', 'dress', 'child', 'figure']
    def build(self):
        self.add_arc('hair-top',(18,10),(30,10),radius_x=6,sweep=True)
        self.add_arc('face',(30,10),(18,10),radius_x=6,sweep=True)
        self.add_contour('head','hair-top','face',closed=True)
        self.add_polyline('dress',(24,24),(36,36),(28,36),(20,36),(12,36),(24,24),closed=True)
        for side in (-1,1):
            self.add_line(f'arm{side}',(24,24),(24+side*16,24))
            self.relate('connect','dress',f'arm{side}')
            self.add_line(f'leg{side}',(24+side*4,36),(24+side*4,44))
            self.relate('connect','dress',f'leg{side}')
        self.mark_human_figure('doll',head='head',torso='dress-1',torso_junction='start')
