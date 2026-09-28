"""Independent 32px profile of gas-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c6b95b7c-51f0-41d6-9758-e2c0e4821afa'
SOURCE_PATH = 'pictographic-primitives/symbol/gas_c6b95b7c-51f0-41d6-9758-e2c0e4821afa.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c6b95b7c-51f0-41d6-9758-e2c0e4821afa', 'pictographic-primitives/symbol/gas_c6b95b7c-51f0-41d6-9758-e2c0e4821afa.svg'),)
PROFILE_SOURCE_KEYS = ('solo/gas-symbol',)
SOLO_SOURCE_ICON_IDS = ('gas-symbol',)
REFERENCE_EXPORT_SHA256 = '66068ccf3c86165962d29426ca0212da0c787d24a2b3f1e5bf9195fb716a239c'

class Drawing(Sub32):
    icon_id = 'gas-symbol-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (12, 2), (20, 2))
        self.add_line('p1-r1-2', (20, 2), (20, 8))
        self.add_bezier('p1-r1-3', (20, 8), ((20, 10), (27, 10), (27, 16)))
        self.add_line('p1-r1-4', (27, 16), (27, 20))
        self.add_line('p1-r1-5', (27, 20), (27, 23))
        self.add_arc('p1-r1-6', (27, 23), (16, 30), radius_x=11, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('p1-r1-7', (16, 30), (5, 23), radius_x=11, radius_y=7, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (5, 23), (5, 20))
        self.add_line('p1-r1-9', (5, 20), (5, 16))
        self.add_bezier('p1-r1-10', (5, 16), ((5, 10), (12, 10), (12, 8)))
        self.add_line('p1-r1-11', (12, 8), (12, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
        self.add_line('p2-r1-1', (5, 20), (27, 20))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p1-r1-8', 'p2-r1-1')
        self.relate("connect", 'p1-r1-9', 'p2-r1-1')
