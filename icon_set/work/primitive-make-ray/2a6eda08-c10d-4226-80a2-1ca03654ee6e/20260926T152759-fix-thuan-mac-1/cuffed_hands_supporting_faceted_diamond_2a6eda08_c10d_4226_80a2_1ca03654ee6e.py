"""An open palm-up hand offering a faceted diamond that rests on its thumb.

SOLO48 HRECT_L: visible (2, 6)-(46, 42), centerline (4, 8)-(44, 40).

Symbol plan: the hand is the library's palm-up hand (Lucide `hand-heart`
construction): the palm's upper curve rising from the wrist and running flat into the thumb,
whose rounded tip curls back under, and the fingers reaching right to a
rounded fingertip arc and back along the palm base. The diamond is mirrored
about x=24: table, girdle corners and culet, with a girdle line; the culet is
a node of the thumb's top edge, so the gem sits on the hand.
Revision: the rejected drawing boxed two upright hands in cuffs with stubby
U thumbs and read as letters; a single unmistakable offering hand replaces
them (feedback: "hand").
Construction reference: Lucide `hand-heart` (via `hand-holding-heart`) and
`gem` (table, girdle, culet outline).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2a6eda08-c10d-4226-80a2-1ca03654ee6e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cuffed-hands-supporting-faceted-diamond/20260926T152509Z-thuan-mac-1/reference/diamond give_2a6eda08-c10d-4226-80a2-1ca03654ee6e.svg'
AUTHOR = "claude-opus-5-5"

AXIS = 24
TABLE_L, GIRDLE_L, CULET = (19, 8), (15, 16), (24, 24)


def mx(p):
    return (2 * AXIS - p[0], p[1])


class Drawing(Solo48):
    icon_id = 'cuffed-hands-supporting-faceted-diamond'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('diamond give', 'hand holding diamond')
    keywords = ('diamond', 'gem', 'hand', 'give', 'offer', 'value', 'jewel', 'support')

    def build(self):
        self.add_line('table', TABLE_L, mx(TABLE_L))
        self.add_line('crown-right', mx(TABLE_L), mx(GIRDLE_L))
        self.add_line('pavilion-right', mx(GIRDLE_L), CULET)
        self.add_line('pavilion-left', CULET, GIRDLE_L)
        self.add_line('crown-left', GIRDLE_L, TABLE_L)
        self.add_contour('diamond', 'table', 'crown-right', 'pavilion-right', 'pavilion-left', 'crown-left', closed=True)
        self.add_line('girdle', GIRDLE_L, mx(GIRDLE_L))
        for m in ('crown-left', 'pavilion-left', 'crown-right', 'pavilion-right'):
            self.relate('connect', 'girdle', m)
        # palm-up hand
        self.add_arc('palm-upper', (4, 28), (14, 24), radius_x=10, radius_y=4)
        self.add_line('palm-top', (14, 24), (20, 24))
        self.add_line('thumb-top-l', (20, 24), CULET)
        self.add_line('thumb-top-r', CULET, (28, 24))
        self.add_arc('thumb-tip-upper', (28, 24), (32, 28), radius_x=4)
        self.add_arc('thumb-tip-lower', (32, 28), (28, 32), radius_x=4)
        self.add_line('thumb-bottom', (28, 32), (18, 32))
        self.add_contour('thumb', 'palm-upper', 'palm-top', 'thumb-top-l', 'thumb-top-r', 'thumb-tip-upper', 'thumb-tip-lower', 'thumb-bottom')
        self.relate('connect', 'diamond', 'thumb')
        self.add_line('fingers-upper', (32, 28), (38, 28))
        self.add_arc('fingertips', (38, 28), (44, 32), radius_x=6)
        self.add_line('fingers-lower', (44, 32), (34, 40))
        self.add_line('palm-base', (34, 40), (12, 40))
        self.add_line('wrist-lower', (12, 40), (4, 38))
        self.add_contour('hand', 'fingers-upper', 'fingertips', 'fingers-lower', 'palm-base', 'wrist-lower')
        self.relate('connect', 'thumb', 'hand')
