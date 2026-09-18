"""Independent 32px profile of state32-58727bf7-a897-4f91-b5c6-d02dbeb80019.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '58727bf7-a897-4f91-b5c6-d02dbeb80019'
SOURCE_PATH = 'icon_set/assets/combination-state32/58727bf7-a897-4f91-b5c6-d02dbeb80019.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('58727bf7-a897-4f91-b5c6-d02dbeb80019', 'icon_set/assets/combination-state32/58727bf7-a897-4f91-b5c6-d02dbeb80019.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'd0a9478da76256fa7471c9d8a96adab03e8b211af6a75612b1420626d562336b'

class Drawing(Sub32):
    icon_id = 'state32-58727bf7-a897-4f91-b5c6-d02dbeb80019'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 2), (21, 2))
        self.add_line('p1-r1-2', (21, 2), (21, 19))
        self.add_line('p1-r1-3', (21, 19), (29, 19))
        self.add_line('p1-r1-4', (29, 19), (16, 30))
        self.add_line('p1-r1-5', (16, 30), (3, 19))
        self.add_line('p1-r1-6', (3, 19), (11, 19))
        self.add_line('p1-r1-7', (11, 19), (11, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
