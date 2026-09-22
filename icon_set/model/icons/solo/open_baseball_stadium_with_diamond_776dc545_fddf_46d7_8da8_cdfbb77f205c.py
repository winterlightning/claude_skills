"""Open baseball stadium surrounding a diamond-shaped field.
HRECT_L bounds 4,8–44,40; mirror shell and diamond about x24.
The infield is intrinsic architecture, not a reusable contained status glyph.
Source supplies cutaway stadium and diamond. Omit seating ticks and mound
for legibility. No useful local Lucide stadium match.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = "776dc545-fddf-46d7-8da8-cdfbb77f205c"
SOURCE_PATH = "pictographic-primitives/_uncategorized_05/ballpark_776dc545-fddf-46d7-8da8-cdfbb77f205c.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "open-baseball-stadium-with-diamond"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ["Baseball Diamond Stadium"]
    keywords = ["baseball", "stadium", "diamond", "field", "mound", "ballpark", "sport"]
    def build(self):
        axis=24;left=4;right=2*axis-left
        self.add_line("wall-left",(left,32),(left,18))
        self.add_arc("rear-rim",(left,18),(right,18),radius_x=20,radius_y=10)
        self.add_line("wall-right",(right,18),(right,32))
        self.add_contour("stadium","wall-left","rear-rim","wall-right")
        self.add_polyline("infield",(axis,24),(34,32),(axis,40),(14,32),closed=True)
        self.add_bezier("rim-front-left",(4,18),((6,20),(9,21),(12,22)))
        self.add_bezier("rim-front-right",(44,18),((42,20),(39,21),(36,22)))
        self.relate("connect","stadium","rim-front-left")
        self.relate("connect","stadium","rim-front-right")
