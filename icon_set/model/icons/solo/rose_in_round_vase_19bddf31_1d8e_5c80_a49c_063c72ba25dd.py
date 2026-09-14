"""A rose leans right above a round vase; one left leaf remains as a curved sprig.

Construction references: Lucide rose, heart, gem and hand as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '19bddf31-1d8e-5c80-a49c-063c72ba25dd'
SOURCE_PATH = 'pictographic-primitives/romance/dating rose vase_19bddf31-1d8e-5c80-a49c-063c72ba25dd.svg'
AUTHOR = 'gpt-6'


class RoseInRoundVase(Solo48):
    icon_id = 'rose-in-round-vase'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('rose', 'vase', 'flower', 'stem', 'romance', 'decoration')

    def build(self) -> None:
        self.add_arc('bud-crown',(24,12),(40,4),radius_x=16,radius_y=8)
        self.add_line('bud-side',(40,4),(40,12))
        self.add_arc('bud-cup',(40,12),(24,12),radius_x=8)
        self.add_contour('bud','bud-crown','bud-side','bud-cup',closed=True)
        self.add_line('petal-fold',(24,12),(40,12))
        self.relate('connect','bud','petal-fold')
        self.add_arc('stem',(32,20),(22,28),radius_x=24)
        self.relate('connect','bud','stem')
        self.add_arc('leaf',(10,20),(22,28),radius_x=12,radius_y=8,sweep=False)
        self.relate('connect','leaf','stem')
        self.add_line('lip',(18,28),(30,28))
        self.add_arc('shoulder-r',(30,28),(40,36),radius_x=10,radius_y=8)
        self.add_arc('base-r',(40,36),(24,44),radius_x=16,radius_y=8)
        self.add_arc('base-l',(24,44),(8,36),radius_x=16,radius_y=8)
        self.add_arc('shoulder-l',(8,36),(18,28),radius_x=10,radius_y=8)
        self.add_contour('vase','lip','shoulder-r','base-r','base-l','shoulder-l',closed=True)
        self.relate('connect','stem','vase')
        self.relate('connect','leaf','vase')
