"""Mechanical Robotic Hand. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: inspected local Lucide hand, truck, piggy-bank, globe, zap, video and wallet originals and atomic-debug geometry for coherent outlines, shared radii and simplification.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '6444a5ca-ed45-4973-a423-c42fca7fd778'
SOURCE_PATH = 'pictographic-primitives/other/hand robot_6444a5ca-ed45-4973-a423-c42fca7fd778.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mechanical-robotic-hand-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'mechanical robotic hand')
    def build(self):
        # Open mechanical gripper: palm shell, raised digit and cuff.
        self.add_bezier('back',(4,8),((12,8),(18,12),(24,14)))
        self.add_arc('knuckle',(24,14),(28,18),radius_x=4)
        self.add_line('finger-bottom',(28,18),(28,24))
        self.add_line('digit-up',(28,24),(37,16))
        self.add_bezier('digit-tip',(37,16),((41,12),(44,15),(44,18)),((44,22),(36,31),(32,35)),((27,40),(23,40),(20,40)),((13,40),(9,35),(4,34)))
        self.add_line('wrist',(4,34),(4,8))
        self.add_contour('outline','back','knuckle','finger-bottom','digit-up','digit-tip','wrist',closed=True)
        self.add_line('cuff',(13,12),(13,37))
        self.relate('connect','outline','cuff')
