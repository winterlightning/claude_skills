"""Independent 32px profile of state32-0e1c9946-f691-4b0b-a27c-05b65a10e50d.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0e1c9946-f691-4b0b-a27c-05b65a10e50d'
SOURCE_PATH = 'icon_set/assets/combination-state32/0e1c9946-f691-4b0b-a27c-05b65a10e50d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0e1c9946-f691-4b0b-a27c-05b65a10e50d', 'icon_set/assets/combination-state32/0e1c9946-f691-4b0b-a27c-05b65a10e50d.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '9aa0f66a9fbc06c192a5a26ef80887ffb3bb6458fd491defb6ba678c9cbca271'

class Drawing(Sub32):
    icon_id = 'state32-0e1c9946-f691-4b0b-a27c-05b65a10e50d'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (20, 2), (4, 19))
        self.add_line('p1-r1-2', (4, 19), (15, 19))
        self.add_line('p1-r1-3', (15, 19), (10, 30))
        self.add_line('p1-r1-4', (10, 30), (28, 12))
        self.add_line('p1-r1-5', (28, 12), (17, 12))
        self.add_line('p1-r1-6', (17, 12), (20, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
