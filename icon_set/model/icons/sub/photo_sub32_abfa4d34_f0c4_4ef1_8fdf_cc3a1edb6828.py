"""Independent 32px profile of photo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'abfa4d34-f0c4-4ef1-8fdf-cc3a1edb6828'
SOURCE_PATH = 'pictographic-primitives/state/photo_abfa4d34-f0c4-4ef1-8fdf-cc3a1edb6828.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('abfa4d34-f0c4-4ef1-8fdf-cc3a1edb6828', 'pictographic-primitives/state/photo_abfa4d34-f0c4-4ef1-8fdf-cc3a1edb6828.svg'),)
PROFILE_SOURCE_KEYS = ('solo/photo',)
SOLO_SOURCE_ICON_IDS = ('photo',)
REFERENCE_EXPORT_SHA256 = '6159c913c176accd6d998920afc5c5a54568a5ba079f774de41016c5646f6f1d'

class Drawing(Sub32):
    icon_id = 'photo-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (4, 28), (11, 19))
        self.add_line('p1-r1-2', (11, 19), (14, 22))
        self.add_line('p1-r1-3', (14, 22), (22, 13))
        self.add_line('p1-r1-4', (22, 13), (30, 24))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (30, 24), (29, 28))
        self.add_arc('p2-r1-2', (29, 28), (27, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (27, 30), (6, 30))
        self.add_arc('p2-r1-4', (6, 30), (2, 27), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p2-r1-5', (2, 27), (2, 6))
        self.add_arc('p2-r1-6', (2, 6), (6, 2), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p2-r1-7', (6, 2), (27, 2))
        self.add_arc('p2-r1-8', (27, 2), (30, 5), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-9', (30, 5), (30, 24))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', closed=False)
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-9')
