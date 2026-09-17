"""UV Text: The uppercase letters UV stand side by side, with a round-bottomed U and a V with a softly rounded lower point. Generate this component alone; exclude Circle Frame.

Construction: A narrow round-bottomed U and open V stand on a shared baseline.
Keyshape: HRECT_XL; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e3d5e666-c846-4c0b-af9f-f90826b900a7'
SOURCE_PATH = 'pictographic-primitives/state/circle uv text_e3d5e666-c846-4c0b-af9f-f90826b900a7.svg'
AUTHOR = 'gpt-6'


class UvText(Sub32):
    icon_id = 'uv-text'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('uv', 'text', 'uppercase', 'letters', 'stand', 'side', 'round', 'bottomed')

    def build(self):
        self.add_line('left',(2,4),(2,23))
        self.add_arc('bottom',(2,23),(12,23),radius_x=5,sweep=False)
        self.add_line('right',(12,23),(12,4))
        self.add_contour('u','left','bottom','right')
        self.add_polyline('v',(20,4),(25,28),(30,4))
