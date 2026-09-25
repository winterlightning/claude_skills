"""Independent 32px profile of state32-a19d3d8c-ca4f-4084-a880-3c773e5774a7.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a19d3d8c-ca4f-4084-a880-3c773e5774a7'
SOURCE_PATH = 'icon_set/assets/combination-state32/a19d3d8c-ca4f-4084-a880-3c773e5774a7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a19d3d8c-ca4f-4084-a880-3c773e5774a7', 'icon_set/assets/combination-state32/a19d3d8c-ca4f-4084-a880-3c773e5774a7.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '36c8c5a48b466efcd1e037174d79d14046e8f3220d58cf4f2fb411cb6eded7ef'

class Drawing(Sub32):
    icon_id = 'state32-a19d3d8c-ca4f-4084-a880-3c773e5774a7'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 2), (2, 16))
        self.add_line('p1-r1-2', (2, 16), (30, 30))
        self.add_line('p1-r1-3', (30, 30), (23, 16))
        self.add_line('p1-r1-4', (23, 16), (30, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
