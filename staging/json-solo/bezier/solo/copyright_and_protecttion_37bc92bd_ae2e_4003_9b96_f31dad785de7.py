"""Copyright and protecttion (content), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '37bc92bd-ae2e-4003-9b96-f31dad785de7'
SOURCE_PATH = 'icons-json/content/copyright and protecttion_37bc92bd-ae2e-4003-9b96-f31dad785de7.json'
AUTHOR = 'json_to_solo'

class CopyrightAndProtecttionContent(Solo48):
    icon_id = 'copyright-and-protecttion-content'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('copyright', 'and', 'protecttion', 'content')

    def build(self):
        self.add_line('e0', (19, 34), (19, 24))
        self.add_line('e1', (30, 34), (26, 24))
        self.add_line('e2', (26, 24), (19, 24))
        self.add_line('e3', (26, 14), (19, 14))
        self.add_line('e4', (19, 14), (19, 24))
        self.add_arc('e5-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e5-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e6', (27, 24), ((27.891, 23.782), (28.436, 23.536), (29.155, 22.936)), ((32.118, 20.5), (31.018, 15.645), (27.518, 14.382)), ((26.991, 14.191), (26.564, 14), (26, 14)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e6', 'e3', 'e4')
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
