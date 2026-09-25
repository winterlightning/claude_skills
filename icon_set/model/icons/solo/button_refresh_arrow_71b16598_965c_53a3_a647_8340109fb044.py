"""Button refresh arrow (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '71b16598-965c-53a3-a647-8340109fb044'
SOURCE_PATH = 'pictographic-primitives/interface-essential/button refresh arrow_71b16598-965c-53a3-a647-8340109fb044.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class ButtonRefreshArrow(Solo48):
    icon_id = 'button-refresh-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('button', 'refresh', 'arrow', 'interface-essential')

    def build(self):
        # Plan: remove subpixel cubic detours while preserving real contour nodes.
        # Reference: supplied subject and its existing stroke graph.
        self.add_line('e0', (18, 40), (17, 35))
        self.add_line('e1', (13, 42), (18, 40))
        self.add_bezier('e2', (24, 41), ((31.691, 40.673), (38.809, 36.166), (41.157, 28.664)), ((41.624, 27.183), (41.984, 25.522), (41.984, 23.959)), ((41.992, 23.877), (41.992, 23.787), (42, 23.705)), ((42, 23.495), (41.984, 23.293), (41.984, 23.084)), ((41.984, 15.286), (36.715, 8.986), (29.4, 6.802)), ((27.845, 6.335), (26.176, 6), (24.54, 6)), ((24.303, 6), (24.07, 6.016), (23.845, 6.016)), ((14.665, 6.016), (6.016, 13.323), (6.016, 22.838)), ((6.016, 23.092), (6, 23.354), (6, 23.615)), ((6, 23.928), (6.008, 24.234), (6.008, 24.54)), ((6.008, 25.497), (6.278, 26.528), (6.483, 27.453)), ((7.555, 32.255), (10.983, 36.42), (15.172, 38.891)), ((16.154, 39.472), (16.961, 39.534), (18, 40)))
        self.add_contour('c0', 'e2', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
