"""A heart balloon has a knot and a gently bending string; the knot is an open chevron.

Construction references: Lucide heart, hand-heart, sprout and balloon as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = ('c6a8f9b5-4b58-5f76-86c0-ef27a854f0e3', '19bddf31-1d8e-5c80-a49c-063c72ba25dd', '51e76296-a983-5334-b175-a7cea9b5c594', 'bfd27f8d-8727-5931-9917-75f7ab5d709f', '70377e7a-8cca-5570-bd4d-b59d111416c4', '96b4290c-87f0-48c0-8533-608fb681e5cb', '8754b18e-fc4d-41a8-894a-39b1c99f6f6f', 'a2887055-760f-49bf-891b-ea35d76e023d')
SOURCE_PATH = ('pictographic-primitives/romance/dating flowers vase_c6a8f9b5-4b58-5f76-86c0-ef27a854f0e3.svg', 'pictographic-primitives/romance/dating rose vase_19bddf31-1d8e-5c80-a49c-063c72ba25dd.svg', 'pictographic-primitives/romance/dating rose_51e76296-a983-5334-b175-a7cea9b5c594.svg', 'pictographic-primitives/romance/diamond ring_bfd27f8d-8727-5931-9917-75f7ab5d709f.svg', 'pictographic-primitives/romance/engagement ring_70377e7a-8cca-5570-bd4d-b59d111416c4.svg', 'pictographic-primitives/romance/flowers_96b4290c-87f0-48c0-8533-608fb681e5cb.svg', 'pictographic-primitives/romance/lesbian lgbt heart_8754b18e-fc4d-41a8-894a-39b1c99f6f6f.svg', 'pictographic-primitives/romance/lgbt bracelet hand_a2887055-760f-49bf-891b-ea35d76e023d.svg')
AUTHOR = 'gpt-6'


class HeartBalloon(Solo48):
    icon_id = 'heart-balloon'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('heart', 'balloon', 'string', 'party', 'romance', 'celebration')

    def build(self) -> None:
        self.add_arc('lobe-l',(24,12),(8,12),radius_x=8,sweep=False)
        self.add_arc('shoulder-l',(8,12),(12,20),radius_x=10,sweep=False)
        self.add_line('side-l',(12,20),(24,30))
        self.add_line('side-r',(24,30),(36,20))
        self.add_arc('shoulder-r',(36,20),(40,12),radius_x=10,sweep=False)
        self.add_arc('lobe-r',(40,12),(24,12),radius_x=8,sweep=False)
        self.add_contour('balloon','lobe-l','shoulder-l','side-l','side-r','shoulder-r','lobe-r',closed=True)
        self.add_polyline('knot',(20,34),(24,30),(28,34))
        self.relate('connect','balloon','knot')
        self.add_arc('string-a',(24,30),(22,37),radius_x=10,sweep=False)
        self.add_arc('string-b',(22,37),(24,44),radius_x=10)
        self.add_contour('string','string-a','string-b')
        self.relate('connect','balloon','string')
        self.relate('connect','knot','string')
