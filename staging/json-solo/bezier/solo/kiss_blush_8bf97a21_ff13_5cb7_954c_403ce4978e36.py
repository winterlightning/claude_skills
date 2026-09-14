"""Kiss blush (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8bf97a21-ff13-5cb7-954c-403ce4978e36'
SOURCE_PATH = 'icons-json/smileys/kiss blush_8bf97a21-ff13-5cb7-954c-403ce4978e36.json'
AUTHOR = 'json_to_solo'

class KissBlushSmileys(Solo48):
    icon_id = 'kiss-blush-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('kiss', 'blush', 'smileys')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e1', (13, 20), ((13.155, 19.227), (13.391, 18.918), (13.918, 18.291)), ((15.473, 16.464), (18.745, 16.664), (19.918, 18.809)), ((20.2, 19.309), (19.9, 19.445), (20, 20)))
        self.add_bezier('e2', (28, 21), ((28.118, 20.436), (27.818, 20.218), (28.1, 19.7)), ((29.373, 17.382), (33.036, 16.373), (34.536, 19.055)), ((34.773, 19.491), (34.9, 19.536), (35, 20)))
        self.add_bezier('e3', (24, 27), ((24.518, 27.027), (25.009, 26.755), (25.509, 26.9)), ((26.782, 27.264), (28.191, 28.5), (27.327, 29.909)), ((26.964, 30.482), (26.518, 30.6), (26, 31)))
        self.add_bezier('e4', (24, 31), ((24.609, 31), (25.391, 31), (26, 31)))
        self.add_bezier('e5', (24, 37), ((24.609, 36.909), (25.164, 36.582), (25.736, 36.318)), ((27.127, 35.682), (28.1, 34.073), (27.218, 32.618)), ((26.891, 32.082), (26.445, 31.382), (26, 31)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
