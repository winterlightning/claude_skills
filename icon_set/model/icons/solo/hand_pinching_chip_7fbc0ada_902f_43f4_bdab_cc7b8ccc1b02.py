"""A curved hand pinches a square microchip. Two pins replace the full pin array. Lucide hand informs the continuous curved finger; the forearm stays deliberately asymmetric.
Fresh SOLO48 geometry. Keyshape SQUARE; bounds are resolved from the live contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7fbc0ada-902f-43f4-bdab-cc7b8ccc1b02'
SOURCE_PATH = 'pictographic-primitives/programing/chip hold_7fbc0ada-902f-43f4-bdab-cc7b8ccc1b02.svg'
AUTHOR = 'gpt-6'

class HandPinchingChip(Solo48):
    icon_id = 'hand-pinching-chip'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "programing"
    aliases = ()
    keywords = ('hand', 'chip', 'microchip', 'hardware', 'holding', 'technology', 'processor', 'electronics')

    def build(self) -> None:
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def oval(name, x, y, rx, ry):
            self.add_arc(name+'-top', (x-rx,y), (x+rx,y), radius_x=rx,radius_y=ry)
            self.add_arc(name+'-bottom', (x+rx,y), (x-rx,y), radius_x=rx,radius_y=ry)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        self.add_polyline('chip',(10,15),(22,15),(22,27),(10,27),closed=True)
        self.add_line('top-pin',(14,11),(14,15))
        self.add_line('left-pin',(6,18),(10,18))
        self.relate('connect','chip','top-pin')
        self.relate('connect','chip','left-pin')
        self.add_line('finger-top',(22,6),(26,6))
        self.add_arc('outer-knuckle',(26,6),(42,22),radius_x=16)
        self.add_line('outer-arm',(42,22),(42,42))
        self.add_contour('hand-outer','finger-top','outer-knuckle','outer-arm')
        self.add_line('finger-tip',(22,15),(26,15))
        self.add_arc('inner-upper',(26,15),(33,22),radius_x=7)
        self.add_arc('inner-lower',(33,22),(26,29),radius_x=7)
        self.add_line('thumb-tip',(26,29),(22,27))
        self.add_contour('grasp','finger-tip','inner-upper','inner-lower','thumb-tip')
        self.relate('connect','grasp','chip')
        self.add_polyline('thumb-arm',(10,27),(26,42))
        self.relate('connect','thumb-arm','chip')
