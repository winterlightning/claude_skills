"""An interstate route shield with a header and road center mark.
Plan: VRECT_L preserves the tall, pointed shield. Visible ink bounds: (6, 2, 42, 46).
Reduction: Two road dashes reduced to one; header lowered to enlarge its band and attached to explicit side endpoints.
Construction: Lucide shield: mirrored sides and pointed base."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '65d8507f-531a-4e81-bd3e-1e2516aebe33'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_33/route interstate_65d8507f-531a-4e81-bd3e-1e2516aebe33.svg'
AUTHOR = 'gpt-6'
PLAN = 'An interstate route shield with a header and road center mark.'
OMISSIONS = 'Two road dashes reduced to one; header lowered to enlarge its band and attached to explicit side endpoints.'
CONSTRUCTION_REFERENCES = 'Lucide shield: mirrored sides and pointed base.'
KEYSHAPE_INK_BOUNDS = (6, 2, 42, 46)

class AuthoredIcon(Solo48):
    icon_id = 'route-interstate'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('route', 'interstate')

    def build(self):
        self.add_bezier('left-top', (24, 6), ((19, 8), (14, 8), (11, 4)))
        self.add_bezier('left-upper', (11, 4), ((9, 9), (8, 12), (8, 17)))
        self.add_line('left-wall', (8, 17), (8, 19))
        self.add_bezier('left-lower', (8, 19), ((8, 31), (15, 40), (24, 44)))
        self.add_bezier('right-lower', (24, 44), ((33, 40), (40, 31), (40, 19)))
        self.add_line('right-wall', (40, 19), (40, 17))
        self.add_bezier('right-upper', (40, 17), ((40, 12), (39, 9), (37, 4)))
        self.add_bezier('right-top', (37, 4), ((34, 8), (29, 8), (24, 6)))
        self.add_contour('shield', 'left-top', 'left-upper', 'left-wall', 'left-lower', 'right-lower', 'right-wall', 'right-upper', 'right-top', closed=True)
        self.add_line('header', (8, 17), (40, 17))
        self.relate('connect', 'header', 'shield')
        self.add_line('road-mark', (24, 26), (24, 31))
