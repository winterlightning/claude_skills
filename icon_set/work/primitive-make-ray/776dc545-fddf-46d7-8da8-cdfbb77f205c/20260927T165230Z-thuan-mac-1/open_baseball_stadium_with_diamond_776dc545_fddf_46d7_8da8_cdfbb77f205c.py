"""Open baseball stadium surrounding a diamond-shaped field.
HRECT_L bounds 4,8–44,40; mirror shell and diamond about x24.
The infield is intrinsic architecture, not a reusable contained status glyph.
Source supplies cutaway stadium and diamond. Omit seating ticks and mound
for legibility. No useful local Lucide stadium match.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = "776dc545-fddf-46d7-8da8-cdfbb77f205c"
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__open-baseball-stadium-with-diamond/20260927T164916Z-thuan-mac-1/reference/ballpark_776dc545-fddf-46d7-8da8-cdfbb77f205c.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "open-baseball-stadium-with-diamond"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ["Baseball Diamond Stadium"]
    keywords = ["baseball", "stadium", "diamond", "field", "mound", "ballpark", "sport"]
    def build(self):
        axis=24;left=4;right=2*axis-left
        self.add_line("wall-left",(left,36),(left,18))
        self.add_arc("rear-rim",(left,18),(right,18),radius_x=20,radius_y=10)
        self.add_line("wall-right",(right,18),(right,36))
        self.add_contour("stadium","wall-left","rear-rim","wall-right")
        self.add_polyline("infield",(axis,29),(30,35),(axis,40),(18,35),closed=True)
        self.add_bezier("rim-front-left",(4,18),((10,22),(18,20),(24,20)))
        self.add_bezier("rim-front-right",(44,18),((38,22),(30,20),(24,20)))
        self.relate("connect","stadium","rim-front-left")
        self.relate("connect","stadium","rim-front-right")
