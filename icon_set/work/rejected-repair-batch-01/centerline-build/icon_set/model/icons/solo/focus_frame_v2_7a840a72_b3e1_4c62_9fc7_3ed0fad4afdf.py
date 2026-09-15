'focus-frame: independent smooth-curve repair.\n\nConstruction: Square frame around a smaller square; identical circular corner geometry.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/square.svg and atomic-debug/square.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '7a840a72-b3e1-4c62-9fc7-3ed0fad4afdf'
SOURCE_PATH = 'pictographic-primitives/photography/focus frame_7a840a72-b3e1-4c62-9fc7-3ed0fad4afdf.svg'
AUTHOR = 'gpt-6'


class FocusFrameVariant2(Solo48):
    icon_id = 'focus-frame-v2'
    variant_of = 'focus-frame'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('focus', 'frame', 'photography')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'outer',6,6,42,42,4)
        box(self,'inner',16,16,32,32,2)
        contacts(self)
