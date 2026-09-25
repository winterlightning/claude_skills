"""Independent 32px profile of state32-7b4acd01-51fe-4645-a2d7-08e28c65ee64.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7b4acd01-51fe-4645-a2d7-08e28c65ee64'
SOURCE_PATH = 'icon_set/assets/combination-state32/7b4acd01-51fe-4645-a2d7-08e28c65ee64.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7b4acd01-51fe-4645-a2d7-08e28c65ee64', 'icon_set/assets/combination-state32/7b4acd01-51fe-4645-a2d7-08e28c65ee64.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'd70e68b555408ab77093935d225fc184d7fcaad049b8d7d6d7bec71591882059'

class Drawing(Sub32):
    icon_id = 'state32-7b4acd01-51fe-4645-a2d7-08e28c65ee64'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 10), (16, 16))
        self.add_line('p1-r1-2', (16, 16), (21, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p1-r2-1', (16, 16), (16, 22))
        self.add_contour('path-1-2', 'p1-r2-1', closed=False)
        self.add_line('p1-r3-1', (12, 18), (20, 18))
        self.add_contour('path-1-3', 'p1-r3-1', closed=False)
        self.add_arc('p2-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p1-r2-1')
        self.relate("connect", 'p1-r1-2', 'p1-r2-1')
