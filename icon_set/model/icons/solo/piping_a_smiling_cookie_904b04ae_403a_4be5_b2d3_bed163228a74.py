"""A smiling cookie is being decorated by a piping bag. SQUARE 6..42 balances round cookie and upper-right bag. Source supplies physical decorating scene; Lucide cookie teaches interrupted circular contour and dot details. Eyes reduced to dots and bag cropped open."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '904b04ae-403a-4be5-b2d3-bed163228a74'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_13/cookies decirating 1_904b04ae-403a-4be5-b2d3-bed163228a74.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'piping-a-smiling-cookie'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('Decorating Smiley Face Cookie',)
    keywords = ('cookie', 'icing', 'piping', 'baking', 'smile', 'decoration', 'pastry')
    def build(self):
        self.add_arc("cookie-upper",(22,10),(6,26),radius_x=16,sweep=False)
        self.add_arc("cookie-lower",(6,26),(22,42),radius_x=16,sweep=False)
        self.add_bezier("cookie-right",(22,42),((30,42),(35,39),(38,34)))
        self.add_contour("cookie","cookie-upper","cookie-lower","cookie-right")
        for x in (16,24): self.add_dot(f"eye-{x}",(x,22))
        self.add_bezier("smile",(16,30),((18,34),(24,34),(26,30)))
        self.add_polyline("piping-bag",(42,6),(32,24),(42,18))
