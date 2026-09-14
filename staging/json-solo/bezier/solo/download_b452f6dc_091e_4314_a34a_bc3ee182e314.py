"""Download (emails), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b452f6dc-091e-4314-a34a-bc3ee182e314'
SOURCE_PATH = 'icons-json/emails/download_b452f6dc-091e-4314-a34a-bc3ee182e314.json'
AUTHOR = 'json_to_solo'

class Download(Solo48):
    icon_id = 'download'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('download', 'emails')

    def build(self):
        self.add_line('sym-e0', (24, 4), (24, 31))
        self.add_line('sym-e1', (24, 31), (32, 22))
        self.add_line('sym-e2', (24, 44), (37, 44))
        self.add_bezier('sym-e3', (37, 44), ((37.042, 43.991), (36.958, 44), (37, 44)))
        self.add_bezier('sym-e4', (37, 44), ((38.836, 44), (40, 41.836), (40, 40)))
        self.add_bezier('sym-e5', (40, 40), ((40, 39.818), (40, 40.182), (40, 40)))
        self.add_bezier('sym-e6', (40, 40), ((40, 39.982), (40, 39.018), (40, 39)))
        self.add_line('sym-e7', (24, 31), (16, 22))
        self.add_line('sym-e8', (24, 44), (11, 44))
        self.add_bezier('sym-e9', (11, 44), ((10.958, 43.991), (11.042, 44), (11, 44)))
        self.add_bezier('sym-e10', (11, 44), ((9.164, 44), (8, 41.836), (8, 40)))
        self.add_bezier('sym-e11', (8, 40), ((8, 39.818), (8, 40.182), (8, 40)))
        self.add_bezier('sym-e12', (8, 40), ((8, 39.982), (8, 39.018), (8, 39)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7')
        self.add_contour('sym-c3', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
