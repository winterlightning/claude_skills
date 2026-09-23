"""A desktop monitor displaying a single video-call participant."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ec2d4eb4-b488-4b60-b260-7de322e396fd"
SOURCE_PATH = "pictographic-primitives/other/monitor person_ec2d4eb4-b488-4b60-b260-7de322e396fd.svg"
AUTHOR = "gpt-6"


class VideoConferenceMonitor(Solo48):
    icon_id = "video-conference-monitor"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("monitor person", "video call screen")
    keywords = ("desktop", "conference", "meeting", "webcam", "profile")

    def build(self) -> None:
        # The screen has mirrored three-unit corner arcs. Its lower edge is
        # split at the stand and shoulder nodes so contacts are explicit.
        self.add_line("top", (9, 6), (39, 6))
        self.add_arc("ne", (39, 6), (42, 9), radius_x=3)
        self.add_line("right", (42, 9), (42, 31))
        self.add_arc("se", (42, 31), (39, 34), radius_x=3)
        self.add_line("bottom-right-a", (39, 34), (32, 34))
        self.add_line("bottom-right-b", (32, 34), (24, 34))
        self.add_line("bottom-left-b", (24, 34), (16, 34))
        self.add_line("bottom-left-a", (16, 34), (9, 34))
        self.add_arc("sw", (9, 34), (6, 31), radius_x=3)
        self.add_line("left", (6, 31), (6, 9))
        self.add_arc("nw", (6, 9), (9, 6), radius_x=3)
        self.add_contour("screen", "top", "ne", "right", "se",
                         "bottom-right-a", "bottom-right-b", "bottom-left-b",
                         "bottom-left-a", "sw", "left", "nw", closed=True)

        self.add_line("stand", (24, 34), (24, 42))
        self.add_line("foot-left", (16, 42), (24, 42))
        self.add_line("foot-right", (24, 42), (32, 42))
        self.relate("connect", "stand", "bottom-right-b")
        self.relate("connect", "stand", "bottom-left-b")
        self.relate("connect", "stand", "foot-left")
        self.relate("connect", "stand", "foot-right")

        # A compact version of human_ref/user.svg: the head outline ends at
        # y=21 and the shoulders begin at y=29, an exact 4-unit ink gap.
        self.add_arc("head-top", (27, 18), (21, 18), radius_x=3, sweep=False)
        self.add_arc("head-bottom", (21, 18), (27, 18), radius_x=3, sweep=False)
        self.add_contour("head", "head-top", "head-bottom", closed=True)
        self.add_bezier("shoulder-left", (16, 34),
                        ((16, 31), (20, 29), (24, 29)))
        self.add_bezier("shoulder-right", (24, 29),
                        ((28, 29), (32, 31), (32, 34)))
        self.add_contour("shoulders", "shoulder-left", "shoulder-right")
        self.relate("connect", "shoulder-left", "bottom-left-a")
        self.relate("connect", "shoulder-right", "bottom-right-a")
