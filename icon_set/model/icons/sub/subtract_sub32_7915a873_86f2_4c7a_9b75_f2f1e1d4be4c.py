"""Independent 32px profile of subtract.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7915a873-86f2-4c7a-9b75-f2f1e1d4be4c'
SOURCE_PATH = 'pictographic-primitives/interface-essential/subtract_7915a873-86f2-4c7a-9b75-f2f1e1d4be4c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7915a873-86f2-4c7a-9b75-f2f1e1d4be4c', 'pictographic-primitives/interface-essential/subtract_7915a873-86f2-4c7a-9b75-f2f1e1d4be4c.svg'), ('b7450985-5938-4c75-b40d-352e69b5080d', 'pictographic-primitives/symbol/minus_b7450985-5938-4c75-b40d-352e69b5080d.svg'))
PROFILE_SOURCE_KEYS = ('solo/subtract', 'solo/minus-solo')
SOLO_SOURCE_ICON_IDS = ('subtract', 'minus-solo')
REFERENCE_EXPORT_SHA256 = 'a9d178dbfd8f261371bc749e4a8ab6387f2f12beacbe68036ceea205482ee2a7'

class Drawing(Sub32):
    icon_id = 'subtract-sub32'
    keyshape = Keyshape.HRECT_S
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 16), (30, 16))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
