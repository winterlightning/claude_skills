"""Independent 32px profile of go-text.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '6526c9e6-1222-445f-b7c5-c16580a2e930'
SOURCE_PATH = 'pictographic-primitives/symbol/GO_6526c9e6-1222-445f-b7c5-c16580a2e930.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6526c9e6-1222-445f-b7c5-c16580a2e930', 'pictographic-primitives/symbol/GO_6526c9e6-1222-445f-b7c5-c16580a2e930.svg'),)
PROFILE_SOURCE_KEYS = ('solo/go-text',)
SOLO_SOURCE_ICON_IDS = ('go-text',)
REFERENCE_EXPORT_SHA256 = '425f4aa0b5fac6db2bd8a75e28e74fde34c22ee567fe8bbb24e998511389b6a5'

class Drawing(Sub32):
    icon_id = 'go-text-sub32'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Letters from the official typeface (grid-hinted v2), 8 units apart.
        self.add_line('go-0-0-0', (11, 8), (8, 8))
        self.add_bezier('go-0-0-1', (8, 8), ((4.91, 8), (2, 11.78), (2, 16)), ((2, 20.64), (4.91, 24), (8, 24)), ((10.43, 24), (12, 22.43), (12, 20)))
        self.add_line('go-0-0-2', (12, 20), (12, 17))
        self.add_contour('go-0-0', 'go-0-0-0', 'go-0-0-1', 'go-0-0-2')
        self.add_bezier('go-1-0-0', (25, 8), ((27.74, 8), (30, 10.41), (30, 13)))
        self.add_line('go-1-0-1', (30, 13), (30, 19))
        self.add_bezier('go-1-0-2', (30, 19), ((30, 21.59), (27.74, 24), (25, 24)), ((22.26, 24), (20, 21.59), (20, 19)))
        self.add_line('go-1-0-3', (20, 19), (20, 13))
        self.add_bezier('go-1-0-4', (20, 13), ((20, 10.41), (22.26, 8), (25, 8)))
        self.add_contour('go-1-0', 'go-1-0-0', 'go-1-0-1', 'go-1-0-2', 'go-1-0-3', 'go-1-0-4', closed=True)
