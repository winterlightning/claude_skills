"""hidden: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f48fc2c-5ebe-4a21-b259-42ee5c3ca129'
SOURCE_PATH = 'pictographic-primitives/symbol/hidden_2f48fc2c-5ebe-4a21-b259-42ee5c3ca129.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Hidden(Solo48):
    icon_id = 'hidden'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('hidden', 'symbol')

    def build(self):
        # Plan: HRECT_L; mirror all lens quadrants; diagonal terminates on exact curve knots.
        # Reference: Geometric paired curves and shared nodes.
        mirror = False

        axis = 24
        def p(x,y):return (48-x,y) if mirror else (x,y)
        self.add_bezier('upper-left',p(4,24),(p(7,19),p(10,14),p(14,12)),(p(18,10),p(20,8),p(24,8)))
        self.add_bezier('upper-right',p(24,8),(p(28,8),p(30,10),p(34,12)),(p(38,14),p(41,19),p(44,24)))
        self.add_bezier('lower-right',p(44,24),(p(41,29),p(38,34),p(34,36)),(p(30,38),p(28,40),p(24,40)))
        self.add_bezier('lower-left',p(24,40),(p(20,40),p(18,38),p(14,36)),(p(10,34),p(7,29),p(4,24)))
        self.add_contour('outline','upper-left','upper-right','lower-right','lower-left',closed=True)
        self.add_line('slash',p(14,12),p(34,36))
        self.relate('connect','slash','outline')
