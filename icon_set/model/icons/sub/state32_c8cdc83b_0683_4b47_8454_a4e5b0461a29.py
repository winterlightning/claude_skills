"""Independent 32px profile of state32-c8cdc83b-0683-4b47-8454-a4e5b0461a29.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c8cdc83b-0683-4b47-8454-a4e5b0461a29'
SOURCE_PATH = 'icon_set/assets/combination-state32/c8cdc83b-0683-4b47-8454-a4e5b0461a29.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c8cdc83b-0683-4b47-8454-a4e5b0461a29', 'icon_set/assets/combination-state32/c8cdc83b-0683-4b47-8454-a4e5b0461a29.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '5af3228161685f41992a96239b142c72271959bbdc01e8528b781c69d02f0e98'

class Drawing(Sub32):
    icon_id = 'state32-c8cdc83b-0683-4b47-8454-a4e5b0461a29'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (12, 16), (20, 16))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p1-r2-1', (16, 12), (16, 20))
        self.add_contour('path-1-2', 'p1-r2-1', closed=False)
        self.add_arc('p2-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
