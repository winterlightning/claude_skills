"""Amazon web services logo (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '671a6600-cf66-4590-9e43-48121888537b'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/amazon web services logo_671a6600-cf66-4590-9e43-48121888537b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class AmazonWebServicesLogo(Solo48):
    icon_id = 'amazon-web-services-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('amazon', 'web', 'services', 'logo', '_uncategorized_03')

    def build(self):
        self.add_line('e0', (42, 12), (42, 35))
        self.add_line('e1', (42, 35), (24, 42))
        self.add_line('e2', (42, 12), (24, 6))
        self.add_line('e3', (24, 6), (6, 12))
        self.add_line('e4', (42, 12), (24, 18))
        self.add_line('e5', (24, 42), (24, 18))
        self.add_line('e6', (24, 42), (6, 35))
        self.add_line('e7', (6, 35), (6, 12))
        self.add_line('e8', (24, 18), (6, 12))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6', 'e7')
        self.add_contour('c5', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c5')
