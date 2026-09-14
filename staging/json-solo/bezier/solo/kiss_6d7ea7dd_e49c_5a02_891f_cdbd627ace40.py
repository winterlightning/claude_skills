"""Kiss (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6d7ea7dd-e49c-5a02-891f-cdbd627ace40'
SOURCE_PATH = 'icons-json/smileys/kiss_6d7ea7dd-e49c-5a02-891f-cdbd627ace40.json'
AUTHOR = 'json_to_solo'

class Kiss6d7ea7dd(Solo48):
    icon_id = 'kiss-6d7ea7dd'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('kiss', 'smileys')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e1', (25, 28), ((26.855, 28.127), (29.245, 28.227), (28.4, 30.818)), ((28.236, 31.291), (28.245, 31.573), (28, 32)))
        self.add_bezier('e2', (28, 32), ((29.282, 33.355), (29.145, 34.882), (27.136, 35.609)), ((26.464, 35.845), (25.7, 35.964), (25, 36)))
        self.add_bezier('e3', (28, 32), ((27.7, 32), (27.3, 32), (27, 32)))
        self.add_bezier('e4', (12, 20), ((14.264, 17.545), (16.736, 17.545), (19, 20)))
        self.add_bezier('e5', (29, 20), ((31.282, 17.509), (33.736, 17.464), (36, 20)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
