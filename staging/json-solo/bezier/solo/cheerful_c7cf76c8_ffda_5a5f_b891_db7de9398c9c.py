"""Cheerful (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c7cf76c8-ffda-5a5f-b891-db7de9398c9c'
SOURCE_PATH = 'icons-json/smileys/cheerful_c7cf76c8-ffda-5a5f-b891-db7de9398c9c.json'
AUTHOR = 'json_to_solo'

class CheerfulSmileys(Solo48):
    icon_id = 'cheerful-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('cheerful', 'smileys')

    def build(self):
        self.add_line('e0', (14, 27), (19, 28))
        self.add_arc('e1-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e1-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e2', (34, 27), ((33.709, 27.582), (33.3, 27.918), (33.091, 28.545)), ((32.573, 30.109), (32.009, 31.645), (30.836, 32.873)), ((26.018, 37.9), (18.127, 36.227), (14.991, 30.2)), ((14.427, 29.109), (14.209, 28.191), (14, 27)))
        self.add_bezier('e3', (19, 28), ((21.891, 28.482), (26.336, 27.8), (29.264, 27.427)), ((30.282, 27.291), (31.3, 27.145), (32.318, 26.991)), ((32.709, 26.927), (33.109, 26.873), (33.5, 26.809)), ((33.791, 26.764), (34, 26.727), (34, 26.727)), ((33.7, 27.336), (33.3, 28.391), (33, 29)))
        self.add_bezier('e4', (13, 19), ((13.127, 18.309), (13.309, 18.173), (13.727, 17.582)), ((15.291, 15.409), (18.8, 15.7), (20, 18.091)), ((20.227, 18.536), (19.9, 18.518), (20, 19)))
        self.add_bezier('e5', (28, 19), ((28.082, 18.518), (27.745, 17.627), (27.964, 17.173)), ((29.127, 14.727), (32.718, 14.491), (34.273, 16.664)), ((34.7, 17.264), (34.873, 18.3), (35, 19)))
        self.add_contour('c0', 'e2', 'e0', 'e3')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e5')
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
