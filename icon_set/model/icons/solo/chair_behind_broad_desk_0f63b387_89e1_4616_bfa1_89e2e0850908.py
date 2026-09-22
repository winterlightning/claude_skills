"""Chair behind desk is one furniture scene. HRECT_L retains broad tabletop. Shared x=24 symmetry and back radius. Actual reference gives raised rounded back, tabletop and lower chair legs; Lucide table is a data grid and supplies no useful furniture geometry. Omit thin tabletop bevel and seat thickness."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '0f63b387-89e1-4616-bfa1-89e2e0850908'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_10/chair table 1_0f63b387-89e1-4616-bfa1-89e2e0850908.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'chair-behind-broad-desk'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ['Chair behind Broad Desk']
    keywords = ['desk', 'chair', 'furniture', 'office', 'table', 'seat', 'workspace']
    def build(self):
        self.add_polyline("desk",(4,40),(4,25),(44,25),(44,40))
        self.add_arc("chair-back",(16,16),(32,16),radius_x=8)
        self.add_polyline("chair-seat",(16,40),(16,33),(32,33),(32,40))
