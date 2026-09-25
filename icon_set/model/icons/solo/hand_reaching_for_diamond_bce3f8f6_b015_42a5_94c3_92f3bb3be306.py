"""Hand Holding Diamond.
Plan: Open upright pinch reaches toward a broad upper-left diamond. Extrema (6,6)-(42,42).
Reference: Lucide gem and hand: broad gem silhouette and coherent thumb-to-palm outline; shared human reference reviewed.
Reduction: Diamond facet line and finger creases removed; open pinch and crown silhouette retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bce3f8f6-b015-42a5-94c3-92f3bb3be306'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/diamond hold_bce3f8f6-b015-42a5-94c3-92f3bb3be306.svg'
AUTHOR = 'gpt-6'

class Batch30Icon(Solo48):
    icon_id = 'hand-reaching-for-diamond'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "finance"
    aliases = ()
    keywords = ('hand', 'holding', 'diamond')

    def build(self):

        self.add_polyline('gem',(6,12),(10,6),(22,6),(26,12),(16,22),(6,12))
        self.add_polyline('thumb',(24,42),(24,36),(18,30),(26,34))
        self.add_bezier('palm-inner',(26,34),((32,34),(32,20),(34,14)))
        self.add_bezier('palm-outer',(34,14),((40,14),(42,20),(42,28)),((42,34),(42,38),(42,42)))
        self.relate('connect','thumb','palm-inner');self.relate('connect','palm-inner','palm-outer')
