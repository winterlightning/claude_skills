"""A sun shines above a pair of sunglasses.
Lucide glasses: paired lens geometry, connecting bridge and rising arms. Source keeps a sun above.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '81f3cdea-8b11-5ce2-be37-8b1a02812d9f'
SOURCE_PATH = 'icon_set/work/todo-references/glasses sun_81f3cdea-8b11-5ce2-be37-8b1a02812d9f.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'glasses-sun'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    categories = ('primitives', 'accessories')
    aliases = ()
    keywords = ('glasses', 'sun')
    def build(self):

        # Plan: repeated lens bowls mirrored about x=24; sun centered above them.
        # SQUARE visible extrema (4,4)-(44,44), centerlines (6,6)-(42,42).
        for side in (-1,1):
            cx=24+side*11
            self.add_line(f'lens-top-{side}',(cx-7,30),(cx+7,30))
            self.add_arc(f'lens-bowl-{side}',(cx+7,30),(cx-7,30),radius_x=7,radius_y=12)
            self.add_contour(f'lens-{side}',f'lens-top-{side}',f'lens-bowl-{side}',closed=True)
            self.add_line(f'arm-{side}',(cx+side*7,30),(cx+side*2,24))
            self.relate('connect',f'arm-{side}',f'lens-{side}')
        self.add_line('bridge',(20,30),(28,30))
        self.relate('connect','bridge','lens--1')
        self.relate('connect','bridge','lens-1')
        self.add_arc('sun-top',(20,18),(28,18),radius_x=4)
        self.add_arc('sun-bottom',(28,18),(20,18),radius_x=4)
        self.add_contour('sun','sun-top','sun-bottom',closed=True)
        self.add_dot('ray-top',(24,6))
        self.add_dot('ray-left',(12,12))
        self.add_dot('ray-right',(36,12))
