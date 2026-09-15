"""A cloud-shaped bonsai canopy and curved trunk rise from a shallow pot. VRECT extremes (8,4)-(40,44); canopy lobes mirror about x=24.
Reduction: Reduced the trunk to one S-curving stroke and removed the pot rim band.
Lucide construction: tree-deciduous, cloud
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c19ebb9b-05e5-5119-8ac2-6bb97be01613'
SOURCE_PATH = 'pictographic-primitives/nature/plant bonsai_c19ebb9b-05e5-5119-8ac2-6bb97be01613.svg'
AUTHOR = 'gpt-6'


class BonsaiInShallowPot(Solo48):
    icon_id = 'bonsai-in-shallow-pot'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-02"
    aliases = ()
    keywords = ('bonsai', 'tree', 'pot', 'plant', 'miniature', 'japanese', 'garden', 'houseplant')

    def build(self) -> None:
        self.add_arc("top",(18,10),(30,10),radius_x=6)
        self.add_arc("right",(30,10),(30,20),radius_x=5)
        self.add_line("base-right",(30,20),(24,20))
        self.add_line("base-left",(24,20),(18,20))
        self.add_arc("left",(18,20),(18,10),radius_x=5)
        self.add_contour("canopy","top","right","base-right","base-left","left",closed=True)
        self.add_arc("trunk-top",(24,20),(24,28),radius_x=4)
        self.add_arc("trunk-bottom",(24,28),(24,36),radius_x=4,sweep=False)
        self.add_contour("trunk","trunk-top","trunk-bottom")
        self.relate("connect","trunk-top","base-right")
        self.relate("connect","trunk-top","base-left")
        self.add_polyline("pot",(8,36),(24,36),(40,36),(36,44),(12,44),closed=True)
        self.relate("connect","trunk-bottom","pot-1")
        self.relate("connect","trunk-bottom","pot-2")
