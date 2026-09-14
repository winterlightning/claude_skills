"""Heart (romance), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b74d773d-2544-4971-935a-c2f6b85abdcb'
SOURCE_PATH = 'icons-json/romance/heart_b74d773d-2544-4971-935a-c2f6b85abdcb.json'
AUTHOR = 'json_to_solo'

class Heart(Solo48):
    icon_id = 'heart'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    aliases = ()
    keywords = ('heart', 'romance')

    def build(self):
        self.add_line('e0', (22, 38), (7, 24))
        self.add_line('e1', (22, 11), (24, 13))
        self.add_line('e2', (41, 24), (24, 40))
        self.add_line('e3', (24, 40), (22, 38))
        self.add_bezier('e4', (7, 24), ((5.327, 22.451), (4, 20.076), (4, 17.886)), ((4, 17.883), (4, 17.88), (4, 17.877)), ((4, 17.678), (4, 17.488), (4, 17.297)), ((4, 12.547), (8.355, 8), (13.609, 8)), ((13.612, 8), (13.616, 8), (13.619, 8)), ((13.824, 8), (14.021, 8), (14.218, 8)), ((17.391, 8), (19.818, 8.962), (22, 11)))
        self.add_bezier('e5', (24, 13), ((26.736, 10.432), (29.418, 8), (33.609, 8)), ((33.818, 8), (34.027, 8), (34.236, 8)), ((39.364, 8), (44, 12.387), (44, 17.103)), ((44, 17.106), (44, 17.11), (44, 17.113)), ((44, 17.32), (43.991, 17.519), (43.991, 17.726)), ((43.991, 19.848), (42.618, 22.501), (41, 24)))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5', 'e2', 'e3', closed=True)
