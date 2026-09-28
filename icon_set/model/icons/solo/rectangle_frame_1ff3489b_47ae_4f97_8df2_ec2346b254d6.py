'rectangle-frame: independent smooth-curve repair.\n\nConstruction: Rounded vertical frame with equal corner radii; centered controls or a shared sidebar divider retain the original panel meaning.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/rectangle-horizontal.svg and atomic-debug/rectangle-horizontal.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '1ff3489b-47ae-4f97-8df2-ec2346b254d6'
SOURCE_PATH = 'pictographic-primitives/design/rectangle frame_1ff3489b-47ae-4f97-8df2-ec2346b254d6.svg'
AUTHOR = 'gpt-6'


class RectangleFrame(Solo48):
    icon_id = 'rectangle-frame'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('rectangle', 'frame', 'design')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'frame',4,8,44,40,4,xs=(32,),ys=(24,))
        contacts(self)
