"""Independent 32px profile of microphone-sound.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f991ef0f-2aa9-4924-9670-c07e3215f3a9'
SOURCE_PATH = 'pictographic-primitives/state/microphone sound_f991ef0f-2aa9-4924-9670-c07e3215f3a9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f991ef0f-2aa9-4924-9670-c07e3215f3a9', 'pictographic-primitives/state/microphone sound_f991ef0f-2aa9-4924-9670-c07e3215f3a9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/microphone-sound',)
SOLO_SOURCE_ICON_IDS = ('microphone-sound',)
REFERENCE_EXPORT_SHA256 = '9e7fec83b02b08562b88ecacdb030ebc8e249ff66efdd4a60e87a68ebe0fad84'

class Drawing(Sub32):
    icon_id = 'microphone-sound-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (16, 2))
        self.add_arc('p1-r1-2', (16, 2), (22, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (22, 8), (22, 10))
        self.add_line('p1-r1-4', (22, 10), (22, 13))
        self.add_arc('p1-r1-5', (22, 13), (16, 19), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (16, 19), (16, 19))
        self.add_arc('p1-r1-7', (16, 19), (10, 13), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (10, 13), (10, 10))
        self.add_line('p1-r1-9', (10, 10), (10, 8))
        self.add_arc('p1-r1-10', (10, 8), (16, 2), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (10, 10), (22, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 19), (16, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (5, 30), (16, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (16, 30), (27, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p3-r1-1')
        self.relate("connect", 'p1-r1-6', 'p3-r1-1')
        self.relate("connect", 'p1-r1-7', 'p3-r1-1')
        self.relate("connect", 'p1-r1-8', 'p2-r1-1')
        self.relate("connect", 'p1-r1-9', 'p2-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p5-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
