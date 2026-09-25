"""A dollar sign grows from a straight stem above two pointed leaves. VRECT_L centerline extremes (8,6)-(40,42) fit the upright plant. Lucide dollar-sign supplies paired round S bends; sprout supplies curved leaf construction. Omit the coin rim and veins so the dollar and open leaf interiors remain readable. Preserve mirrored leaves and intrinsic growth metaphor."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ffaf42d2-7401-4c82-b8d6-168a72a6a01c'
SOURCE_PATH = 'pictographic-primitives/symbol/flower dollar_ffaf42d2-7401-4c82-b8d6-168a72a6a01c.svg'
AUTHOR = 'gpt-6'

class MoneyPlant(Solo48):
    icon_id = 'money-plant'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('money', 'plant', 'growth', 'investment', 'dollar', 'finance', 'savings', 'profit')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_line('dollar-top-right', (30, 7), (24, 7))
        self.add_line('dollar-top-left', (24, 7), (22, 7))
        self.add_arc('dollar-upper', (22, 7), (22, 15), radius_x=4, sweep=False)
        self.add_line('dollar-middle', (22, 15), (26, 15))
        self.add_arc('dollar-lower', (26, 15), (26, 23), radius_x=4)
        self.add_line('dollar-bottom-right', (26, 23), (24, 23))
        self.add_line('dollar-bottom-left', (24, 23), (18, 23))
        self.add_contour('dollar', 'dollar-top-right', 'dollar-top-left', 'dollar-upper', 'dollar-middle', 'dollar-lower', 'dollar-bottom-right', 'dollar-bottom-left')
        self.add_line('dollar-tick', (24, 4), (24, 7))
        self.relate('connect', 'dollar', 'dollar-tick')
        self.add_polyline('stem', (24, 23), (24, 44))
        self.relate('connect', 'dollar', 'stem')
        for name, tip, root, sweep in [('left', (8, 29), (19, 44), False), ('right', (40, 29), (29, 44), True)]:
            self.add_arc('leaf-' + name + '-outer', tip, root, radius_x=11, radius_y=15, sweep=sweep)
            self.add_arc('leaf-' + name + '-inner', root, tip, radius_x=11, radius_y=15, sweep=sweep)
            self.add_contour('leaf-' + name, 'leaf-' + name + '-outer', 'leaf-' + name + '-inner', closed=True)
            self.add_line('branch-' + name, root, (24, 44))
            self.relate('connect', 'leaf-' + name, 'branch-' + name)
            self.relate('connect', 'branch-' + name, 'stem')
