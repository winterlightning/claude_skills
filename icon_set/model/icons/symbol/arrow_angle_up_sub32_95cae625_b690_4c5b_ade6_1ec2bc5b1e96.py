"""Independent 32px profile of arrow-angle-up.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '95cae625-b690-4c5b-ade6-1ec2bc5b1e96'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow angle up_95cae625-b690-4c5b-ade6-1ec2bc5b1e96.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('95cae625-b690-4c5b-ade6-1ec2bc5b1e96', 'pictographic-primitives/symbol/arrow angle up_95cae625-b690-4c5b-ade6-1ec2bc5b1e96.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-angle-up',)
SOLO_SOURCE_ICON_IDS = ('arrow-angle-up',)
REFERENCE_EXPORT_SHA256 = 'a815d120fd4fedb6b27ef35011e4b1e72e140c7a9aa39bfbcb7259eab5bb7918'

class Drawing(Sub32):
    icon_id = 'arrow-angle-up-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (30, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
