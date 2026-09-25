"""Independent 32px profile of state32-bae8ce7a-80bd-4ca5-b65d-f7e8e8792508.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'bae8ce7a-80bd-4ca5-b65d-f7e8e8792508'
SOURCE_PATH = 'icon_set/assets/combination-state32/bae8ce7a-80bd-4ca5-b65d-f7e8e8792508.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bae8ce7a-80bd-4ca5-b65d-f7e8e8792508', 'icon_set/assets/combination-state32/bae8ce7a-80bd-4ca5-b65d-f7e8e8792508.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '06a7719f879d7d8be852999ad63965cd16c31e06469085f0660441ffc0d585fc'

class Drawing(Sub32):
    icon_id = 'state32-bae8ce7a-80bd-4ca5-b65d-f7e8e8792508'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (30, 16))
        self.add_line('p1-r1-2', (30, 16), (2, 30))
        self.add_line('p1-r1-3', (2, 30), (9, 16))
        self.add_line('p1-r1-4', (9, 16), (2, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
