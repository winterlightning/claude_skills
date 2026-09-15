"""Three five-point stars burst above a straight central trail and mirrored curved side trails.

Construction references: Lucide shirt and star as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '681b3046-14a4-4a88-9ab2-2d02df009170'
SOURCE_PATH = 'pictographic-primitives/romance/wedding fireworks_681b3046-14a4-4a88-9ab2-2d02df009170.svg'
AUTHOR = 'gpt-6'


class StarFireworks(Solo48):
    icon_id = 'star-fireworks'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('fireworks', 'star', 'burst', 'celebration', 'wedding', 'festival')

    def build(self) -> None:
        def star(n,cx,top):
            self.add_polyline(n,(cx,top),(cx+2,top+4),(cx+6,top+4),(cx+3,top+8),(cx+4,top+12),(cx,top+10),(cx-4,top+12),(cx-3,top+8),(cx-6,top+4),(cx-2,top+4),closed=True)
        axis=24
        star('upper-star',axis,8)
        star('left-star',axis-14,24)
        star('right-star',axis+14,24)
        self.add_line('central-trail',(24,18),(24,40))
        self.relate('connect','upper-star','central-trail')
        self.add_arc('left-trail',(10,34),(14,40),radius_x=20,sweep=True)
        self.add_arc('right-trail',(38,34),(34,40),radius_x=20,sweep=False)
        self.relate('connect','left-star','left-trail')
        self.relate('connect','right-star','right-trail')
