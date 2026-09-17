"""Bento Box and Chopsticks."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4983297b-a8e1-57e1-af3a-d0469ec7cc79'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/asian food japanese launchbox bento chopstick_4983297b-a8e1-57e1-af3a-d0469ec7cc79.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rectangular-bento-and-chopsticks'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('bento', 'lunchbox', 'chopsticks', 'meal', 'compartment', 'japanese', 'food')

    def build(self):
        # Plan: Three-compartment rectangular bento beside two parallel chopsticks. Food piece omitted for clearance. Rounded rectangle joins from Lucide wallet. Bounds (6,6)-(42,42).
        self.add_line('top-1',(9,6),(16,6));self.add_line('top-2',(16,6),(23,6))
        self.add_arc('tr',(23,6),(26,9),radius_x=3)
        self.add_line('r1',(26,9),(26,22));self.add_line('r2',(26,22),(26,39))
        self.add_arc('br',(26,39),(23,42),radius_x=3)
        self.add_line('bottom',(23,42),(9,42))
        self.add_arc('bl',(9,42),(6,39),radius_x=3)
        self.add_line('l1',(6,39),(6,22));self.add_line('l2',(6,22),(6,9))
        self.add_arc('tl',(6,9),(9,6),radius_x=3)
        self.add_contour('box','top-1','top-2','tr','r1','r2','br','bottom','bl','l1','l2','tl',closed=True)
        self.add_polyline('crossbar',(6,22),(16,22),(26,22));self.relate('connect','crossbar','box')
        self.add_line('divider',(16,6),(16,22));self.relate('connect','divider','box');self.relate('connect','divider','crossbar')
        for i,x in enumerate((34,42)):self.add_line(f'chopstick-{i}',(x,6),(x,42))
