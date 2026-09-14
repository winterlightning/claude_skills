"""Blushing (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '488475b1-7c72-5f21-ba4a-76116df6b100'
SOURCE_PATH = 'icons-json/smileys/blushing_488475b1-7c72-5f21-ba4a-76116df6b100.json'
AUTHOR = 'json_to_solo'

class BlushingSmileys(Solo48):
    icon_id = 'blushing-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('blushing', 'smileys')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e1', (13, 20), ((13.145, 19.382), (13.318, 19.209), (13.7, 18.673)), ((15.209, 16.545), (18.664, 16.736), (19.945, 19.009)), ((20.191, 19.455), (19.882, 19.518), (20, 20)))
        self.add_bezier('e2', (28, 21), ((28.145, 20.364), (27.882, 20.082), (28.255, 19.518)), ((29.591, 17.491), (33.064, 16.664), (34.491, 19.055)), ((34.745, 19.482), (34.882, 19.536), (35, 20)))
        self.add_bezier('e3', (15, 29), ((18.945, 36.645), (29.073, 36.673), (33, 29)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
