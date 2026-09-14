"""Photo vignette (photography), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e307432-0868-448a-be7b-29a7dd769da1'
SOURCE_PATH = 'icons-json/photography/photo vignette_8e307432-0868-448a-be7b-29a7dd769da1.json'
AUTHOR = 'json_to_solo'

class PhotoVignettePhotography(Solo48):
    icon_id = 'photo-vignette-photography'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('photo', 'vignette', 'photography')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e1', (24, 13), ((24, 12.7), (24, 12.3), (24, 12)))
        self.add_bezier('e2', (24, 35), ((24, 34.7), (24, 34.3), (24, 34)))
        self.add_bezier('e3', (15, 19), ((15, 18.7), (15, 18.3), (15, 18)))
        self.add_bezier('e4', (33, 19), ((33, 18.7), (33, 18.3), (33, 18)))
        self.add_bezier('e5', (15, 29), ((15, 28.7), (15, 28.3), (15, 28)))
        self.add_bezier('e6', (33, 29), ((33, 28.7), (33, 28.3), (33, 28)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
