"""Upload (emails), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '150ba06d-d7fc-447d-a794-a611c860309d'
SOURCE_PATH = 'icons-json/emails/upload_150ba06d-d7fc-447d-a794-a611c860309d.json'
AUTHOR = 'json_to_solo'

class UploadEmails(Solo48):
    icon_id = 'upload-emails'
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
        self.add_bezier('sym-e3', (6, 33), ((6, 33.434), (6, 33.566), (6, 34)))
        self.add_bezier('sym-e4', (6, 34), ((6, 36.495), (6, 39.437), (8, 41)))
        self.add_bezier('sym-e5', (8, 41), ((8.532, 41.36), (9.345, 42), (10, 42)))
        self.add_line('sym-e6', (10, 42), (24, 42))
        self.add_line('sym-e7', (24, 42), (38, 42))
        self.add_bezier('sym-e8', (38, 42), ((38.655, 42), (39.468, 41.36), (40, 41)))
        self.add_bezier('sym-e9', (40, 41), ((42, 39.437), (42, 36.495), (42, 34)))
        self.add_bezier('sym-e10', (42, 34), ((42, 33.566), (42, 33.434), (42, 33)))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
