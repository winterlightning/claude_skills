"""Right-facing bear with raised ear, broad back, heavy legs and open mouth.
HRECT_L envelope (4,8)-(44,40). One asymmetric silhouette; two square feet
share baseline and width. Omit eye and far legs at native size. No Lucide bear match.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'd4ac73e1-75ba-437f-bb76-a2124650edec'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_33/saving bear market_d4ac73e1-75ba-437f-bb76-a2124650edec.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'bear-with-open-mouth'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ['Bear Market Symbol']
    keywords = ['bear', 'animal', 'mouth', 'profile', 'wildlife', 'mammal']
    def build(self):
        self.add_bezier('back',(4,28),((4,16),(14,12),(28,12)))
        self.add_arc('ear',(28,12),(36,12),radius_x=4)
        self.add_line('snout-top',(36,12),(44,12))
        self.add_bezier('snout',(44,12),((44,20),(34,16),(34,24)))
        self.add_bezier('jaw',(34,24),((34,28),(40,28),(44,24)))
        self.add_bezier('chest',(44,24),((44,32),(32,32),(32,32)))
        self.add_line('front-outer',(32,32),(32,40))
        self.add_line('front-foot',(32,40),(24,40))
        self.add_line('front-inner',(24,40),(24,30))
        self.add_line('belly',(24,30),(14,30))
        self.add_line('rear-inner',(14,30),(14,40))
        self.add_line('rear-foot',(14,40),(6,40))
        self.add_bezier('rump',(6,40),((6,34),(4,34),(4,28)))
        self.add_contour('bear','back','ear','snout-top','snout','jaw','chest','front-outer','front-foot','front-inner','belly','rear-inner','rear-foot','rump',closed=True)
