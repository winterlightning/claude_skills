"""Arrow rectangle left (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b8a720f-0633-555e-8c23-fb7b13dda012'
SOURCE_PATH = 'icons-json/arrows/arrow rectangle left_6b8a720f-0633-555e-8c23-fb7b13dda012.json'
AUTHOR = 'json_to_solo'

class ArrowRectangleLeft6b8a720f(Solo48):
    icon_id = 'arrow-rectangle-left-6b8a720f'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'rectangle', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (26, 16), (18, 24))
        self.add_line('e1', (18, 24), (26, 33))
        self.add_line('e2', (35, 42), (13, 42))
        self.add_line('e3', (6, 33), (6, 13))
        self.add_line('e4', (15, 6), (37, 6))
        self.add_line('e5', (42, 13), (42, 38))
        self.add_bezier('e6', (13, 42), ((12.869, 42), (12.292, 41.992), (12.161, 41.992)), ((8.913, 41.992), (6.016, 39.136), (6.016, 35.88)), ((6.016, 35.062), (6, 34.244), (6, 33.425)), ((6, 33.286), (6, 33.139), (6, 33)))
        self.add_bezier('e7', (6, 13), ((6, 12.853), (6.016, 12.259), (6.016, 12.112)), ((6.016, 9.117), (8.577, 6.753), (11.335, 6.115)), ((11.875, 6), (12.48, 6.016), (13.02, 6.016)), ((13.544, 6.016), (14.067, 6), (14.583, 6)), ((14.722, 6), (14.861, 6), (15, 6)))
        self.add_bezier('e8', (37, 6), ((37.131, 6), (37.345, 6.008), (37.475, 6.008)), ((39.619, 6.008), (41.378, 7.89), (41.853, 9.878)), ((41.992, 10.459), (41.992, 11.155), (41.992, 11.76)), ((41.992, 11.932), (42, 12.104), (42, 12.267)), ((42, 12.365), (42, 12.91), (42, 13)))
        self.add_bezier('e9', (42, 38), ((41.992, 38.131), (41.992, 38.171), (41.984, 38.302)), ((41.984, 40.077), (40.331, 41.984), (38.515, 41.984)), ((37.901, 41.984), (37.295, 42), (36.69, 42)), ((36.003, 42), (35.679, 42), (35, 42)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e6', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', closed=True)
