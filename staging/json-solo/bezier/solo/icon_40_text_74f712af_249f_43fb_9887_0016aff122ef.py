"""40 (text) (text), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '74f712af-249f-43fb-9887-0016aff122ef'
SOURCE_PATH = 'icons-json/text/40 (text)_74f712af-249f-43fb-9887-0016aff122ef.json'
AUTHOR = 'json_to_solo'

class Icon40TextText(Solo48):
    icon_id = 'icon-40-text-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('text',)

    def build(self):
        self.add_line('e0', (19, 33), (4, 33))
        self.add_line('e1', (4, 33), (16, 8))
        self.add_line('e2', (16, 8), (16, 40))
        self.add_bezier('e3', (28, 24), ((28.018, 22.806), (27.655, 21.612), (27.809, 20.431)), ((28.482, 15.237), (30.918, 8.012), (35.482, 8.012)), ((35.573, 8), (35.664, 8), (35.755, 8)), ((35.845, 8), (35.936, 8), (36.036, 8.012)), ((41.009, 8.012), (43.982, 16.369), (43.982, 22.314)), ((43.982, 22.769), (44, 23.237), (44, 23.692)), ((44, 23.701), (44, 23.71), (44, 23.718)), ((44, 24.264), (43.982, 24.821), (43.982, 25.366)), ((43.982, 31.138), (41.509, 39.988), (36.482, 39.988)), ((36.391, 40), (36.3, 40), (36.209, 40)), ((36.118, 40), (36.027, 40), (35.927, 39.988)), ((30.291, 39.988), (28.073, 30.363), (28, 24)))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3', closed=True)
