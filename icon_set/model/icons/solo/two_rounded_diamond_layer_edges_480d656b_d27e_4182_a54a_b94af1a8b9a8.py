"""Stacked Diamond Layers.

Symbol plan: A mirrored diamond and one open lower edge, using Lucide layers contour grouping. The same slopes are reused.
Keyshape: SQUARE; exact visible bounds (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '480d656b-d27e-4182-a54a-b94af1a8b9a8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/square stack_480d656b-d27e-4182-a54a-b94af1a8b9a8.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'two-rounded-diamond-layer-edges'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design"
    categories = ("design", "primitives")
    aliases = ()
    keywords = ('stacked', 'diamond', 'layers')

    def build(self):
        a=24; half=18
        self.add_polyline('top',(a,6),(a+half,19),(a,32),(a-half,19),closed=True)
        self.add_polyline('lower',(a-half,29),(a,42),(a+half,29))
