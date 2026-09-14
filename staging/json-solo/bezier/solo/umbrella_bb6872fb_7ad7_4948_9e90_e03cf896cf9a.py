"""Batch-02/umbrella (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb6872fb-7ad7-4948-9e90-e03cf896cf9a'
SOURCE_PATH = 'icons-json/accessories/batch-02/umbrella_bb6872fb-7ad7-4948-9e90-e03cf896cf9a.json'
AUTHOR = 'json_to_solo'

class Batch02Umbrella(Solo48):
    icon_id = 'batch-02-umbrella'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'umbrella', 'accessories')

    def build(self):
        self.add_line('e0', (24, 37), (24, 24))
        self.add_line('e1', (8, 24), (40, 24))
        self.add_line('e2', (24, 4), (24, 8))
        self.add_bezier('e3', (16, 40), ((16.463, 42.091), (18.156, 44), (20.278, 44)), ((20.289, 44), (20.3, 44), (20.311, 44)), ((21.016, 44), (21.727, 43.702), (22.299, 43.282)), ((24.328, 41.791), (24, 39.336), (24, 37)))
        self.add_bezier('e4', (40, 24), ((40, 23.855), (39.992, 23.709), (39.992, 23.573)), ((39.992, 22.391), (39.697, 21.136), (39.385, 20.009)), ((37.432, 13.045), (30.813, 7.482), (24, 7.636)), ((17.364, 7.791), (10.973, 12.482), (8.8, 19.336)), ((8.379, 20.655), (8.017, 22.155), (8.017, 23.564)), ((8.008, 23.709), (8.008, 23.855), (8, 24)))
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e1', 'e4')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c1')
