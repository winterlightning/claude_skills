"""Nauseous (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd8d61638-d143-5e45-ab87-0388fc66f071'
SOURCE_PATH = 'icons-json/smileys/nauseous_d8d61638-d143-5e45-ab87-0388fc66f071.json'
AUTHOR = 'json_to_solo'

class NauseousD8d61638(Solo48):
    icon_id = 'nauseous-d8d61638'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('nauseous', 'smileys')

    def build(self):
        self.add_line('e0', (35, 35), (33, 32))
        self.add_arc('e1-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e1-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e2', (13, 25), ((13.218, 24.6), (13.482, 24.045), (13.809, 23.709)), ((14.827, 22.655), (16.718, 22.173), (18.045, 22.864)), ((18.591, 23.145), (18.555, 23.591), (19, 24)))
        self.add_bezier('e3', (29, 24), ((30.491, 22.955), (32.745, 21.991), (34.418, 23.309)), ((34.655, 23.491), (34.818, 23.782), (35, 24)))
        self.add_bezier('e4', (33, 32), ((32.645, 31.873), (32.436, 31.827), (32.045, 31.8)), ((30.273, 31.682), (29.764, 34.436), (27.455, 34.427)), ((25.955, 34.418), (25.873, 32.173), (24.318, 31.991)), ((22.173, 31.736), (21.891, 34.418), (20.145, 34.609)), ((18.245, 34.818), (17.255, 32.018), (16.282, 31.891)), ((15.218, 31.755), (13.609, 33.282), (13, 34)))
        self.add_bezier('e5', (29, 14), ((28.745, 13.927), (28.955, 13.845), (28.7, 13.773)), ((28.755, 13.9), (28.809, 14.027), (28.873, 14.155)), ((28.991, 14.391), (29.127, 14.636), (29.273, 14.864)), ((29.691, 15.509), (30.218, 16.091), (30.836, 16.564)), ((32.327, 17.691), (34.2, 18.209), (36, 18)))
        self.add_bezier('e6', (12, 18), ((14.691, 18.355), (17, 17.936), (19, 16)))
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e0', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
