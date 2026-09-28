from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "9241b7de-9722-4a77-a035-d10d9bdf9d33"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__microphone-podcast-international/20260926T170547Z-thuan-mac-1/reference/microphone podcast international_9241b7de-9722-4a77-a035-d10d9bdf9d33.svg"
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = "microphone-podcast-international"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ("mobile", "phone", "smartphone")

    def build(self) -> None:
        # Centered podcast microphone with globe meridians and sound rays.
        self.add_arc("capsule-left", (21, 10), (21, 24), radius_x=6, radius_y=7, sweep=True)
        self.add_arc("capsule-right", (27, 24), (27, 10), radius_x=6, radius_y=7, sweep=True)
        self.add_line("capsule-top", (27, 10), (21, 10))
        self.add_line("capsule-bottom", (21, 24), (27, 24))
        self.add_contour("microphone", "capsule-left", "capsule-bottom", "capsule-right", "capsule-top", closed=True)
        self.add_line("stand-left", (17, 20), (17, 25))
        self.add_arc("stand-bowl", (17, 25), (31, 25), radius_x=7, radius_y=6, sweep=True)
        self.add_line("stand-right", (31, 25), (31, 20))
        self.add_line("stem", (24, 31), (24, 37))
        self.add_line("base", (18, 38), (30, 38))
        self.add_arc("globe-upper", (11, 17), (37, 17), radius_x=13, radius_y=10, sweep=True)
        self.add_arc("globe-lower", (37, 31), (11, 31), radius_x=13, radius_y=10, sweep=True)
        self.add_line("equator", (11, 24), (15, 24))
        self.add_line("equator-right", (33, 24), (37, 24))
