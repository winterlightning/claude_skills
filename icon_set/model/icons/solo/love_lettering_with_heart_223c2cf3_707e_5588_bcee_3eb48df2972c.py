"""LOVE occupies a two-by-two square with a heart as the O; letter strokes remain open.

Construction references: Lucide heart, hand-heart, sprout and balloon as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = ('c6a8f9b5-4b58-5f76-86c0-ef27a854f0e3', '19bddf31-1d8e-5c80-a49c-063c72ba25dd', '51e76296-a983-5334-b175-a7cea9b5c594', 'bfd27f8d-8727-5931-9917-75f7ab5d709f', '70377e7a-8cca-5570-bd4d-b59d111416c4', '96b4290c-87f0-48c0-8533-608fb681e5cb', '8754b18e-fc4d-41a8-894a-39b1c99f6f6f', 'a2887055-760f-49bf-891b-ea35d76e023d')
SOURCE_PATH = ('pictographic-primitives/romance/dating flowers vase_c6a8f9b5-4b58-5f76-86c0-ef27a854f0e3.svg', 'pictographic-primitives/romance/dating rose vase_19bddf31-1d8e-5c80-a49c-063c72ba25dd.svg', 'pictographic-primitives/romance/dating rose_51e76296-a983-5334-b175-a7cea9b5c594.svg', 'pictographic-primitives/romance/diamond ring_bfd27f8d-8727-5931-9917-75f7ab5d709f.svg', 'pictographic-primitives/romance/engagement ring_70377e7a-8cca-5570-bd4d-b59d111416c4.svg', 'pictographic-primitives/romance/flowers_96b4290c-87f0-48c0-8533-608fb681e5cb.svg', 'pictographic-primitives/romance/lesbian lgbt heart_8754b18e-fc4d-41a8-894a-39b1c99f6f6f.svg', 'pictographic-primitives/romance/lgbt bracelet hand_a2887055-760f-49bf-891b-ea35d76e023d.svg')
AUTHOR = 'gpt-6'


class LoveLetteringWithHeart(Solo48):
    icon_id = 'love-lettering-with-heart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('love', 'lettering', 'heart', 'word', 'romance', 'typography')

    def build(self) -> None:
        def heart(n,cx,y,r,tip):
            self.add_arc(n+'-l',(cx,y),(cx-2*r,y),radius_x=r,sweep=False)
            self.add_arc(n+'-shl',(cx-2*r,y),(cx-2*r+2,y+4),radius_x=5,sweep=False)
            self.add_line(n+'-sl',(cx-2*r+2,y+4),(cx,tip))
            self.add_line(n+'-sr',(cx,tip),(cx+2*r-2,y+4))
            self.add_arc(n+'-shr',(cx+2*r-2,y+4),(cx+2*r,y),radius_x=5,sweep=False)
            self.add_arc(n+'-r',(cx+2*r,y),(cx,y),radius_x=r,sweep=False)
            self.add_contour(n,n+'-l',n+'-shl',n+'-sl',n+'-sr',n+'-shr',n+'-r',closed=True)

        self.add_polyline('letter-l',(6,6),(6,22),(18,22))
        heart('heart-o',34,10,4,17)
        self.add_polyline('letter-v',(6,30),(12,42),(18,30))
        self.add_polyline('letter-e',(42,26),(28,26),(28,34),(28,42),(42,42))
        self.add_line('e-middle',(28,34),(40,34))
        self.relate('connect','letter-e','e-middle')
