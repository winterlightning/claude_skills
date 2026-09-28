"""Side road left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b971eedf-9af0-4383-8315-76ad26cf72c9'
SOURCE_PATH = 'pictographic-primitives/arrows/side road left_b971eedf-9af0-4383-8315-76ad26cf72c9.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class SideRoadLeft(Solo48):
    icon_id = 'side-road-left'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('side', 'road', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (8, 11), (24, 4))
        self.add_line('e1', (24, 44), (24, 4))
        self.add_line('e2', (40, 11), (24, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
