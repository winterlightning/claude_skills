"""Microphone sound (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f991ef0f-2aa9-4924-9670-c07e3215f3a9'
SOURCE_PATH = 'pictographic-primitives/state/microphone sound_f991ef0f-2aa9-4924-9670-c07e3215f3a9.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class MicrophoneSound(Solo48):
    icon_id = 'microphone-sound'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('microphone', 'sound', 'state')

    def build(self):
        self.add_line('e0', (24, 44), (24, 4))
        self.add_line('e1', (16, 10), (16, 38))
        self.add_line('e2', (32, 34), (32, 14))
        self.add_line('e3', (8, 30), (8, 18))
        self.add_line('e4', (40, 27), (40, 22))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
