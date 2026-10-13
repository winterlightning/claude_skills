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
        # Movie camera: two film reels above the body, a triangle lens on the right.
        for k, x in enumerate((7, 25)):
            self.add_arc(f'reel-{k}-1', (x - 5, 7), (x + 5, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
            self.add_arc(f'reel-{k}-2', (x + 5, 7), (x - 5, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
            self.add_contour(f'reel-{k}', f'reel-{k}-1', f'reel-{k}-2', closed=True)
        self.add_polyline('body', (2, 20), (22, 20), (22, 30), (2, 30), closed=True)
        self.add_polyline('lens', (30, 20), (22, 25), (30, 30))
        self.relate('connect', 'body', 'lens')
