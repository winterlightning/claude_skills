'warp-squeeze: independent smooth-curve repair.\n\nConstruction: Squeezed panel with four coherent curves and exact mirrored concave sidewalls.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/braces.svg and atomic-debug/braces.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'efb3c5db-a644-505f-b7f3-a21fccc2fb30'
SOURCE_PATH = 'pictographic-primitives/design/warp squeeze_efb3c5db-a644-505f-b7f3-a21fccc2fb30.svg'
AUTHOR = 'gpt-6'


class WarpSqueezeVariant2(Solo48):
    icon_id = 'warp-squeeze-v2'
    variant_of = 'warp-squeeze'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'squeeze', 'design')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'shape',(8,12),('C',(16,1.333333333),(32,1.333333333),(40,12)),('C',(30,18),(30,30),(40,36)),('C',(32,46.666666667),(16,46.666666667),(8,36)),('C',(18,30),(18,18),(8,12)),closed=True)
        contacts(self)
