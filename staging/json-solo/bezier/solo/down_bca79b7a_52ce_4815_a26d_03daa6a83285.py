"""Down (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bca79b7a-52ce-4815-a26d-03daa6a83285'
SOURCE_PATH = 'icons-json/arrows/down_bca79b7a-52ce-4815-a26d-03daa6a83285.json'
AUTHOR = 'json_to_solo'

class Down(Solo48):
    icon_id = 'down'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('down', 'arrows')

    def build(self):
        self.add_line('e0', (42, 8), (6, 8))
        self.add_line('e1', (4, 11), (22, 39))
        self.add_line('e2', (26, 39), (44, 11))
        self.add_bezier('e3', (6, 8), ((5.964, 8), (5.745, 8), (5.709, 8)), ((4.773, 8), (4.018, 9.061), (4.018, 9.827)), ((4.009, 9.928), (4.009, 10.021), (4, 10.114)), ((4, 10.248), (4, 10.865), (4, 11)))
        self.add_bezier('e4', (22, 39), ((22.509, 39.362), (23.209, 39.992), (23.909, 39.992)), ((23.981, 40), (24.043, 40), (24.115, 40)), ((24.116, 40), (24.117, 40), (24.118, 40)), ((24.155, 40), (24.2, 39.992), (24.236, 39.992)), ((24.9, 39.992), (25.527, 39.328), (26, 39)))
        self.add_bezier('e5', (44, 11), ((44, 10.756), (43.982, 10.046), (43.982, 9.802)), ((43.982, 8.682), (42.9, 8.345), (42, 8)))
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e4', 'e2', 'e5', closed=True)
