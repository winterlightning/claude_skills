'hexagon-shape: independent smooth-curve repair.\n\nConstruction: Regular mirrored hexagon; six deliberate corners preserve its geometric identity.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/hexagon.svg and atomic-debug/hexagon.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '392ff95c-1214-470d-870f-2dc6d3f7f1c3'
SOURCE_PATH = 'pictographic-primitives/design/hexagon shape_392ff95c-1214-470d-870f-2dc6d3f7f1c3.svg'
AUTHOR = 'gpt-6'


class HexagonShape(Solo48):
    icon_id = 'hexagon-shape'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('hexagon', 'shape', 'design')
    keyshape = Keyshape.VRECT_L

    def build(self):
        poly(self,'hexagon',(24,4),(40,14),(40,34),(24,44),(8,34),(8,14),closed=True)
        contacts(self)
