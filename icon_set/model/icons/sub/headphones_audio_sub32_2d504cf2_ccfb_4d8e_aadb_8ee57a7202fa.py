"""Independent 32px profile of headphones-audio.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2d504cf2-ccfb-4d8e-aadb-8ee57a7202fa'
SOURCE_PATH = 'pictographic-primitives/audio/headphones_2d504cf2-ccfb-4d8e-aadb-8ee57a7202fa.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2d504cf2-ccfb-4d8e-aadb-8ee57a7202fa', 'pictographic-primitives/audio/headphones_2d504cf2-ccfb-4d8e-aadb-8ee57a7202fa.svg'),)
PROFILE_SOURCE_KEYS = ('solo/headphones-audio',)
SOLO_SOURCE_ICON_IDS = ('headphones-audio',)
REFERENCE_EXPORT_SHA256 = 'e2617c7a7bb7675b49c11b8b9de23adbf6bf8c7ab84629f7007d497252e869de'

class Drawing(Sub32):
    icon_id = 'headphones-audio-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'audio'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 16), (2, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (30, 16), (30, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 21), (8, 21))
        self.add_line('p4-r1-2', (8, 21), (8, 30))
        self.add_line('p4-r1-3', (8, 30), (2, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.add_line('p5-r1-1', (30, 21), (24, 21))
        self.add_line('p5-r1-2', (24, 21), (24, 30))
        self.add_line('p5-r1-3', (24, 30), (30, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-3')
        self.relate("connect", 'p3-r1-1', 'p5-r1-3')
