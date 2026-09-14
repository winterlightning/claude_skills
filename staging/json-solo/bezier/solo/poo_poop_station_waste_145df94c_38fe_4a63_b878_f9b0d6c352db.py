"""Poo poop station waste (babies), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '145df94c-38fe-4a63-b878-f9b0d6c352db'
SOURCE_PATH = 'icons-json/babies/poo poop station waste_145df94c-38fe-4a63-b878-f9b0d6c352db.json'
AUTHOR = 'json_to_solo'

class PooPoopStationWaste(Solo48):
    icon_id = 'poo-poop-station-waste'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    aliases = ()
    keywords = ('poo', 'poop', 'station', 'waste', 'babies')

    def build(self):
        self.add_line('e0', (19, 18), (18, 16))
        self.add_line('e1', (18, 16), (18, 14))
        self.add_line('e2', (18, 14), (20, 11))
        self.add_line('e3', (27, 19), (26, 17))
        self.add_line('e4', (42, 42), (37, 42))
        self.add_line('e5', (11, 42), (6, 42))
        self.add_line('e6', (6, 42), (6, 34))
        self.add_line('e7', (19, 28), (28, 28))
        self.add_line('e8', (35, 22), (37, 14))
        self.add_bezier('e9', (20, 11), ((20.794, 9.413), (19.794, 7.391), (19, 6)))
        self.add_bezier('e10', (26, 17), ((26.033, 16.403), (26.512, 16.309), (26.716, 15.736)), ((26.905, 15.213), (27.215, 14.779), (27.502, 14.296)), ((28.336, 12.889), (28.401, 11.571), (28, 10)))
        self.add_bezier('e11', (37, 42), ((36.877, 41.926), (36.78, 41.951), (36.649, 41.861)), ((36.215, 41.566), (35.365, 40.331), (34.89, 39.873)), ((33.916, 38.899), (32.746, 38.081), (31.527, 37.451)), ((26.487, 34.833), (20.097, 34.98), (15.286, 38.056)), ((13.519, 39.177), (12.456, 40.617), (11, 42)))
        self.add_bezier('e12', (6, 34), ((6, 33.91), (6.016, 33.646), (6.016, 33.556)), ((6.016, 32.624), (6.27, 31.715), (6.45, 30.807)), ((6.925, 28.443), (7.653, 26.127), (8.594, 23.902)), ((9.076, 22.756), (9.919, 20.915), (11.474, 21.57)), ((12.668, 22.077), (12.873, 23.55), (13.495, 24.556)), ((14.656, 26.438), (16.66, 28), (19, 28)))
        self.add_bezier('e13', (28, 28), ((30.765, 28), (34.444, 24.774), (35, 22)))
        self.add_bezier('e14', (37, 14), ((37.164, 13.885), (37.295, 13.904), (37.516, 13.805)), ((40.077, 12.652), (40.527, 17.602), (40.805, 19.165)), ((41.468, 22.961), (41.55, 26.872), (41.722, 30.709)), ((41.853, 33.524), (41.992, 36.355), (41.992, 39.177)), ((41.992, 39.545), (42, 39.905), (42, 40.274)), ((42, 40.846), (42, 41.427), (42, 42)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e9')
        self.add_contour('c1', 'e3', 'e10')
        self.add_contour('c2', 'e4', 'e11', 'e5', 'e6', 'e12', 'e7', 'e13', 'e8', 'e14', closed=True)
