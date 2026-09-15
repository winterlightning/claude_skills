'vertical-rectangcle: independent smooth-curve repair.\n\nConstruction: Rounded vertical frame with equal corner radii; centered controls or a shared sidebar divider retain the original panel meaning.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/rectangle-horizontal.svg and atomic-debug/rectangle-horizontal.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'b24697a2-f23c-47f5-882a-55246a5eb7ad'
SOURCE_PATH = 'pictographic-primitives/symbol/vertical rectangcle_b24697a2-f23c-47f5-882a-55246a5eb7ad.svg'
AUTHOR = 'gpt-6'


class VerticalRectangcle(Solo48):
    icon_id = 'vertical-rectangcle'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('vertical', 'rectangcle', 'symbol')
    keyshape = Keyshape.VRECT_L

    def build(self):
        box(self,'frame',8,4,40,44,4,xs=(30,),ys=(24,))
        contacts(self)
