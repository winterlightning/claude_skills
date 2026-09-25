"""User Bust: A detached round head sits above broad curved shoulders enclosed by short upright sides and a straight lower edge. The head and torso have no internal details.

Construction: A round detached head sits above broad shoulders with the original closed bottom; exact 4-unit ink gap.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '43b3b89e-0139-4c66-91f6-1ac0c13d9617'
SOURCE_PATH = 'pictographic-primitives/state/person_43b3b89e-0139-4c66-91f6-1ac0c13d9617.svg'
AUTHOR = 'gpt-6'

class UserBustSubState202ContainerSymbol(Sub32):
    icon_id = 'user-bust-sub-state-202-symbol'
    related_origin_icon_id = 'user-bust-sub-state-202'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/user-bust-sub-state-202'
    counterpart_icon_id = 'user-bust-sub-state-202'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('user', 'bust', 'detached', 'round', 'head', 'sits', 'broad', 'curved')

    def build(self):

        def circle(name, cx, cy, radius):
            self.add_arc(name + '-top', (cx - radius, cy), (cx + radius, cy), radius_x=radius)
            self.add_arc(name + '-bottom', (cx + radius, cy), (cx - radius, cy), radius_x=radius)
            self.add_contour(name, name + '-top', name + '-bottom', closed=True)
        circle('head', 16, 7, 5)
        self.add_arc('shoulders', (2, 27), (30, 27), radius_x=14, radius_y=7)
        points = [(30, 27), (30, 30), (2, 30), (2, 27)]
        for i, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(f'base-{i}', a, b)
        self.add_contour('torso', 'shoulders', 'base-1', 'base-2', 'base-3', closed=True)
