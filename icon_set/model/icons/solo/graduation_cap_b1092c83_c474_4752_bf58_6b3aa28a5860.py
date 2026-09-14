"""A diamond mortarboard sits over a V-bottom skull cap. HRECT_L extremes (6,8)-(42,40). Lucide graduation-cap informs board-to-band joins; preserve the source V-shaped band, symmetric perspective and absence of a tassel."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b1092c83-c474-4752-bf58-6b3aa28a5860'
SOURCE_PATH = 'pictographic-primitives/symbol/graduate hat_b1092c83-c474-4752-bf58-6b3aa28a5860.svg'
AUTHOR = 'gpt-6'


class GraduationCap(Solo48):
    icon_id = 'graduation-cap'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('graduation', 'cap', 'mortarboard', 'education', 'school', 'degree', 'student', 'university')

    def build(self) -> None:
        self.add_polyline('board',(6,18),(24,8),(42,18),(34,23),(24,28),(14,23),(6,18),closed=True)
        self.add_polyline('skull-cap',(14,23),(14,35),(24,40),(34,35),(34,23))
        self.relate('connect','board','skull-cap')
