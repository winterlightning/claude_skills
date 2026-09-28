"""Independent 32px profile of movie-camera-reels.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '9518f09e-6822-415c-9a66-f43eca8bd8d0'
SOURCE_PATH = 'pictographic-primitives/symbol/video_9518f09e-6822-415c-9a66-f43eca8bd8d0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9518f09e-6822-415c-9a66-f43eca8bd8d0', 'pictographic-primitives/symbol/video_9518f09e-6822-415c-9a66-f43eca8bd8d0.svg'),)
PROFILE_SOURCE_KEYS = ('solo/movie-camera-reels',)
SOLO_SOURCE_ICON_IDS = ('movie-camera-reels',)
REFERENCE_EXPORT_SHA256 = '59cfc4f3926b4a59990d5458c953519f28c54e8f897a377254cc809473081cf0'

class Drawing(Sub32):
    icon_id = 'movie-camera-reels-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 8), (14, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (14, 8), (2, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (21, 11), (27, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (27, 11), (21, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (7, 14), (8, 14))
        self.add_line('p3-r1-2', (8, 14), (24, 14))
        self.add_line('p3-r1-3', (24, 14), (24, 19))
        self.add_line('p3-r1-4', (24, 19), (30, 16))
        self.add_line('p3-r1-5', (30, 16), (30, 28))
        self.add_line('p3-r1-6', (30, 28), (24, 25))
        self.add_line('p3-r1-7', (24, 25), (24, 27))
        self.add_arc('p3-r1-8', (24, 27), (21, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-9', (21, 30), (7, 30))
        self.add_arc('p3-r1-10', (7, 30), (2, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p3-r1-11', (2, 25), (2, 19))
        self.add_arc('p3-r1-12', (2, 19), (7, 14), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', 'p3-r1-9', 'p3-r1-10', 'p3-r1-11', 'p3-r1-12', closed=False)
