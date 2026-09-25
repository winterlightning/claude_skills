"""Hard-hatted worker beside an open-jaw wrench.
Plan: HRECT_L fits the worker and upright tool side by side. Circular head radius 10 at (16,18) ends at y28; shoulder crest y36 gives exactly 8 centerline / 4 ink gap. Smooth shoulders and open jaws reviewed both themes.
Reduction: Hat rib and tiny collar details omitted. Wrench rings replaced by open jaws for clearer tool identity.
Construction references: human_ref/user.svg: circular face and broad smooth shoulders; head-to-body gap analytically verified. Source supplies helmet and wrench.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "5e90a983-c6c8-4780-99a7-53d2101f43e0"
SOURCE_PATH = 'pictographic-primitives/_uncategorized_24/labor worker_5e90a983-c6c8-4780-99a7-53d2101f43e0.svg'
AUTHOR = "gpt-6"


class ConstructionWorkerWithWrench(Solo48):
    icon_id = 'construction-worker-with-wrench'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("labor worker", "mechanic")
    keywords = ("worker", "helmet", "hard hat", "wrench", "construction")

    def build(self) -> None:
        self.add_arc("hard-hat-dome", (6, 18), (26, 18), radius_x=10, sweep=True)
        self.add_arc("face-lower", (26, 18), (6, 18), radius_x=10, sweep=True)
        self.add_contour("head-and-hat", "hard-hat-dome", "face-lower", closed=True)
        self.add_line("hat-brim", (4, 18), (28, 18))
        self.relate("connect", "hat-brim", "head-and-hat")
        # Circular face bottom y28 and shoulder crest y36 give exactly four units of ink gap.
        self.add_bezier('shoulders',(4,40),((8,36),(12,36),(16,36)),((20,36),(24,36),(28,40)))
        # Two open jaws retain the reference wrench identity without enclosed tiny rings.
        for name,cy,direction in [('top',20,1),('bottom',36,-1)]:
            self.add_line(name+'-left',(36,cy-4*direction),(36,cy))
            self.add_arc(name+'-arc-left',(36,cy),(40,cy+4*direction),radius_x=4,sweep=direction<0)
            self.add_arc(name+'-arc-right',(40,cy+4*direction),(44,cy),radius_x=4,sweep=direction<0)
            self.add_line(name+'-right',(44,cy),(44,cy-4*direction))
            self.add_contour(name+'-jaw',name+'-left',name+'-arc-left',name+'-arc-right',name+'-right')
        self.add_line('wrench-shaft',(40,24),(40,32))
        self.relate('connect','wrench-shaft','top-jaw')
        self.relate('connect','wrench-shaft','bottom-jaw')