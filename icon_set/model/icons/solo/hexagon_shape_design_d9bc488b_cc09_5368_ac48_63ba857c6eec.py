'hexagon-shape-design: independent smooth-curve repair.\n\nConstruction: Regular mirrored hexagon; six deliberate corners preserve its geometric identity.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/hexagon.svg and atomic-debug/hexagon.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'd9bc488b-cc09-5368-ac48-63ba857c6eec'
SOURCE_PATH = 'pictographic-primitives/design/hexagon shape_d9bc488b-cc09-5368-ac48-63ba857c6eec.svg'
AUTHOR = 'gpt-6'


class HexagonShapeDesign(Solo48):
    icon_id = 'hexagon-shape-design'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('hexagon', 'shape', 'design')
    keyshape = Keyshape.VRECT_L

    def build(self):
        poly(self,'hexagon',(24,4),(40,14),(40,34),(24,44),(8,34),(8,14),closed=True)
        contacts(self)
