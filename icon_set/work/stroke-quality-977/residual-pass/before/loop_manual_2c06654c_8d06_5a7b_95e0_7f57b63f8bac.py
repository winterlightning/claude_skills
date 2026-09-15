"""Loop manual (diagrams), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c06654c-8d06-5a7b-95e0-7f57b63f8bac'
SOURCE_PATH = 'pictographic-primitives/diagrams/loop manual_2c06654c-8d06-5a7b-95e0-7f57b63f8bac.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class LoopManual(Solo48):
    icon_id = 'loop-manual'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('loop', 'manual', 'diagrams')

    def build(self):
        self.add_line('e0', (22, 29), (27, 16))
        self.add_bezier('e1', (21, 16), ((18.909, 12.24), (17.009, 8.016), (13.745, 8.016)), ((13.62, 8.016), (13.486, 8), (13.352, 8)), ((13.35, 8), (13.348, 8), (13.345, 8)), ((13.064, 8), (12.773, 8.032), (12.491, 8.032)), ((8.1, 8.032), (4.018, 15.376), (4.018, 23.072)), ((4.018, 23.45), (4, 23.812), (4, 24.175)), ((4, 24.18), (4, 24.186), (4, 24.192)), ((4, 24.576), (4.018, 24.944), (4.018, 25.312)), ((4.018, 26.16), (4.173, 27.104), (4.291, 27.936)), ((5.173, 34.48), (8.618, 39.984), (12.527, 39.984)), ((12.773, 39.984), (13.009, 40), (13.245, 40)), ((13.247, 40), (13.248, 40), (13.249, 40)), ((13.33, 40), (13.419, 40), (13.5, 40)), ((17.045, 40), (20.255, 33.912), (22, 29)))
        self.add_bezier('e2', (27, 16), ((28.618, 11.44), (31.5, 8.032), (34.555, 8.032)), ((34.764, 8.032), (34.964, 8), (35.173, 8)), ((35.245, 8.016), (35.327, 8.016), (35.4, 8.032)), ((39.755, 8.032), (44, 15.136), (44, 22.912)), ((44, 22.914), (44, 22.916), (44, 22.918)), ((44, 23.044), (44, 23.17), (44, 23.28)), ((44, 23.664), (43.982, 24.048), (43.982, 24.416)), ((43.982, 31.84), (40.291, 39.968), (35.855, 39.968)), ((35.627, 39.968), (35.391, 40), (35.155, 40)), ((34.918, 40), (34.691, 39.968), (34.455, 39.968)), ((30.782, 39.968), (28.291, 34.304), (26, 30)))
        self.add_contour('c0', 'e1', 'e0', 'e2')
