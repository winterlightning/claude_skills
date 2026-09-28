"""hexagon-shape-design: approved original model.

Construction: Hexagonal design divided into three geometric faces by exact shared center spokes.
Keyshape: VRECT_L; exact SOLO48 envelope.
Construction reference: hexagon from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
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
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('hexagon', 'shape', 'design')
    keyshape = Keyshape.VRECT_L

    def build(self):
        poly(self, 'hexagon', (24, 4), (40, 14), (40, 34), (24, 44), (8, 34), (8, 14), closed=True)
        for i, p in enumerate(((24, 4), (8, 34), (40, 34))):
            line(self, f'spoke-{i}', (24, 24), p)
        contacts(self)
