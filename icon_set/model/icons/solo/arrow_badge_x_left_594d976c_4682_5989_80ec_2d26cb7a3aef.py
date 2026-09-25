'Directional badge: shared mirrored outline, smoothly rounded tip and balanced internal mark. Lucide tag and chevron construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '594d976c-4682-5989-80ec-2d26cb7a3aef'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow badge x left_594d976c-4682-5989-80ec-2d26cb7a3aef.svg'
AUTHOR = 'gpt-6'

class ArrowBadgeXLeft(Solo48):
    icon_id = 'arrow-badge-x-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'badge', 'x', 'left', 'arrows')

    def build(self) -> None:
        # One rounded tag outline, mirrored/rotated on the same SOLO48 grid.
        # Shoulder/tip controls follow the adjoining slope exactly for smooth joins.
        # HRECT_L ink (2,6)-(46,42), or VRECT_L ink (6,2)-(42,46).
        def point(x,y): return (48-x,y)
        self.add_line('top',point(8,8),point(30,8))
        self.add_bezier('upper-shoulder',point(30,8),(point(32,8),point(33,12-18/7),point(35,12)))
        self.add_line('upper-slope',point(35,12),point(42,21))
        self.add_bezier('tip-upper',point(42,21),(point(42+7/9,22),point(44,23),point(44,24)))
        self.add_bezier('tip-lower',point(44,24),(point(44,25),point(42+7/9,26),point(42,27)))
        self.add_line('lower-slope',point(42,27),point(35,36))
        self.add_bezier('lower-shoulder',point(35,36),(point(33,36+18/7),point(32,40),point(30,40)))
        self.add_line('bottom',point(30,40),point(8,40))
        self.add_bezier('lower-corner',point(8,40),(point(6,40),point(4,38),point(4,36)))
        self.add_line('back',point(4,36),point(4,12))
        self.add_bezier('upper-corner',point(4,12),(point(4,10),point(6,8),point(8,8)))
        self.add_contour('outline','top','upper-shoulder','upper-slope','tip-upper','tip-lower','lower-slope','lower-shoulder','bottom','lower-corner','back','upper-corner',closed=True)
        self.add_polyline('cross-a',point(14,18),point(20,24),point(26,30))
        self.add_polyline('cross-b',point(14,30),point(20,24),point(26,18))
        self.relate('connect','cross-a','cross-b')
