"""Bento Box and Chopsticks."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca68ad0e-a236-469d-8502-80a8b60cbc6c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/japanese launchbox bento chopstick_ca68ad0e-a236-469d-8502-80a8b60cbc6c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'oval-bento-and-chopsticks'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('bento', 'lunchbox', 'chopsticks', 'rice', 'meal', 'japanese', 'food')

    def build(self):
        # Plan: Oval bento with upper paired compartments and larger lower space beside chopsticks. Small food mound omitted. Symmetric capsule and common chopstick spacing. Bounds (6,6)-(42,42).
        self.add_arc('tl',(6,16),(16,6),radius_x=10)
        self.add_arc('tr',(16,6),(26,16),radius_x=10)
        self.add_line('r1',(26,16),(26,24));self.add_line('r2',(26,24),(26,32))
        self.add_arc('base',(26,32),(6,32),radius_x=10)
        self.add_line('l1',(6,32),(6,24));self.add_line('l2',(6,24),(6,16))
        self.add_contour('box','tl','tr','r1','r2','base','l1','l2',closed=True)
        self.add_polyline('crossbar',(6,24),(16,24),(26,24));self.relate('connect','crossbar','box')
        self.add_line('divider',(16,6),(16,24));self.relate('connect','divider','box');self.relate('connect','divider','crossbar')
        for i,x in enumerate((34,42)):self.add_line(f'chopstick-{i}',(x,6),(x,42))
