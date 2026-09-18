"""Independent 32px profile of vintage-movie-camera-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e27f92c4-11f6-4c62-91f1-78b562213eb2'
SOURCE_PATH = 'pictographic-primitives/state/video_e27f92c4-11f6-4c62-91f1-78b562213eb2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e27f92c4-11f6-4c62-91f1-78b562213eb2', 'pictographic-primitives/state/video_e27f92c4-11f6-4c62-91f1-78b562213eb2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/vintage-movie-camera-solo',)
SOLO_SOURCE_ICON_IDS = ('vintage-movie-camera-solo',)
REFERENCE_EXPORT_SHA256 = '68e2a0a36089dd99416d90054cef68f6915ee4d4ca7bae94e8cbda4866843754'

class Drawing(Sub32):
    icon_id = 'vintage-movie-camera-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (4, 7), (13, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (13, 7), (4, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (19, 7), (28, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (28, 7), (19, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (5, 18), (18, 18))
        self.add_arc('p3-r1-2', (18, 18), (21, 21), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-3', (21, 21), (30, 18))
        self.add_line('p3-r1-4', (30, 18), (30, 30))
        self.add_line('p3-r1-5', (30, 30), (21, 27))
        self.add_arc('p3-r1-6', (21, 27), (18, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-7', (18, 30), (5, 30))
        self.add_arc('p3-r1-8', (5, 30), (2, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-9', (2, 27), (2, 21))
        self.add_arc('p3-r1-10', (2, 21), (5, 18), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', 'p3-r1-9', 'p3-r1-10', closed=False)
