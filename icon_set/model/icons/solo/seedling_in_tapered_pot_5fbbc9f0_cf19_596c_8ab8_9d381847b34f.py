"""A seedling with two broad pointed leaves meeting one stem. VRECT extremes (8,4)-(40,44); shared leaf nodes and curved lens construction.
Reduction: Removed the separate pot rim band.
Lucide construction: sprout, leaf
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5fbbc9f0-cf19-596c-8ab8-9d381847b34f'
SOURCE_PATH = 'pictographic-primitives/nature/plant pot_5fbbc9f0-cf19-596c-8ab8-9d381847b34f.svg'
AUTHOR = 'gpt-6'


class SeedlingInTaperedPot(Solo48):
    icon_id = 'seedling-in-tapered-pot'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    categories = ("nature", "primitives")
    aliases = ()
    keywords = ('seedling', 'sprout', 'pot', 'plant', 'potted', 'growth', 'houseplant', 'leaves')

    def build(self) -> None:
        def leaf(name,tip,joint,rx,ry,sweep):
            self.add_arc(name+"-outer",tip,joint,radius_x=rx,radius_y=ry,sweep=sweep)
            self.add_arc(name+"-inner",joint,tip,radius_x=rx,radius_y=ry,sweep=sweep)
            self.add_contour(name,name+"-outer",name+"-inner",closed=True)
            self.relate("connect",name+"-outer","stem")
            self.relate("connect",name+"-inner","stem")
        joint=(24,24)
        self.add_line("stem",joint,(24,32))
        leaf("left-leaf",(8,4),joint,16,20,True)
        leaf("right-leaf",(40,4),joint,16,20,False)
        self.add_polyline("pot",(8,32),(24,32),(40,32),(36,44),(12,44),closed=True)
        self.relate("connect","stem","pot-1")
        self.relate("connect","stem","pot-2")
