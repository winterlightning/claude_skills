"""Two outlined descending chart columns on a shared baseline with a left axis.
SQUARE: axis starts6,6; baseline ends42,42. A repeated8-unit column width and
16-unit step give identical openings/gaps; only the top height changes.
Source supplies two outlined bars and axes. Lucide chart-no-axes-column-decreasing
informs the shared baseline and decreasing heights, not its three solid bars.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = "af5465db-c598-4951-abe8-0254bea610c7"
SOURCE_PATH = "pictographic-primitives/_uncategorized_05/bar step_af5465db-c598-4951-abe8-0254bea610c7.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "two-descending-columns-on-axes"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ["Decreasing Bar Chart Statistics"]
    keywords = ["chart", "bars", "columns", "descending", "statistics", "axes", "graph"]
    def build(self):
        baseline=42;width=8;step=16
        self.add_polyline("axes",(6,6),(6,baseline),(14,baseline),(22,baseline),(30,baseline),(38,baseline),(42,baseline))
        for i,top in enumerate([10,22]):
            left=14+i*step
            uid=f"column-{i+1}"
            self.add_polyline(uid,(left,baseline),(left,top),(left+width,top),(left+width,baseline))
            self.relate("connect",uid,"axes")
