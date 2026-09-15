"""Three pointed petal tips form one upright bud above a short stem. VRECT extremes (8,4)-(40,44); mirrored sides surround the taller central petal.
Reduction: Removed overlapping inner petal seams while retaining all three pointed tips.
Lucide construction: flower-2, leaf
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '040b040e-612c-45ac-a316-563014f6363c'
SOURCE_PATH = 'pictographic-primitives/nature/plant_040b040e-612c-45ac-a316-563014f6363c.svg'
AUTHOR = 'gpt-6'


class ThreePetalBud(Solo48):
    icon_id = 'three-petal-bud'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-02"
    aliases = ()
    keywords = ('bud', 'plant', 'petals', 'lotus', 'flower', 'growth', 'nature', 'botanical')

    def build(self) -> None:
        self.add_line("left-tip",(8,12),(18,18))
        self.add_arc("center-left",(18,18),(24,4),radius_x=20)
        self.add_arc("center-right",(24,4),(30,18),radius_x=20)
        self.add_line("right-tip",(30,18),(40,12))
        self.add_arc("bowl-right",(40,12),(24,36),radius_x=16,radius_y=24)
        self.add_arc("bowl-left",(24,36),(8,12),radius_x=16,radius_y=24)
        self.add_contour("bud","left-tip","center-left","center-right","right-tip","bowl-right","bowl-left",closed=True)
        self.add_line("stem",(24,36),(24,44))
        self.relate("connect","stem","bowl-right")
        self.relate("connect","stem","bowl-left")
