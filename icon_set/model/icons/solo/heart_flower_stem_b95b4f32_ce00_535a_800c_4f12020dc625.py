"""A heart flower on a straight stem has two mirrored pointed leaves; veins are omitted.

Construction references: Lucide heart, hand-heart, sprout and balloon as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b95b4f32-ce00-535a-800c-4f12020dc625'
SOURCE_PATH = 'pictographic-primitives/romance/love bud_b95b4f32-ce00-535a-800c-4f12020dc625.svg'
AUTHOR = 'gpt-6'


class HeartFlowerStem(Solo48):
    icon_id = 'heart-flower-stem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "romance"
    categories = ("primitives", "romance")
    aliases = ()
    keywords = ('heart', 'flower', 'stem', 'leaf', 'plant', 'romance')

    def build(self) -> None:
        self.add_arc('lobe-l',(24,12),(8,12),radius_x=8,sweep=False)
        self.add_arc('shoulder-l',(8,12),(12,20),radius_x=10,sweep=False)
        self.add_line('heart-l',(12,20),(24,28))
        self.add_line('heart-r',(24,28),(36,20))
        self.add_arc('shoulder-r',(36,20),(40,12),radius_x=10,sweep=False)
        self.add_arc('lobe-r',(40,12),(24,12),radius_x=8,sweep=False)
        self.add_contour('bloom','lobe-l','shoulder-l','heart-l','heart-r','shoulder-r','lobe-r',closed=True)
        self.add_line('stem-a',(24,28),(24,38))
        self.add_line('stem-b',(24,38),(24,44))
        self.add_contour('stem','stem-a','stem-b')
        self.relate('connect','bloom','stem')
        for side in (-1,1):
            n='leaf-l' if side<0 else 'leaf-r'
            self.add_arc(n+'-a',(24,38),(24+16*side,28),radius_x=16,radius_y=10,sweep=side<0)
            self.add_arc(n+'-b',(24+16*side,28),(24,38),radius_x=16,radius_y=10,sweep=side<0)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
            self.relate('connect','stem',n)
        self.relate('connect','leaf-l','leaf-r')
