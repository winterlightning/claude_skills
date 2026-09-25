"""A seedling with two broad pointed leaves meeting one stem. VRECT extremes (8,4)-(40,44); shared leaf nodes and curved lens construction.
Reduction: Removed leaf veins to preserve open leaf interiors.
Lucide construction: sprout, leaf
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dd0e8ee8-e696-581d-8388-71b1b1304a70'
SOURCE_PATH = 'pictographic-primitives/nature/plant_dd0e8ee8-e696-581d-8388-71b1b1304a70.svg'
AUTHOR = 'gpt-6'


class SproutingSeedling(Solo48):
    icon_id = 'sprouting-seedling'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    aliases = ()
    keywords = ('seedling', 'sprout', 'plant', 'growth', 'leaves', 'ground', 'garden', 'ecology')

    def build(self) -> None:
        def leaf(name,tip,joint,rx,ry,sweep):
            self.add_arc(name+"-outer",tip,joint,radius_x=rx,radius_y=ry,sweep=sweep)
            self.add_arc(name+"-inner",joint,tip,radius_x=rx,radius_y=ry,sweep=sweep)
            self.add_contour(name,name+"-outer",name+"-inner",closed=True)
            self.relate("connect",name+"-outer","stem")
            self.relate("connect",name+"-inner","stem")
        joint=(24,24)
        self.add_line("stem",joint,(24,44))
        leaf("left-leaf",(8,4),joint,16,20,True)
        leaf("right-leaf",(40,4),joint,16,20,False)
        self.add_polyline("ground",(8,44),(24,44),(40,44))
        self.relate("connect","stem","ground-1")
        self.relate("connect","stem","ground-2")
