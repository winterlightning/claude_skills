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
        # Centerline extremes: (6,6)-(42,42).
        self.add_line("top",(10,6),(38,6))
        self.add_arc("tr",(38,6),(42,10),radius_x=8)
        self.add_line("right",(42,10),(42,38))
        self.add_arc("br",(42,38),(38,42),radius_x=8)
        self.add_line("bottom",(38,42),(10,42))
        self.add_arc("bl",(10,42),(6,38),radius_x=8)
        self.add_line("left",(6,38),(6,10))
        self.add_arc("tl",(6,10),(10,6),radius_x=8)
        self.add_contour("stone","top","tr","right","br","bottom","bl","left","tl",closed=True)
        self.add_polyline("spine",(24,11),(20,19),(26,28),(24,37))
        self.add_polyline("left-wing",(20,19),(11,21),(11,30))
        self.relate("connect","spine","left-wing")
        self.add_polyline("right-wing",(20,19),(34,15),(37,24))
        self.relate("connect","spine","right-wing")
