"""A Cupid arrow pierces a heart diagonally; one fletching chevron replaces tiny feathers.

Construction references: Lucide heart, hand-heart, sprout and balloon as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = ('c6a8f9b5-4b58-5f76-86c0-ef27a854f0e3', '19bddf31-1d8e-5c80-a49c-063c72ba25dd', '51e76296-a983-5334-b175-a7cea9b5c594', 'bfd27f8d-8727-5931-9917-75f7ab5d709f', '70377e7a-8cca-5570-bd4d-b59d111416c4', '96b4290c-87f0-48c0-8533-608fb681e5cb', '8754b18e-fc4d-41a8-894a-39b1c99f6f6f', 'a2887055-760f-49bf-891b-ea35d76e023d')
SOURCE_PATH = ('pictographic-primitives/romance/dating flowers vase_c6a8f9b5-4b58-5f76-86c0-ef27a854f0e3.svg', 'pictographic-primitives/romance/dating rose vase_19bddf31-1d8e-5c80-a49c-063c72ba25dd.svg', 'pictographic-primitives/romance/dating rose_51e76296-a983-5334-b175-a7cea9b5c594.svg', 'pictographic-primitives/romance/diamond ring_bfd27f8d-8727-5931-9917-75f7ab5d709f.svg', 'pictographic-primitives/romance/engagement ring_70377e7a-8cca-5570-bd4d-b59d111416c4.svg', 'pictographic-primitives/romance/flowers_96b4290c-87f0-48c0-8533-608fb681e5cb.svg', 'pictographic-primitives/romance/lesbian lgbt heart_8754b18e-fc4d-41a8-894a-39b1c99f6f6f.svg', 'pictographic-primitives/romance/lgbt bracelet hand_a2887055-760f-49bf-891b-ea35d76e023d.svg')
AUTHOR = 'gpt-6'


class HeartPiercedByArrow(Solo48):
    icon_id = 'heart-pierced-by-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('heart', 'arrow', 'cupid', 'love', 'romance', 'pierced')

    def build(self) -> None:
        self.add_arc('lobe-l',(24,12),(12,12),radius_x=6,sweep=False)
        self.add_arc('shoulder-l',(12,12),(14,16),radius_x=5,sweep=False)
        self.add_line('side-l-upper',(14,16),(20,28))
        self.add_line('side-l-lower',(20,28),(24,34))
        self.add_line('side-r-lower',(24,34),(28,28))
        self.add_line('side-r-upper',(28,28),(34,16))
        self.add_arc('shoulder-r',(34,16),(36,12),radius_x=5,sweep=False)
        self.add_arc('lobe-r',(36,12),(24,12),radius_x=6,sweep=False)
        self.add_contour('heart','lobe-l','shoulder-l','side-l-upper','side-l-lower','side-r-lower','side-r-upper','shoulder-r','lobe-r',closed=True)
        self.add_line('arrow-inside',(28,20),(36,12))
        self.add_line('arrow-outside',(36,12),(42,6))
        self.add_contour('arrow-front','arrow-inside','arrow-outside')
        self.add_polyline('arrowhead',(34,6),(42,6),(42,14))
        self.relate('connect','arrow-front','arrowhead')
        self.relate('connect','arrow-front','heart')
        self.add_line('arrow-back',(6,42),(20,28))
        self.add_polyline('fletching',(6,34),(6,42),(14,42))
        self.relate('connect','arrow-back','fletching')
        self.relate('connect','arrow-back','heart')
