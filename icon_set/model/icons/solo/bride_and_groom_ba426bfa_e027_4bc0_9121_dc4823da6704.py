"""A groom and veiled bride stand side by side; face and finger details omitted.

Construction references: Lucide heart, hand, sprout, balloon, cake, car and users-round as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ba426bfa-e027-4bc0-9121-dc4823da6704'
SOURCE_PATH = 'pictographic-primitives/romance/wedding bride groom_ba426bfa-e027-4bc0-9121-dc4823da6704.svg'
AUTHOR = 'gpt-6'


class BrideAndGroom(Solo48):
    icon_id = 'bride-and-groom'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('bride', 'groom', 'couple', 'wedding', 'veil', 'marriage')

    def build(self) -> None:
        self.add_arc('groom-head-r',(12,6),(12,14),radius_x=4)
        self.add_arc('groom-head-l',(12,14),(12,6),radius_x=4)
        self.add_contour('groom-head','groom-head-r','groom-head-l',closed=True)
        self.add_polyline('shirt',(6,32),(6,25),(12,23),(18,25),(18,32),(16,32),(8,32),closed=True)
        self.add_line('leg-l',(8,32),(8,42))
        self.add_line('leg-r',(16,32),(16,42))
        self.relate('connect','shirt','leg-l')
        self.relate('connect','shirt','leg-r')
        self.add_arc('bride-hair',(26,14),(42,14),radius_x=8)
        self.add_arc('bride-face',(42,14),(26,14),radius_x=8)
        self.add_contour('bride-head','bride-hair','bride-face',closed=True)
        self.add_polyline('veil-l',(26,14),(26,26),(30,26))
        self.add_polyline('veil-r',(42,14),(42,26),(38,26))
        self.add_polyline('dress',(30,26),(34,30),(38,26),(42,42),(26,42),closed=True)
        self.relate('connect','bride-head','veil-l')
        self.relate('connect','bride-head','veil-r')
        self.relate('connect','veil-l','dress')
        self.relate('connect','veil-r','dress')
