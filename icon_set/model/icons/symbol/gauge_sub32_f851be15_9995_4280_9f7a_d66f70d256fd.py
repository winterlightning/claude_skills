"""Independent 32px profile of gauge.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'f851be15-9995-4280-9f7a-d66f70d256fd'
SOURCE_PATH = 'pictographic-primitives/symbol/gauge_f851be15-9995-4280-9f7a-d66f70d256fd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f851be15-9995-4280-9f7a-d66f70d256fd', 'pictographic-primitives/symbol/gauge_f851be15-9995-4280-9f7a-d66f70d256fd.svg'),)
PROFILE_SOURCE_KEYS = ('solo/gauge',)
SOLO_SOURCE_ICON_IDS = ('gauge',)
REFERENCE_EXPORT_SHA256 = 'b1057982da61ba3025d8140132084e8edf2e373a8ff9b1c1d87ed8a2a61c10ee'

class Drawing(Sub32):
    icon_id = 'gauge-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Gauge: dial ring with three ticks and a needle from the centre.
        self.add_arc('dial-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('dial-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('dial', 'dial-1', 'dial-2', closed=True)
        self.add_line('tick-l', (2, 16), (5, 16))
        self.add_line('tick-t', (16, 2), (16, 5))
        self.add_line('tick-r', (30, 16), (27, 16))
        self.add_line('needle', (14, 18), (20, 12))
        self.relate('connect', 'dial', 'tick-l')
        self.relate('connect', 'dial', 'tick-t')
        self.relate('connect', 'dial', 'tick-r')
