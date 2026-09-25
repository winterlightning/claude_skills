"""Sad Face: Two short upright eyes stand above a broad downturned mouth, with no separate head outline surrounding the features. Generate this component alone; exclude Speech Bubble.

Construction: Short upright eyes sit above an open downturned mouth, matching the source expression.
Keyshape: HRECT_XL; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '45f458f8-61bb-42f1-853f-4d3f292ca46d'
SOURCE_PATH = 'pictographic-primitives/state/messages bubble square sad_45f458f8-61bb-42f1-853f-4d3f292ca46d.svg'
AUTHOR = 'gpt-6'


class SadFaceSub(Sub32):
    icon_id = 'sad-face-sub'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('sad', 'face', 'short', 'upright', 'eyes', 'stand', 'broad', 'downturned')

    def build(self):
        for x in (8,24):self.add_line(f'eye-{x}',(x,4),(x,8))
        self.add_arc('mouth',(2,28),(30,28),radius_x=14,radius_y=9)
