"""Independent 32px profile of state32-91065c0d-d056-4c23-a604-1f2b872fca43.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '91065c0d-d056-4c23-a604-1f2b872fca43'
SOURCE_PATH = 'icon_set/assets/combination-state32/91065c0d-d056-4c23-a604-1f2b872fca43.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('91065c0d-d056-4c23-a604-1f2b872fca43', 'icon_set/assets/combination-state32/91065c0d-d056-4c23-a604-1f2b872fca43.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '122799c6ee20a9a3084ab120e7242dec747f851bcc53095bf58a1d088507e484'

class Drawing(Sub32):
    icon_id = 'state32-91065c0d-d056-4c23-a604-1f2b872fca43'
    keyshape = Keyshape.VRECT_L
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 12), (8, 5))
        self.add_line('p1-r1-2', (8, 5), (13, 2))
        self.add_line('p1-r1-3', (13, 2), (19, 2))
        self.add_line('p1-r1-4', (19, 2), (24, 5))
        self.add_line('p1-r1-5', (24, 5), (21, 12))
        self.add_line('p1-r1-6', (21, 12), (11, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_arc('p2-r1-1', (7, 21), (25, 21), radius_x=9, radius_y=9, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (25, 21), (7, 21), radius_x=9, radius_y=9, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
