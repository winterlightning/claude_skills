"""A desktop monitor displaying a single video-call participant."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "ec2d4eb4-b488-4b60-b260-7de322e396fd"
SOURCE_PATH = "pictographic-primitives/other/monitor person_ec2d4eb4-b488-4b60-b260-7de322e396fd.svg"
AUTHOR = "claude-fable-5-1"


class VideoConferenceMonitor(Solo48):
    icon_id = "video-conference-monitor"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ("monitor person", "video call screen")
    keywords = ("desktop", "conference", "meeting", "webcam", "profile")

    def build(self) -> None:
        # Monitor on VRECT_L: a 32x32 screen (y 4-36) over an 8-unit stand and
        # feet at y=44. SQUARE's 28-unit screen cannot hold a head, its 4-unit
        # gap, the shoulders and the pocket beneath them.
        self.add_line("top", (11, 4), (37, 4))
        self.add_arc("ne", (37, 4), (40, 7), radius_x=3)
        self.add_line("right", (40, 7), (40, 33))
        self.add_arc("se", (40, 33), (37, 36), radius_x=3)
        self.add_line("bottom-right-a", (37, 36), (31, 36))
        self.add_line("bottom-right-b", (31, 36), (24, 36))
        self.add_line("bottom-left-b", (24, 36), (17, 36))
        self.add_line("bottom-left-a", (17, 36), (11, 36))
        self.add_arc("sw", (11, 36), (8, 33), radius_x=3)
        self.add_line("left", (8, 33), (8, 7))
        self.add_arc("nw", (8, 7), (11, 4), radius_x=3)
        self.add_contour("screen", "top", "ne", "right", "se",
                         "bottom-right-a", "bottom-right-b", "bottom-left-b",
                         "bottom-left-a", "sw", "left", "nw", closed=True)

        self.add_line("stand", (24, 36), (24, 44))
        self.add_line("foot-left", (16, 44), (24, 44))
        self.add_line("foot-right", (24, 44), (32, 44))
        self.relate("connect", "stand", "bottom-right-b")
        self.relate("connect", "stand", "bottom-left-b")
        self.relate("connect", "stand", "foot-left")
        self.relate("connect", "stand", "foot-right")

        # human_ref/user.svg reduced: a complete 4-unit head (ink 13-17) and an
        # elliptical shoulder arc whose apex at y=26 leaves an exact 4-unit ink
        # gap below the head and a 6-unit pocket above the screen edge.
        self.add_arc("head-top", (26, 15), (22, 15), radius_x=2, sweep=False)
        self.add_arc("head-bottom", (22, 15), (26, 15), radius_x=2, sweep=False)
        self.add_contour("head", "head-top", "head-bottom", closed=True)
        self.add_arc("shoulders", (17, 36), (31, 36), radius_x=7, radius_y=10, sweep=True)
        self.relate("connect", "shoulders", "bottom-left-a")
        self.relate("connect", "shoulders", "bottom-right-a")
        self.mark_human_figure("person", head="head", torso="shoulders", torso_junction="start")
