'rectangle-two-dots: independent smooth-curve repair.\n\nConstruction: Rounded vertical frame with equal corner radii; centered controls or a shared sidebar divider retain the original panel meaning.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/rectangle-horizontal.svg and atomic-debug/rectangle-horizontal.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'b499c107-a18c-412b-a0f2-7df8766d8257'
SOURCE_PATH = 'pictographic-primitives/state/rectangle two dots_b499c107-a18c-412b-a0f2-7df8766d8257.svg'
AUTHOR = 'gpt-6'


class RectangleTwoDots(Solo48):
    icon_id = 'rectangle-two-dots'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('rectangle', 'two', 'dots', 'state')
    keyshape = Keyshape.VRECT_L

    def build(self):
        box(self,'frame',8,4,40,44,4,xs=(30,),ys=(24,))
        self.add_dot("top-dot",(24,16))
        self.add_dot("bottom-dot",(24,32))
        contacts(self)
