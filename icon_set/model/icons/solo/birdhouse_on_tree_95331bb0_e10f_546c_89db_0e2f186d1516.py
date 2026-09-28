"""A pitched birdhouse on a branched tree trunk. VRECT extremes (8,4)-(40,44); mirrored boughs and house sides share the trunk axis.
Reduction: Reduced the arched entrance to a dot; removed cloud-shaped foliage to retain the birdhouse and branching tree structure.
Lucide construction: birdhouse, tree-deciduous
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95331bb0-e10f-546c-89db-0e2f186d1516'
SOURCE_PATH = 'pictographic-primitives/nature/outdoors bird house_95331bb0-e10f-546c-89db-0e2f186d1516.svg'
AUTHOR = 'gpt-6'


class BirdhouseOnTree(Solo48):
    icon_id = 'birdhouse-on-tree'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    categories = ("nature", "primitives")
    aliases = ()
    keywords = ('birdhouse', 'tree', 'bird', 'outdoors', 'garden', 'branches', 'nature', 'nest')

    def build(self) -> None:
        self.add_polyline("house",(12,14),(24,4),(36,14),(36,26),(24,26),(12,26),closed=True)
        self.add_dot("entrance",(24,17))
        self.add_line("trunk-top",(24,26),(24,40))
        self.add_line("trunk-bottom",(24,40),(24,44))
        self.relate("connect","trunk-top","house-4")
        self.relate("connect","trunk-top","house-5")
        self.add_arc("left-bough",(8,34),(24,40),radius_x=16,radius_y=6)
        self.add_arc("right-bough",(24,40),(40,34),radius_x=16,radius_y=6)
        for bough in ("left-bough","right-bough"):
            self.relate("connect",bough,"trunk-top")
            self.relate("connect",bough,"trunk-bottom")
