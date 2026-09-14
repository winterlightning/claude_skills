"""File paper document (files), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94195673-5dbd-5579-91d7-d7c5ee83aa98'
SOURCE_PATH = 'icons-json/files/file paper document_94195673-5dbd-5579-91d7-d7c5ee83aa98.json'
AUTHOR = 'json_to_solo'

class FilePaperDocumentFiles(Solo48):
    icon_id = 'file-paper-document-files'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'files'
    aliases = ()
    keywords = ('file', 'paper', 'document', 'files')

    def build(self):
        self.add_line('e0', (40, 15), (29, 4))
        self.add_line('e1', (40, 15), (40, 41))
        self.add_line('e2', (37, 44), (11, 44))
        self.add_line('e3', (8, 41), (8, 6))
        self.add_line('e4', (10, 4), (29, 4))
        self.add_line('e5', (29, 4), (29, 11))
        self.add_line('e6', (32, 15), (40, 15))
        self.add_bezier('e7', (40, 41), ((40, 41.2), (39.992, 41.682), (39.992, 41.882)), ((39.992, 43.1), (38.964, 43.991), (37.861, 43.991)), ((37.794, 43.991), (37.726, 44), (37.667, 44)), ((37.6, 44), (37.067, 44), (37, 44)))
        self.add_bezier('e8', (11, 44), ((10.798, 44), (10.964, 43.991), (10.771, 43.991)), ((10.627, 43.991), (10.493, 43.991), (10.358, 43.982)), ((9.347, 43.982), (8.008, 42.836), (8.008, 41.682)), ((8.008, 41.609), (8, 41.545), (8, 41.473)), ((8, 41.409), (8, 41.064), (8, 41)))
        self.add_bezier('e9', (8, 6), ((8.531, 4.764), (8.872, 4.609), (10, 4)))
        self.add_bezier('e10', (29, 11), ((29, 11.355), (28.985, 11.945), (29.061, 12.309)), ((29.381, 13.955), (30.543, 15), (32, 15)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7', 'e2', 'e8', 'e3', 'e9', 'e4', 'e5', 'e10', 'e6', closed=True)
        self.relate('connect', 'c0', 'c1')
