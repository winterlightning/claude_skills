"""Smiling Face: Two short vertical eyes sit above a broad upward-curving smile, with no separate outline around the facial features. Generate this component alone; exclude Round Speech Bubble.

Construction: Only the source eyes and upward smile are drawn; the speech-bubble frame is not a face outline.
Keyshape: HRECT_XL; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd0333cae-aa48-4180-9d32-5051aadda8fa'
SOURCE_PATH = 'pictographic-primitives/state/messages bubble round smile_d0333cae-aa48-4180-9d32-5051aadda8fa.svg'
AUTHOR = 'gpt-6'


class SmilingFaceSubState172(Sub32):
    icon_id = 'smiling-face-sub-state-172'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('smiling', 'face', 'short', 'vertical', 'eyes', 'sit', 'broad', 'upward')

    def build(self):
        for x in (8,24):self.add_line(f'eye-{x}',(x,4),(x,8))
        self.add_arc('smile',(2,18),(30,18),radius_x=14,radius_y=10,sweep=False)
