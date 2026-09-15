"""A sprout with an upright tip leaf and two lower pointed leaves. VRECT extremes (8,4)-(40,44); one axis generates mirrored side leaves.
Reduction: Removed the ground line to give all three leaf interiors room.
Lucide construction: sprout, leaf
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f0327d2c-bb99-5e91-9ec2-af95814cf0fe'
SOURCE_PATH = 'pictographic-primitives/nature/plant_f0327d2c-bb99-5e91-9ec2-af95814cf0fe.svg'
AUTHOR = 'gpt-6'


class ThreeLeafSprout(Solo48):
    icon_id = 'three-leaf-sprout'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-02"
    aliases = ()
    keywords = ('sprout', 'plant', 'leaves', 'growth', 'seedling', 'ground', 'garden', 'nature')

    def build(self) -> None:
        def leaf(name,tip,joint,rx,ry,sweep):
            self.add_arc(name+"-outer",tip,joint,radius_x=rx,radius_y=ry,sweep=sweep)
            self.add_arc(name+"-inner",joint,tip,radius_x=rx,radius_y=ry,sweep=sweep)
            self.add_contour(name,name+"-outer",name+"-inner",closed=True)
            self.relate("connect",name+"-outer","stem")
            self.relate("connect",name+"-inner","stem")
        self.add_arc("top-right",(24,4),(24,20),radius_x=10)
        self.add_arc("top-left",(24,20),(24,4),radius_x=10)
        self.add_contour("top-leaf","top-right","top-left",closed=True)
        self.add_line("stem-upper",(24,20),(24,40))
        self.add_line("stem",(24,40),(24,44))
        self.relate("connect","stem-upper","top-right")
        self.relate("connect","stem-upper","top-left")
        leaf("left-leaf",(8,26),(24,40),16,14,True)
        leaf("right-leaf",(40,26),(24,40),16,14,False)
        for side in ("left-leaf","right-leaf"):
            for part in ("outer","inner"):self.relate("connect","stem-upper",side+"-"+part)
