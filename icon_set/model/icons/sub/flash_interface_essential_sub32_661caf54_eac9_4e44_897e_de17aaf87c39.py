"""Independent 32px profile of flash-interface-essential.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '661caf54-eac9-4e44-897e-de17aaf87c39'
SOURCE_PATH = 'pictographic-primitives/interface-essential/flash_661caf54-eac9-4e44-897e-de17aaf87c39.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('661caf54-eac9-4e44-897e-de17aaf87c39', 'pictographic-primitives/interface-essential/flash_661caf54-eac9-4e44-897e-de17aaf87c39.svg'),)
PROFILE_SOURCE_KEYS = ('solo/flash-interface-essential',)
SOLO_SOURCE_ICON_IDS = ('flash-interface-essential',)
REFERENCE_EXPORT_SHA256 = 'b0f5a0c0363b2e76d473dfd74bb38ac1f539260b41a6a164bc5436070ea6c89c'

class Drawing(Sub32):
    icon_id = 'flash-interface-essential-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (20, 2), (5, 18))
        self.add_line('p1-r1-2', (5, 18), (13, 18))
        self.add_line('p1-r1-3', (13, 18), (12, 30))
        self.add_line('p1-r1-4', (12, 30), (27, 14))
        self.add_line('p1-r1-5', (27, 14), (19, 14))
        self.add_line('p1-r1-6', (19, 14), (20, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
