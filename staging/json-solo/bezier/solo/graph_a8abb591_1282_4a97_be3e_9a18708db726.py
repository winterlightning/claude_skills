"""Graph (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8abb591-1282-4a97-be3e-9a18708db726'
SOURCE_PATH = 'icons-json/arrows/graph_a8abb591-1282-4a97-be3e-9a18708db726.json'
AUTHOR = 'json_to_solo'

class GraphArrows(Solo48):
    icon_id = 'graph-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('graph', 'arrows')

    def build(self):
        self.add_line('e0', (36, 8), (44, 8))
        self.add_line('e1', (44, 8), (25, 31))
        self.add_line('e2', (25, 31), (18, 23))
        self.add_line('e3', (18, 23), (4, 40))
        self.add_line('e4', (44, 8), (44, 18))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e4')
        self.relate('connect', 'c0', 'c1')
