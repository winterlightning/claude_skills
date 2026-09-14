"""70 (text) (text), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2792944b-1f57-4c58-8e3b-19150be318d8'
SOURCE_PATH = 'icons-json/text/70 (text)_2792944b-1f57-4c58-8e3b-19150be318d8.json'
AUTHOR = 'json_to_solo'

class Icon70TextText(Solo48):
    icon_id = 'icon-70-text-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('text',)

    def build(self):
        self.add_line('e0', (4, 8), (19, 8))
        self.add_line('e1', (19, 8), (9, 40))
        self.add_bezier('e2', (29, 24), ((29.045, 18.031), (29.991, 8.012), (35.682, 8.012)), ((35.773, 8), (35.864, 8), (35.955, 8)), ((36.045, 8), (36.136, 8), (36.227, 8.012)), ((41.145, 8.012), (43.982, 16.505), (43.982, 22.314)), ((43.982, 22.769), (44, 23.237), (44, 23.692)), ((44, 23.701), (44, 23.71), (44, 23.718)), ((44, 24.264), (43.982, 24.821), (43.982, 25.366)), ((43.982, 31.028), (41.636, 39.988), (36.664, 39.988)), ((36.573, 40), (36.482, 40), (36.391, 40)), ((36.3, 40), (36.209, 40), (36.118, 39.988)), ((30.273, 39.988), (29.018, 30.252), (29, 24)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', closed=True)
