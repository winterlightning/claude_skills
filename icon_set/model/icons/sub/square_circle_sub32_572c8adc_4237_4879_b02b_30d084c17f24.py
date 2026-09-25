"""Independent 32px profile of square-circle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '572c8adc-4237-4879-b02b-30d084c17f24'
SOURCE_PATH = 'pictographic-primitives/state/square circle_572c8adc-4237-4879-b02b-30d084c17f24.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('572c8adc-4237-4879-b02b-30d084c17f24', 'pictographic-primitives/state/square circle_572c8adc-4237-4879-b02b-30d084c17f24.svg'),)
PROFILE_SOURCE_KEYS = ('solo/square-circle',)
SOLO_SOURCE_ICON_IDS = ('square-circle',)
REFERENCE_EXPORT_SHA256 = '4f4056be3f46f29fd7b4044543601eb168868e1a74579304116542d64693993d'

class Drawing(Sub32):
    icon_id = 'square-circle-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 21), (11, 11))
        self.add_line('p1-r1-2', (11, 11), (21, 11))
        self.add_line('p1-r1-3', (21, 11), (21, 21))
        self.add_line('p1-r1-4', (21, 21), (11, 21))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_arc('p2-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
