"""A sleeveless bridal dress has a pointed neckline, fitted waist and flared skirt with a curved hem; decorative seams omitted.

Construction references: Lucide shirt and star as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a68c5ccf-a8ab-5039-b435-ccd14e4ad205'
SOURCE_PATH = 'pictographic-primitives/romance/wedding dress_a68c5ccf-a8ab-5039-b435-ccd14e4ad205.svg'
AUTHOR = 'gpt-6'


class WeddingDress(Solo48):
    icon_id = 'wedding-dress'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "romance"
    categories = ("primitives", "romance")
    aliases = ()
    keywords = ('dress', 'wedding', 'gown', 'bridal', 'garment', 'skirt')

    def build(self) -> None:
        # One right-side profile owns both halves of the silhouette.
        axis = 24
        right = [(axis,12),(axis+8,4),(axis+10,12),(axis+6,20),(axis+16,40)]
        left = [(2*axis-x,y) for x,y in reversed(right)]
        for side,points in [('right',right),('left',left)]:
            for i,(start,end) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{side}-{i}',start,end)
        self.add_arc('hem-r',(axis+16,40),(axis,44),radius_x=16,radius_y=4)
        self.add_arc('hem-l',(axis,44),(axis-16,40),radius_x=16,radius_y=4)
        self.add_contour('dress',*(f'right-{i}' for i in range(1,5)),'hem-r','hem-l',*(f'left-{i}' for i in range(1,5)),closed=True)
        self.add_line('waist',(axis-6,20),(axis+6,20))
        self.relate('connect','waist','dress')
