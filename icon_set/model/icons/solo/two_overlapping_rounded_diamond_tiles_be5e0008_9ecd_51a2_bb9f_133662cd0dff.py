"""Two Stacked Design Layers.

Symbol plan: Two broad diamond tiles; lower rear contour joins the top at sloping edge midpoints. Lucide layers-2 informs the overlap. Mirror across x=24.
Keyshape: HRECT_L; exact visible bounds (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be5e0008-9ecd-51a2-bb9f-133662cd0dff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/layers stacked_be5e0008-9ecd-51a2-bb9f-133662cd0dff.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'two-overlapping-rounded-diamond-tiles'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design"
    categories = ("design", "primitives")
    aliases = ()
    keywords = ('two', 'stacked', 'design', 'layers')

    def build(self):
        a=24
        self.add_polyline('top',(a,8),(44,18),(a,28),(4,18),closed=True)
        self.add_polyline('rear',(16,24),(4,30),(a,40),(44,30),(32,24))
        self.relate('connect','top','rear')
