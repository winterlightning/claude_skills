"""Mountain Image: A single mountain slope rises to a softly rounded summit and descends right, with a tiny sun dot above-left. Generate this component alone; exclude Rectangle Frame.

Construction: The source shows one open rounded mountain ridge, without a sun or added baseline.
Keyshape: HRECT_S; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '94993cb5-32ce-48f8-ba6f-9fe516a4704d'
SOURCE_PATH = 'pictographic-primitives/state/images_94993cb5-32ce-48f8-ba6f-9fe516a4704d.svg'
AUTHOR = 'gpt-6'


class MountainImageState139(Sub32):
    icon_id = 'mountain-image-state-139'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('mountain', 'image', 'single', 'slope', 'rises', 'softly', 'rounded', 'summit')

    def build(self):
        self.add_line('left',(2,22),(17,11))
        self.add_arc('crest',(17,11),(23,11),radius_x=5,radius_y=5)
        self.add_line('right',(23,11),(30,18))
        self.add_contour('ridge','left','crest','right')
