"""A hard-hatted worker bust beside an upright double-ended wrench.

Symbol plan: worker at left, tool at right; the worker has a shared-axis hard
hat and circular lower face, detached by exactly 8 centerline units from the
shoulder crest. HRECT_L extremes x=4..44, y=8..40.
Human style: icon_set/references/human_ref/user.svg.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5e90a983-c6c8-4780-99a7-53d2101f43e0"
SOURCE_PATH = "pictographic-primitives/_uncategorized_24/labor worker_5e90a983-c6c8-4780-99a7-53d2101f43e0.svg"
AUTHOR = "gpt-6"


class ConstructionWorkerWithWrench(Solo48):
    icon_id = "construction-worker-with-wrench"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/occupations"
    aliases = ("labor worker", "mechanic")
    keywords = ("worker", "helmet", "hard hat", "wrench", "construction")

    def build(self) -> None:
        self.add_arc("hard-hat-dome", (8, 16), (24, 16), radius_x=8, sweep=True)
        self.add_arc("face-lower", (24, 16), (8, 16), radius_x=8, sweep=True)
        self.add_contour("head-and-hat", "hard-hat-dome", "face-lower", closed=True)
        self.add_line("hat-brim", (6, 16), (26, 16))
        self.relate("connect", "hat-brim", "head-and-hat")
        self.add_line("hard-hat-rib", (16, 8), (16, 16))
        self.relate("connect", "hard-hat-rib", "head-and-hat")
        self.relate("connect", "hard-hat-rib", "hat-brim")
        self.add_polyline("shoulders", (4, 40), (8, 34), (16, 32), (24, 34), (28, 40))

        for name, cy in (("top", 20), ("bottom", 36)):
            self.add_arc(f"wrench-{name}-upper", (36, cy), (44, cy), radius_x=4, sweep=True)
            self.add_arc(f"wrench-{name}-lower", (44, cy), (36, cy), radius_x=4, sweep=True)
            self.add_contour(f"wrench-{name}-head", f"wrench-{name}-upper", f"wrench-{name}-lower", closed=True)
        self.add_line("wrench-shaft", (40, 24), (40, 32))
        self.relate("connect", "wrench-shaft", "wrench-top-head")
        self.relate("connect", "wrench-shaft", "wrench-bottom-head")
