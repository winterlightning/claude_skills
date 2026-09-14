"""Two people with paired circular heads, a simplified male body and a dress with open legs. Remove fringe and tiny shoulder steps. SQUARE centerline bounds (6,6)-(42,42). Lucide person-standing informed open limbs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8808cfa8-f297-4bd3-a099-3c4ba3f2b025'
SOURCE_PATH = 'pictographic-primitives/users/multiple man woman 1_8808cfa8-f297-4bd3-a099-3c4ba3f2b025.svg'
AUTHOR = 'gpt-6'

class CoupleStandingWithHairVariant2(Solo48):
    icon_id = 'couple-standing-with-hair-v2'
    variant_of = 'couple-standing-with-hair'
    variant_label = 'Roomier spacing — review 03'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/groups'
    aliases = ()
    keywords = ('couple', 'man', 'woman', 'people', 'pair', 'partners', 'figures', 'family')

    def circle(self, name, cx, cy, radius):
        top, bottom = ((cx, cy - radius), (cx, cy + radius))
        self.add_arc(name + '-a', top, bottom, radius_x=radius)
        self.add_arc(name + '-b', bottom, top, radius_x=radius)
        self.add_contour(name, name + '-a', name + '-b', closed=True)

    def build(self):
        for name, cx in (('man', 12), ('woman', 36)):
            self.circle(name + '-head', cx, 12, 6)
        for side, x in (('left', 30), ('right', 42)):
            self.add_line('hair-' + side, (x, 12), (x, 19))
            self.relate('connect', 'woman-head', 'hair-' + side)
        self.add_arc('body-cap', (6, 33), (18, 33), radius_x=6)
        self.add_line('body-base-1', (18, 33), (18, 42))
        self.add_line('body-base-2', (18, 42), (6, 42))
        self.add_line('body-base-3', (6, 42), (6, 33))
        self.add_contour('man-body', 'body-cap', 'body-base-1', 'body-base-2', 'body-base-3')
        self.add_polyline('dress', (32, 27), (40, 27), (42, 35), (40, 35), (32, 35), (30, 35), closed=True)
        for x in (32, 40):
            self.add_line('leg-' + str(x), (x, 35), (x, 42))
            self.relate('connect', 'dress', 'leg-' + str(x))
