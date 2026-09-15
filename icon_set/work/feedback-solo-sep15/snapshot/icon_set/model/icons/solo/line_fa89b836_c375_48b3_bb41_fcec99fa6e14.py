"""Line (diagrams), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; a diagonal line reaches all four envelope edges."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa89b836-c375-48b3-bb41-fcec99fa6e14'
SOURCE_PATH = 'pictographic-primitives/diagrams/line_fa89b836-c375-48b3-bb41-fcec99fa6e14.svg'
AUTHOR = 'gpt-6'

class LineDiagrams(Solo48):
    icon_id = 'line-diagrams'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('line', 'diagrams')

    def build(self):
        self.add_line('e0', (8, 44), (40, 4))
        self.add_contour('c0', 'e0')
