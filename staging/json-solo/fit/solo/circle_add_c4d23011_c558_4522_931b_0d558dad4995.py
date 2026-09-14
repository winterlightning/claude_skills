"""Circle add (other), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c4d23011-c558-4522-931b-0d558dad4995'
SOURCE_PATH = 'icons-json/other/circle add_c4d23011-c558-4522-931b-0d558dad4995.json'
AUTHOR = 'json_to_solo'

class CircleAddOther(Solo48):
    icon_id = 'circle-add-other'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('circle', 'add', 'other')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_line('sym-e2', (24, 24), (24, 34))
        self.add_line('sym-e3', (14, 24), (24, 24))
        self.add_line('sym-e4', (24, 24), (34, 24))
        self.add_line('sym-e5', (24, 14), (24, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c3', 'sym-e5')
        self.relate('connect', 'sym-c1', 'sym-c2', 'sym-c3')
