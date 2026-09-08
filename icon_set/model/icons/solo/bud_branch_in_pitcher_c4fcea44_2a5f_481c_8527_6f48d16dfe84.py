from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c4fcea44-2a5f-481c-8527-6f48d16dfe84'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-05/vase plant_c4fcea44-2a5f-481c-8527-6f48d16dfe84.svg'
AUTHOR = "gpt-6"


class BudBranchInPitcher(Solo48):
    icon_id = 'bud-branch-in-pitcher'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('bud', 'branch', 'in', 'pitcher')

    def build(self):
        # Centerline extremes: (5, 2) to (43, 46).
        self.add_polyline("pitcher", (22,26), (32,26), (32,46), (8,46), (10,32), (7,26), (22,26))
        self.add_line("stem", (22,26), (22,15))
        self.relate("connect", "stem", "pitcher")
        self.add_polyline("twig", (11,10), (22,20), (32,10))
        self.relate("connect", "twig", "stem")
        self.add_arc("handle", (32,28), (32,42), radius_x=11, radius_y=7)
        self.relate("connect", "handle", "pitcher")
        for name,x,y in [("top",22,5),("left",8,10),("right",35,10)]:
            self.add_arc(name+"-a", (x-3,y), (x+3,y), radius_x=3)
            self.add_arc(name+"-b", (x+3,y), (x-3,y), radius_x=3)
            self.add_contour(name, name+"-a", name+"-b", closed=True)
        self.relate("connect", "left", "twig")
        self.relate("connect", "right", "twig")
