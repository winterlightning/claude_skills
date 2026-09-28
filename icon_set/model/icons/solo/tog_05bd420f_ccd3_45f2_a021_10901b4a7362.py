"""A single diagonal luggage tag with a clear punched hole.
The tag outline and hole are one symbol; the diagonal follows the source.
Lucide tag supplied the rounded polygon and isolated aperture construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "05bd420f-ccd3-45f2-a021-10901b4a7362"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__tog/20260927T140835Z-thuan-mac-1/reference/tog_05bd420f-ccd3-45f2-a021-10901b4a7362.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "tog"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("tag", "luggage-tag")
    keywords = ("tog", "tag", "label")
    def build(self):
        self.add_polyline("tag",(6,27),(20,6),(38,6),(42,10),(42,23),(23,42),(18,42),(6,30),closed=True)
        self.add_arc("hole-upper",(26,18),(34,18),radius_x=4)
        self.add_arc("hole-lower",(34,18),(26,18),radius_x=4)
        self.add_contour("hole","hole-upper","hole-lower",closed=True)
