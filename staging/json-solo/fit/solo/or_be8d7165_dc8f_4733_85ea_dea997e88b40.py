"""Or (religion), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be8d7165-dc8f-4733-85ea-dea997e88b40'
SOURCE_PATH = 'icons-json/religion/or_be8d7165-dc8f-4733-85ea-dea997e88b40.json'
AUTHOR = 'json_to_solo'

class OrBe8d7165(Solo48):
    icon_id = 'or-be8d7165'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'religion'
    aliases = ()
    keywords = ('or', 'religion')

    def build(self):
        self.add_line('e0', (44, 24), (24, 24))
        self.add_line('e1', (24, 44), (24, 24))
        self.add_line('e2', (4, 24), (24, 24))
        self.add_line('e3', (24, 4), (24, 24))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c2', 'e4')
        self.relate('connect', 'c3', 'e4')
