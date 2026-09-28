"""Independent 32px profile of code-programing.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2b2755f6-afff-4284-a954-40e23b277e6f'
SOURCE_PATH = 'pictographic-primitives/programing/code_2b2755f6-afff-4284-a954-40e23b277e6f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2b2755f6-afff-4284-a954-40e23b277e6f', 'pictographic-primitives/programing/code_2b2755f6-afff-4284-a954-40e23b277e6f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/code-programing',)
SOLO_SOURCE_ICON_IDS = ('code-programing',)
REFERENCE_EXPORT_SHA256 = '828c31eb173125a2423d3d6b310d12ffc1d1d349051de06a9f3f39424ac10e01'

class Drawing(Sub32):
    icon_id = 'code-programing-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'programing'
    categories = ('programing', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 27), (20, 5))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (8, 8), (2, 16))
        self.add_line('p2-r1-2', (2, 16), (8, 24))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (24, 8), (30, 16))
        self.add_line('p3-r1-2', (30, 16), (24, 24))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
