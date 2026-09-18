"""Independent 32px profile of state32-19c25b61-6678-43f8-aae6-dc07a9ea8291.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '19c25b61-6678-43f8-aae6-dc07a9ea8291'
SOURCE_PATH = 'icon_set/assets/combination-state32/19c25b61-6678-43f8-aae6-dc07a9ea8291.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('19c25b61-6678-43f8-aae6-dc07a9ea8291', 'icon_set/assets/combination-state32/19c25b61-6678-43f8-aae6-dc07a9ea8291.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '45540cef4120965666bf7a2eddea79074758ae449ab78fe780fd280d847b7bb7'

class Drawing(Sub32):
    icon_id = 'state32-19c25b61-6678-43f8-aae6-dc07a9ea8291'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (12, 11), (21, 16))
        self.add_line('p1-r1-2', (21, 16), (12, 21))
        self.add_line('p1-r1-3', (12, 21), (12, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_arc('p2-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
