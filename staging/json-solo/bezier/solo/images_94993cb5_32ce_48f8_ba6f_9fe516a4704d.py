"""Images (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94993cb5-32ce-48f8-ba6f-9fe516a4704d'
SOURCE_PATH = 'icons-json/state/images_94993cb5-32ce-48f8-ba6f-9fe516a4704d.json'
AUTHOR = 'json_to_solo'

class ImagesState(Solo48):
    icon_id = 'images-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('images', 'state')

    def build(self):
        self.add_line('e0', (44, 33), (34, 22))
        self.add_line('e1', (27, 23), (11, 40))
        self.add_line('e2', (44, 30), (44, 40))
        self.add_line('e3', (44, 40), (4, 40))
        self.add_line('e4', (4, 40), (4, 8))
        self.add_line('e5', (4, 8), (44, 8))
        self.add_line('e6', (44, 8), (44, 30))
        self.add_bezier('e7', (34, 22), ((32.491, 20.34), (30.6, 19.32), (28.636, 20.89)), ((27.936, 21.45), (27.618, 22.32), (27, 23)))
        self.add_dot('e8', (13, 19))
        self.add_contour('c0', 'e0', 'e7', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4', 'e5', 'e6', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
