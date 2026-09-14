"""Upload (emails), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '150ba06d-d7fc-447d-a794-a611c860309d'
SOURCE_PATH = 'icons-json/emails/upload_150ba06d-d7fc-447d-a794-a611c860309d.json'
AUTHOR = 'json_to_solo'

class Upload(Solo48):
    icon_id = 'upload'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('upload', 'emails')

    def build(self):
        self.add_line('sym-e0', (24, 6), (24, 33))
        self.add_line('sym-e1', (14, 16), (24, 6))
        self.add_line('sym-e2', (24, 6), (34, 16))
        self.add_line('sym-e3', (6, 33), (6, 34))
        self.add_line('sym-e4-1', (6, 34), (6, 38))
        self.add_arc('sym-e4-2', (6, 38), (8, 41), radius_x=5, sweep=False)
        self.add_line('sym-e5', (8, 41), (10, 42))
        self.add_line('sym-e6', (10, 42), (24, 42))
        self.add_line('sym-e7', (24, 42), (38, 42))
        self.add_line('sym-e8', (38, 42), (40, 41))
        self.add_line('sym-e9-1', (40, 41), (42, 38))
        self.add_arc('sym-e9-2', (42, 38), (42, 34), radius_x=19)
        self.add_line('sym-e10', (42, 34), (42, 33))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4-1', 'sym-e4-2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9-1', 'sym-e9-2', 'sym-e10')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
