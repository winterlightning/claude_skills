"""A pitched-roof house with a crack descending from its right roof slope. Square envelope. Roof owns exact crack attachment (32,14); left-shifted doorway reserves room for the asymmetric damage. Lucide house informs coherent outline and open doorway. Reference supplies crack placement; simplify rounded doorway to three sides and omit the final small crack bend."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '0e26ccf9-f038-4d05-aee6-75c22820f856'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_28/natural disaster hurricane house damaged_0e26ccf9-f038-4d05-aee6-75c22820f856.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'house-roof-crack'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = []
    keywords = ['house', 'crack', 'damage', 'roof', 'building', 'home']
    def build(self):
        self.add_polyline('house',(32,14),(42,24),(42,42),(22,42),(22,30),(14,30),(14,42),(6,42),(6,24),(24,6),closed=True)
        self.add_polyline('crack',(32,14),(28,22),(32,26))
        self.relate('connect','house','crack')
