"""Independent 32px profile of code.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '13ea8366-b426-4bc2-a649-eea82df87819'
SOURCE_PATH = 'pictographic-primitives/programing/code_13ea8366-b426-4bc2-a649-eea82df87819.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('13ea8366-b426-4bc2-a649-eea82df87819', 'pictographic-primitives/programing/code_13ea8366-b426-4bc2-a649-eea82df87819.svg'),)
PROFILE_SOURCE_KEYS = ('solo/code',)
SOLO_SOURCE_ICON_IDS = ('code',)
REFERENCE_EXPORT_SHA256 = 'f93c3fab4228d36eb95d370b213390a76309529e30052be0d14ffe0815fc7df6'

class Drawing(Sub32):
    icon_id = 'code-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'programing'
    categories = ('programing', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 5), (2, 16))
        self.add_line('p1-r1-2', (2, 16), (8, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (24, 5), (30, 16))
        self.add_line('p2-r1-2', (30, 16), (24, 27))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
