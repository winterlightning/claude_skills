"""An upright folded rose with a stem and paired pointed leaves; fine petal layers omitted.

Construction references: Lucide rose, heart, gem and hand as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51e76296-a983-5334-b175-a7cea9b5c594'
SOURCE_PATH = 'pictographic-primitives/romance/dating rose_51e76296-a983-5334-b175-a7cea9b5c594.svg'
AUTHOR = 'gpt-6'


class RoseStem(Solo48):
    icon_id = 'rose-stem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('rose', 'flower', 'stem', 'petal', 'leaf', 'romance')

    def build(self) -> None:
        self.add_arc('crown-l',(24,4),(10,10),radius_x=14,radius_y=6,sweep=False)
        self.add_line('side-l',(10,10),(10,14))
        self.add_arc('cup-l',(10,14),(24,24),radius_x=14,radius_y=10,sweep=False)
        self.add_arc('cup-r',(24,24),(38,14),radius_x=14,radius_y=10,sweep=False)
        self.add_line('side-r',(38,14),(38,10))
        self.add_arc('crown-r',(38,10),(24,4),radius_x=14,radius_y=6,sweep=False)
        self.add_contour('bloom','crown-l','side-l','cup-l','cup-r','side-r','crown-r',closed=True)
        self.add_arc('fold',(10,10),(24,24),radius_x=14)
        self.relate('connect','bloom','fold')
        self.add_line('stem-top',(24,24),(24,38))
        self.add_line('stem-bottom',(24,38),(24,44))
        self.add_contour('stem','stem-top','stem-bottom')
        self.relate('connect','bloom','stem')
        self.relate('connect','fold','stem')
        for side in (-1,1):
            n='leaf-l' if side<0 else 'leaf-r'
            self.add_arc(n+'-a',(24,38),(24+16*side,28),radius_x=16,radius_y=10,sweep=side<0)
            self.add_arc(n+'-b',(24+16*side,28),(24,38),radius_x=16,radius_y=10,sweep=side<0)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
            self.relate('connect','stem',n)
        self.relate('connect','leaf-l','leaf-r')
