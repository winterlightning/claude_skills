"""A friendly elephant head with broad ears and a softly rounded trunk."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = "gpt-6"


class ElephantHeadFriendly(Solo48):
    icon_id = "elephant-head-friendly"
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ("elephant-head",)
    keywords = ("elephant", "head", "ears", "trunk", "friendly", "wildlife")

    def build(self) -> None:
        # HRECT_XL centerline extremes: left 2, top 5, right 46, bottom 43.
        self.add_arc("forehead", (14, 15), (34, 15), radius_x=10)
        self.add_line("cheek-right", (34, 15), (34, 25))
        self.add_arc("jaw-right", (34, 25), (30, 29), radius_x=4)
        self.add_line("trunk-right", (30, 29), (30, 37))
        self.add_arc("trunk-tip", (30, 37), (18, 37), radius_x=6)
        self.add_line("trunk-left", (18, 37), (18, 29))
        self.add_arc("jaw-left", (18, 29), (14, 25), radius_x=4)
        self.add_line("cheek-left", (14, 25), (14, 15))
        self.add_contour("face", "forehead", "cheek-right", "jaw-right",
                         "trunk-right", "trunk-tip", "trunk-left", "jaw-left",
                         "cheek-left", closed=True)
        for side, mirror, sweep in (("left", False, False), ("right", True, True)):
            def point(x, y):
                return (48 - x if mirror else x, y)
            members = []
            for name, start, end, rx, ry in (
                ("crest", (14, 15), (8, 11), 6, 4),
                ("upper", (8, 11), (2, 22), 6, 11),
                ("lower", (2, 22), (10, 33), 8, 11),
                ("base", (10, 33), (18, 29), 8, 4),
            ):
                part = f"ear-{side}-{name}"
                self.add_arc(part, point(*start), point(*end),
                             radius_x=rx, radius_y=ry, sweep=sweep)
                members.append(part)
            self.add_contour(f"ear-{side}", *members)
            self.relate("connect", "face", f"ear-{side}")
        self.add_dot("eye-left", (21, 19))
        self.add_dot("eye-right", (27, 19))
