'hexagon-shape: distinct review variant.\n\nConstruction: Flat-top hexagon with equal sloping shoulders, distinct from the point-top hexagon.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nConstruction reference: hexagon from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '392ff95c-1214-470d-870f-2dc6d3f7f1c3'
SOURCE_PATH = 'pictographic-primitives/design/hexagon shape_392ff95c-1214-470d-870f-2dc6d3f7f1c3.svg'
AUTHOR = 'gpt-6'


class HexagonShapeVariant2(Solo48):
    icon_id = 'hexagon-shape-v2'
    variant_of = 'hexagon-shape'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('hexagon', 'shape', 'design')
    keyshape = Keyshape.VRECT_L

    def build(self):
        poly(self,'hexagon',(16,4),(32,4),(40,24),(32,44),(16,44),(8,24),closed=True)
        contacts(self)
