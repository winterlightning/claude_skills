"""Archive (content), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d3380f1-04ae-52fb-a0b2-916fda7e3f13'
SOURCE_PATH = 'icons-json/content/archive_4d3380f1-04ae-52fb-a0b2-916fda7e3f13.json'
AUTHOR = 'json_to_solo'

class Archive(Solo48):
    icon_id = 'archive'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('archive', 'content')

    def build(self):
        self.add_line('sym-e0', (24, 24), (29, 24))
        self.add_line('sym-e1', (24, 40), (39, 40))
        self.add_line('sym-e2', (39, 40), (40, 40))
        self.add_line('sym-e3', (40, 40), (41, 37))
        self.add_line('sym-e4', (41, 37), (41, 16))
        self.add_arc('sym-e6', (41, 16), (42, 16), radius_x=62)
        self.add_arc('sym-e7', (42, 16), (44, 16), radius_x=2, sweep=False)
        self.add_line('sym-e9', (44, 16), (44, 11))
        self.add_arc('sym-e10', (44, 11), (44, 10), radius_x=23)
        self.add_line('sym-e11', (44, 10), (41, 8))
        self.add_line('sym-e12', (41, 8), (24, 8))
        self.add_line('sym-e13', (24, 8), (7, 8))
        self.add_line('sym-e14', (7, 8), (4, 10))
        self.add_line('sym-e15', (4, 10), (4, 11))
        self.add_line('sym-e16', (4, 11), (4, 16))
        self.add_arc('sym-e18', (4, 16), (6, 16), radius_x=2, sweep=False)
        self.add_arc('sym-e19', (6, 16), (7, 16), radius_x=10)
        self.add_line('sym-e21', (7, 16), (7, 37))
        self.add_line('sym-e22', (7, 37), (8, 40))
        self.add_line('sym-e23', (8, 40), (9, 40))
        self.add_line('sym-e24', (9, 40), (24, 40))
        self.add_line('sym-e26', (41, 16), (39, 16))
        self.add_line('sym-e27', (39, 16), (24, 16))
        self.add_line('sym-e28', (24, 16), (9, 16))
        self.add_line('sym-e29', (9, 16), (7, 16))
        self.add_line('sym-e31', (24, 24), (19, 24))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e19', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', closed=True)
        self.add_contour('sym-c2', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29')
        self.add_contour('sym-c3', 'sym-e31')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
