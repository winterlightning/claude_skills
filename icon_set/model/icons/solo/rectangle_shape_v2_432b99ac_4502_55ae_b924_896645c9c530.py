'rectangle-shape: distinct review variant.\n\nConstruction: Rounded rectangle with broad eight-unit corner arcs; distinguish it from both the tighter frame and the capsule.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nConstruction reference: rectangle-horizontal from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '432b99ac-4502-55ae-b924-896645c9c530'
SOURCE_PATH = 'pictographic-primitives/design/rectangle shape_432b99ac-4502-55ae-b924-896645c9c530.svg'
AUTHOR = 'gpt-6'


class RectangleShapeVariant2(Solo48):
    icon_id = 'rectangle-shape-v2'
    variant_of = 'rectangle-shape'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('rectangle', 'shape', 'design')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'frame',4,8,44,40,8)
        contacts(self)
