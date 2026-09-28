"""Demeter, goddess of the harvest: a robed woman holding up a tall grain stalk.

Human construction: icon_set/references/human_ref/full_body_ref.png (the dress figure:
circular outlined head, round-topped flared dress). The head (r5, centre (14,11)) sits
exactly 8 above the robe's crown (14,24) on centerlines (4 visible); the crown is the
nearest body point. The robe is an r4 round top flaring to a hem across the bottom edge
(6..22). The arm runs from the right shoulder (18,28) down to the hand on the stalk
(36,38). The stalk rises the full height with two pairs of branches spreading up and out
(at y=16 and y=28, 8.5 apart), as in the reference sprig.
Lucide construction: 'wheat' (stalk with paired branches); restroom-style robed figure.
Keyshape SQUARE: centerline x 6..42 (hem, branch tip), y 6..42 (head, stalk, hem).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1b451532-820c-4276-ab4a-3f9c1c9b785d"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__demeter-holding-stalk/20260926T044250Z-thuan-mac/reference/demeter_1b451532-820c-4276-ab4a-3f9c1c9b785d.svg"
AUTHOR = "claude-opus-5-5"


class DemeterHoldingStalk(Solo48):
    icon_id = "demeter-holding-stalk"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "mythology/greek"
    aliases = ("demeter", "harvest-goddess", "ceres")
    keywords = ("demeter", "goddess", "harvest", "greek", "mythology", "wheat", "grain", "agriculture", "ceres")

    def build(self) -> None:
        self.add_arc("head-top", (9, 11), (19, 11), radius_x=5, sweep=True)
        self.add_arc("head-bottom", (19, 11), (9, 11), radius_x=5, sweep=True)
        self.add_contour("head", "head-top", "head-bottom", closed=True)
        self.add_arc("robe-crown-right", (14, 24), (18, 28), radius_x=4, sweep=True)
        self.add_line("robe-side-right", (18, 28), (22, 42))
        self.add_line("robe-hem", (22, 42), (6, 42))
        self.add_line("robe-side-left", (6, 42), (10, 28))
        self.add_arc("robe-crown-left", (10, 28), (14, 24), radius_x=4, sweep=True)
        self.add_contour("robe", "robe-crown-right", "robe-side-right", "robe-hem", "robe-side-left",
                         "robe-crown-left", closed=True)
        self.mark_human_figure("demeter", head="head", torso="robe-crown-right", torso_junction="start")
        self.add_line("arm", (18, 28), (36, 38))
        self.add_line("stalk-top", (36, 6), (36, 16))
        self.add_line("stalk-upper", (36, 16), (36, 28))
        self.add_line("stalk-mid", (36, 28), (36, 38))
        self.add_line("stalk-low", (36, 38), (36, 42))
        self.add_contour("stalk", "stalk-top", "stalk-upper", "stalk-mid", "stalk-low")
        self.relate("connect", "robe", "arm")
        self.relate("connect", "arm", "stalk")
        for y, reach in ((16, 6), (28, 5)):
            self.add_line(f"branch-left-{y}", (36, y), (36 - reach, y - reach))
            self.add_line(f"branch-right-{y}", (36, y), (36 + reach, y - reach))
            self.relate("connect", "stalk", f"branch-left-{y}")
            self.relate("connect", "stalk", f"branch-right-{y}")
            self.relate("connect", f"branch-left-{y}", f"branch-right-{y}")
