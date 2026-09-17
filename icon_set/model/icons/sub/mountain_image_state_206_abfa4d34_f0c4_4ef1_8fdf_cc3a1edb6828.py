"""Mountain Image: Two unequal mountain peaks form a continuous zigzag, with the taller peak on the right and a tiny sun mark above-left. Generate this component alone; exclude Rounded Square Frame.

Construction: Two unequal open mountain peaks retain the source upper-left tiny sun stroke and no baseline.
Keyshape: HRECT_XL; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'abfa4d34-f0c4-4ef1-8fdf-cc3a1edb6828'
SOURCE_PATH = 'pictographic-primitives/state/photo_abfa4d34-f0c4-4ef1-8fdf-cc3a1edb6828.svg'
AUTHOR = 'gpt-6'


class MountainImageState206(Sub32):
    icon_id = 'mountain-image-state-206'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('mountain', 'image', 'unequal', 'peaks', 'form', 'continuous', 'zigzag', 'taller')

    def build(self):
        self.add_polyline('ridge',(2,28),(10,16),(15,21),(23,6),(30,26))
        self.add_line('sun',(5,4),(5,6))
