# Variant of sitting-baby; parent file remains unchanged.
"""Seated infant with a large round head, two eyes, simple arms and open seated legs. SQUARE preserves generous proportions; Lucide baby informs the minimal face. Closed foot loops and extra diaper curves omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '10921a97-46e3-5bea-b3ba-ce5691a7278c'
SOURCE_PATH = 'pictographic-primitives/babies/baby care body_10921a97-46e3-5bea-b3ba-ce5691a7278c.svg'
AUTHOR = 'gpt-6'

class SittingBabyVariant2(Solo48):
    icon_id = 'sitting-baby-v2'
    variant_of = 'sitting-baby'
    variant_label = 'Simpler seated infant'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/babies'
    aliases = ()
    keywords = ('sitting', 'baby', 'infant', 'nursery')

    def build(self):
        # SQUARE: (2,2)-(46,46); front-facing, mirrored around x=24.
        self.add_arc('head-right', (24,2), (24,24), radius_x=11)
        self.add_arc('head-left', (24,24), (24,2), radius_x=11)
        self.add_contour('head', 'head-right', 'head-left', closed=True)
        self.add_dot('eye-left', (20,12))
        self.add_dot('eye-right', (28,12))
        self.add_arc('shoulder-left', (24,24), (10,32), radius_x=14, radius_y=8, sweep=False)
        self.add_line('arm-left', (10,32), (10,36))
        self.add_arc('shoulder-right', (38,32), (24,24), radius_x=14, radius_y=8, sweep=False)
        self.add_line('arm-right', (38,36), (38,32))
        self.add_contour('left-arm', 'shoulder-left', 'arm-left')
        self.add_contour('right-arm', 'arm-right', 'shoulder-right')
        self.relate('connect', 'head', 'left-arm')
        self.relate('connect', 'head', 'right-arm')
        self.relate('connect', 'left-arm', 'right-arm')
        self.add_arc('leg-left', (10,36), (10,46), radius_x=8, radius_y=5, sweep=False)
        self.add_line('seat-left', (10,46), (18,46))
        self.add_arc('leg-right', (38,46), (38,36), radius_x=8, radius_y=5, sweep=False)
        self.add_line('seat-right', (30,46), (38,46))
        self.add_contour('left-leg', 'leg-left', 'seat-left')
        self.add_contour('right-leg', 'seat-right', 'leg-right')
        self.relate('connect', 'left-arm', 'left-leg')
        self.relate('connect', 'right-arm', 'right-leg')
        self.add_line('diaper', (18,36), (30,36))
