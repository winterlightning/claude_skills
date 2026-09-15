'rectangle-shape: independent smooth-curve repair.\n\nConstruction: Rounded vertical frame with equal corner radii; centered controls or a shared sidebar divider retain the original panel meaning.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/rectangle-horizontal.svg and atomic-debug/rectangle-horizontal.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '432b99ac-4502-55ae-b924-896645c9c530'
SOURCE_PATH = 'pictographic-primitives/design/rectangle shape_432b99ac-4502-55ae-b924-896645c9c530.svg'
AUTHOR = 'gpt-6'


class RectangleShapeVariant2(Solo48):
    icon_id = 'rectangle-shape-v2'
    variant_of = 'rectangle-shape'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('rectangle', 'shape', 'design')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'frame',4,8,44,40,4,xs=(32,),ys=(24,))
        contacts(self)
