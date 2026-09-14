"""A larger rear heart balloon overlaps a smaller front heart; knots and hidden outline are omitted.

Construction references: Lucide heart, hand-heart, sprout and balloon as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = ('c6a8f9b5-4b58-5f76-86c0-ef27a854f0e3', '19bddf31-1d8e-5c80-a49c-063c72ba25dd', '51e76296-a983-5334-b175-a7cea9b5c594', 'bfd27f8d-8727-5931-9917-75f7ab5d709f', '70377e7a-8cca-5570-bd4d-b59d111416c4', '96b4290c-87f0-48c0-8533-608fb681e5cb', '8754b18e-fc4d-41a8-894a-39b1c99f6f6f', 'a2887055-760f-49bf-891b-ea35d76e023d')
SOURCE_PATH = ('pictographic-primitives/romance/dating flowers vase_c6a8f9b5-4b58-5f76-86c0-ef27a854f0e3.svg', 'pictographic-primitives/romance/dating rose vase_19bddf31-1d8e-5c80-a49c-063c72ba25dd.svg', 'pictographic-primitives/romance/dating rose_51e76296-a983-5334-b175-a7cea9b5c594.svg', 'pictographic-primitives/romance/diamond ring_bfd27f8d-8727-5931-9917-75f7ab5d709f.svg', 'pictographic-primitives/romance/engagement ring_70377e7a-8cca-5570-bd4d-b59d111416c4.svg', 'pictographic-primitives/romance/flowers_96b4290c-87f0-48c0-8533-608fb681e5cb.svg', 'pictographic-primitives/romance/lesbian lgbt heart_8754b18e-fc4d-41a8-894a-39b1c99f6f6f.svg', 'pictographic-primitives/romance/lgbt bracelet hand_a2887055-760f-49bf-891b-ea35d76e023d.svg')
AUTHOR = 'gpt-6'


class TwoHeartBalloons(Solo48):
    icon_id = 'two-heart-balloons'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('heart', 'balloons', 'pair', 'party', 'romance', 'celebration')

    def build(self) -> None:
        def heart(n,cx,y,r,tip):
            self.add_arc(n+'-l',(cx,y),(cx-2*r,y),radius_x=r,sweep=False)
            self.add_arc(n+'-shl',(cx-2*r,y),(cx-2*r+2,y+4),radius_x=5,sweep=False)
            self.add_line(n+'-sl',(cx-2*r+2,y+4),(cx,tip))
            self.add_line(n+'-sr',(cx,tip),(cx+2*r-2,y+4))
            self.add_arc(n+'-shr',(cx+2*r-2,y+4),(cx+2*r,y),radius_x=5,sweep=False)
            self.add_arc(n+'-r',(cx+2*r,y),(cx,y),radius_x=r,sweep=False)
            self.add_contour(n,n+'-l',n+'-shl',n+'-sl',n+'-sr',n+'-shr',n+'-r',closed=True)

        self.add_arc('large-lobe-l',(20,10),(8,10),radius_x=6,sweep=False)
        self.add_arc('large-shoulder-l',(8,10),(10,14),radius_x=5,sweep=False)
        self.add_line('large-side-l',(10,14),(20,27))
        self.add_line('large-bottom',(20,27),(24,26))
        self.add_arc('large-lobe-r',(32,10),(20,10),radius_x=6,sweep=False)
        self.add_arc('large-shoulder-r',(30,14),(32,10),radius_x=5,sweep=False)
        self.add_line('large-side-r',(28,22),(30,14))
        self.add_contour('rear-left','large-lobe-l','large-shoulder-l','large-side-l','large-bottom')
        self.add_contour('rear-right','large-side-r','large-shoulder-r','large-lobe-r')
        self.relate('connect','rear-left','rear-right')
        self.add_arc('small-l1',(32,26),(28,22),radius_x=4,sweep=False)
        self.add_arc('small-l2',(28,22),(24,26),radius_x=4,sweep=False)
        self.add_arc('small-shl',(24,26),(26,30),radius_x=5,sweep=False)
        self.add_line('small-sl',(26,30),(32,38))
        self.add_line('small-sr',(32,38),(38,30))
        self.add_arc('small-shr',(38,30),(40,26),radius_x=5,sweep=False)
        self.add_arc('small-r',(40,26),(32,26),radius_x=4,sweep=False)
        self.add_contour('small','small-l1','small-l2','small-shl','small-sl','small-sr','small-shr','small-r',closed=True)
        self.relate('connect','rear-left','small')
        self.relate('connect','rear-right','small')
        self.add_arc('string-l',(20,27),(14,44),radius_x=18)
        self.add_arc('string-r',(32,38),(30,44),radius_x=10)
        self.relate('connect','rear-left','string-l')
        self.relate('connect','small','string-r')
