"""Independent 32px profile of crane-hook-with-square-mount.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'fd80bcd7-73ab-4b8e-8a28-7672b7384731'
SOURCE_PATH = 'pictographic-primitives/construction/hook_fd80bcd7-73ab-4b8e-8a28-7672b7384731.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fd80bcd7-73ab-4b8e-8a28-7672b7384731', 'pictographic-primitives/construction/hook_fd80bcd7-73ab-4b8e-8a28-7672b7384731.svg'),)
PROFILE_SOURCE_KEYS = ('solo/crane-hook-with-square-mount',)
SOLO_SOURCE_ICON_IDS = ('crane-hook-with-square-mount',)
REFERENCE_EXPORT_SHA256 = 'ee842c0b14c3d8f5a3fb7ab0452df5a7b7e7b874100dc632539daeda3ea509b5'

class Drawing(Sub32):
    icon_id = 'crane-hook-with-square-mount-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'construction'
    categories = ('construction', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 2), (21, 2))
        self.add_line('p1-r1-2', (21, 2), (21, 11))
        self.add_line('p1-r1-3', (21, 11), (16, 11))
        self.add_line('p1-r1-4', (16, 11), (11, 11))
        self.add_line('p1-r1-5', (11, 11), (11, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (16, 11), (16, 14))
        self.add_arc('p2-r1-2', (16, 14), (21, 19), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_bezier('p2-r1-3', (21, 19), ((23, 19), (26, 20), (27, 21)))
        self.add_bezier('p2-r1-4', (27, 21), ((29, 22), (30, 23), (30, 25)))
        self.add_arc('p2-r1-5', (30, 25), (2, 25), radius_x=14, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p2-r1-6', (2, 25), (2, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
