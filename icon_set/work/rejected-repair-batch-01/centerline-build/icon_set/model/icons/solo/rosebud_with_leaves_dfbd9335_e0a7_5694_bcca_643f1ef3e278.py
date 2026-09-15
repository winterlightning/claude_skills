"""A rounded rosebud with an inner curling petal, straight stem, and paired leaves. VRECT extremes (8,4)-(40,44).
Reduction: Opened the leaf interiors and reduced the petal spiral to one curl.
Lucide construction: flower-2, leaf
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dfbd9335-e0a7-5694-bcca-643f1ef3e278'
SOURCE_PATH = 'pictographic-primitives/nature/flower_dfbd9335-e0a7-5694-bcca-643f1ef3e278.svg'
AUTHOR = 'gpt-6'


class RosebudWithLeaves(Solo48):
    icon_id = 'rosebud-with-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-01"
    aliases = ()
    keywords = ('rose', 'rosebud', 'flower', 'bloom', 'stem', 'leaves', 'romance', 'garden')

    def build(self) -> None:
        self.add_arc("bud-top",(11,18),(37,18),radius_x=13,radius_y=14)
        self.add_arc("bud-right",(37,18),(24,32),radius_x=13,radius_y=14)
        self.add_arc("bud-left",(24,32),(11,18),radius_x=13,radius_y=14)
        self.add_contour("bud","bud-top","bud-right","bud-left",closed=True)
        # A quarter-circle folds into a smaller semicircle, forming one petal curl.
        self.add_arc("curl-a",(27,14),(21,20),radius_x=6,sweep=False)
        self.add_arc("curl-b",(21,20),(27,20),radius_x=3,sweep=False)
        self.add_contour("curl","curl-a","curl-b")
        self.add_line("stem",(24,32),(24,44))
        self.relate("connect","stem","bud-right")
        self.relate("connect","stem","bud-left")
        # Paired open leaf strokes retain broad negative space at the stem.
        self.add_arc("leaf-left", (8,39), (24,44), radius_x=16, radius_y=5)
        self.add_arc("leaf-right", (24,44), (40,39), radius_x=16, radius_y=5)
        self.relate("connect", "stem", "leaf-left")
        self.relate("connect", "stem", "leaf-right")
