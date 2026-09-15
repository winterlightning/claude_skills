"""A seedling with two broad pointed leaves meeting one stem. VRECT extremes (8,4)-(40,44); shared leaf nodes and curved lens construction. The larger left leaf and leaning stem deliberately preserve asymmetry.
Reduction: None.
Lucide construction: sprout, leaf
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e171dbe1-be86-576e-b8e3-f9216e53ae72'
SOURCE_PATH = 'pictographic-primitives/nature/plant_e171dbe1-be86-576e-b8e3-f9216e53ae72.svg'
AUTHOR = 'gpt-6'


class SeedlingWithTwoLeaves(Solo48):
    icon_id = 'seedling-with-two-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-02"
    aliases = ()
    keywords = ('seedling', 'sprout', 'plant', 'growth', 'leaves', 'ground', 'garden', 'ecology')

    def build(self) -> None:
        def leaf(name,tip,joint,rx,ry,sweep):
            self.add_arc(name+"-outer",tip,joint,radius_x=rx,radius_y=ry,sweep=sweep)
            self.add_arc(name+"-inner",joint,tip,radius_x=rx,radius_y=ry,sweep=sweep)
            self.add_contour(name,name+"-outer",name+"-inner",closed=True)
            self.relate("connect",name+"-outer","stem")
            self.relate("connect",name+"-inner","stem")
        joint=(26,26)
        self.add_line("stem",joint,(24,44))
        leaf("left-leaf",(8,4),joint,18,22,True)
        leaf("right-leaf",(40,10),joint,14,16,False)
        self.add_polyline("ground",(8,44),(24,44),(40,44))
        self.relate("connect","stem","ground-1")
        self.relate("connect","stem","ground-2")
