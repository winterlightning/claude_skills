"""A round-topped cactus column with two upturned arms stands in a tapered pot. VRECT extremes (8,4)-(40,44); paired arm radii and actual wall attachment nodes. Unequal arm heights preserve the source’s subtle asymmetry.
Reduction: Removed the separate pot rim band. Reduced plump arm outlines to rounded single strokes.
Lucide construction: No useful local cactus original; rounded column and elbow construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ce2ed8d-91f7-5823-ac9f-99e07111304f'
SOURCE_PATH = 'pictographic-primitives/nature/plant pot_6ce2ed8d-91f7-5823-ac9f-99e07111304f.svg'
AUTHOR = 'gpt-6'


class CactusWithRoundedArmsInPot(Solo48):
    icon_id = 'cactus-with-rounded-arms-in-pot'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    aliases = ()
    keywords = ('cactus', 'succulent', 'pot', 'plant', 'desert', 'houseplant', 'potted', 'nature')

    def build(self) -> None:
        # The rounded column owns split arm attachment nodes.
        self.add_arc("crown",(20,8),(28,8),radius_x=4)
        self.add_line("right-upper",(28,8),(28,20))
        self.add_line("right-lower",(28,20),(28,32))
        self.add_line("base",(28,32),(20,32))
        self.add_line("left-lower",(20,32),(20,20))
        self.add_line("left-upper",(20,20),(20,8))
        self.add_contour("column","crown","right-upper","right-lower","base","left-lower","left-upper",closed=True)
        self.add_line("left-tip",(8,14),(8,16))
        self.add_arc("left-elbow",(8,16),(12,20),radius_x=4,sweep=False)
        self.add_line("left-arm",(12,20),(20,20))
        self.add_contour("left","left-tip","left-elbow","left-arm")
        self.add_line("right-tip",(40,10),(40,16))
        self.add_arc("right-elbow",(40,16),(36,20),radius_x=4)
        self.add_line("right-arm",(36,20),(28,20))
        self.add_contour("right","right-tip","right-elbow","right-arm")
        for side in ("left","right"):
            for part in ("upper","lower"):self.relate("connect",side+"-arm",side+"-"+part)
        self.add_polyline("pot",(8,32),(20,32),(28,32),(40,32),(36,44),(12,44),closed=True)
        for a in ("left-lower","base"):
            self.relate("connect",a,"pot-1")
            self.relate("connect",a,"pot-2")
        for a in ("right-lower","base"):
            self.relate("connect",a,"pot-2")
            self.relate("connect",a,"pot-3")
