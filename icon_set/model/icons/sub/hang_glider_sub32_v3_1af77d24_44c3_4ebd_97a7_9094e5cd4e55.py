"""Independent 32px profile of hang-glider.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '1af77d24-44c3-4ebd-97a7-9094e5cd4e55'
SOURCE_PATH = 'pictographic-primitives/animals/fly_1af77d24-44c3-4ebd-97a7-9094e5cd4e55.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1af77d24-44c3-4ebd-97a7-9094e5cd4e55', 'pictographic-primitives/animals/fly_1af77d24-44c3-4ebd-97a7-9094e5cd4e55.svg'), ('c154bd5e-85cc-4682-977f-bac1bfee4f64', 'pictographic-primitives/animals/fly_c154bd5e-85cc-4682-977f-bac1bfee4f64.svg'))
PROFILE_SOURCE_KEYS = ('solo/hang-glider', 'solo/hang-glider-with-harness')
SOLO_SOURCE_ICON_IDS = ('hang-glider', 'hang-glider-with-harness')
REFERENCE_EXPORT_SHA256 = '8af35c4515fbf2960523b2057f0128f30f6f21bc95e75a45d47415fef7a08c2f'

class DrawingVariant3(Sub32):
    icon_id = 'hang-glider-sub32-v3'
    related_origin_icon_id = 'hang-glider-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'animals'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('left-leading', (4, 17), (16, 6))
        self.add_line('right-leading', (16, 6), (28, 17))
        self.add_bezier('right-tip', (28, 17), ((31, 20), (30, 22), (27, 21)))
        self.add_bezier('trailing', (27, 21), ((17, 18), (15, 18), (5, 21)))
        self.add_bezier('left-tip', (5, 21), ((2, 22), (1, 20), (4, 17)))
        self.add_contour('wing', 'left-leading', 'right-leading', 'right-tip', 'trailing', 'left-tip', closed=True)
        self.add_polyline('frame', (10, 19), (13, 26), (19, 26), (22, 19))
        self.relate('connect', 'wing', 'frame')
