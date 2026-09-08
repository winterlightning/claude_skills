"""A pterosaur fossil embedded in a rounded stone slab."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac47ac3a-e57f-5b00-8f8a-5ae0e9fb9419'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur pteranodon fossil_ac47ac3a-e57f-5b00-8f8a-5ae0e9fb9419.svg'
AUTHOR = 'gpt-6'


class FossilTablet(Solo48):
    icon_id = 'fossil-tablet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('fossil', 'dinosaur', 'skeleton', 'pterosaur', 'stone', 'tablet', 'archaeology', 'prehistoric')

    def build(self) -> None:
        # Centerline extremes: (2,2)-(46,46).
        self.add_line("top",(10,2),(38,2))
        self.add_arc("tr",(38,2),(46,10),radius_x=8)
        self.add_line("right",(46,10),(46,38))
        self.add_arc("br",(46,38),(38,46),radius_x=8)
        self.add_line("bottom",(38,46),(10,46))
        self.add_arc("bl",(10,46),(2,38),radius_x=8)
        self.add_line("left",(2,38),(2,10))
        self.add_arc("tl",(2,10),(10,2),radius_x=8)
        self.add_contour("stone","top","tr","right","br","bottom","bl","left","tl",closed=True)
        self.add_polyline("spine",(24,11),(20,19),(26,28),(24,37))
        self.add_polyline("left-wing",(20,19),(11,21),(11,30))
        self.relate("connect","spine","left-wing")
        self.add_polyline("right-wing",(20,19),(34,15),(37,24))
        self.relate("connect","spine","right-wing")
