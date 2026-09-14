"""Bell (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77ec3808-7ec4-4c77-9f4e-0bb8e7476863'
SOURCE_PATH = 'icons-json/symbol/bell_77ec3808-7ec4-4c77-9f4e-0bb8e7476863.json'
AUTHOR = 'json_to_solo'

class Bell(Solo48):
    icon_id = 'bell'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bell', 'symbol')

    def build(self):
        self.add_line('e0', (24, 38), (24, 42))
        self.add_line('e1', (6, 38), (42, 38))
        self.add_line('e2', (42, 38), (39, 34))
        self.add_line('e3', (37, 27), (37, 18))
        self.add_line('e4', (11, 19), (11, 26))
        self.add_line('e5', (9, 34), (6, 38))
        self.add_bezier('e6', (39, 34), ((37.945, 32.683), (37, 28.702), (37, 27)))
        self.add_bezier('e7', (37, 18), ((37, 17.46), (36.944, 17.111), (36.845, 16.571)), ((35.806, 10.803), (30.161, 6.008), (24.278, 6.008)), ((24.157, 6.008), (24.044, 6), (23.924, 6)), ((23.922, 6), (23.92, 6), (23.918, 6)), ((23.804, 6), (23.697, 6.008), (23.583, 6.008)), ((18.175, 6.008), (13.699, 10.14), (11.834, 14.959)), ((11.335, 16.235), (11, 17.617), (11, 19)))
        self.add_bezier('e8', (11, 26), ((11, 28.266), (10.456, 32.175), (9, 34)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e6', 'e3', 'e7', 'e4', 'e8', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
