"""A top-view beetle inside an arched display dome.

Symbol plan: symmetric dome on x=24; nested beetle with a circular head,
elliptical wing case, and seam. Six legs were attempted and removed after
the dome and neighboring legs failed the SOLO48 clearance check.
SQUARE centerline extremes: (6, 6) to (42, 42).
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "9e1427e3-01db-4b03-91a2-6aedb6775a60"
SOURCE_PATH = "pictographic-primitives/_uncategorized_23/insectarium_9e1427e3-01db-4b03-91a2-6aedb6775a60.svg"
AUTHOR = "gpt-6"


class BeetleInGlassDome(Solo48):
    icon_id = "beetle-in-glass-dome"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/insects"
    aliases = ("insectarium", "beetle display")
    keywords = ("beetle", "bug", "dome", "glass", "specimen")

    def build(self) -> None:
        self.add_line("dome-left", (6, 42), (6, 22))
        self.add_arc("dome-arch", (6, 22), (42, 22), radius_x=18, radius_y=16, sweep=True)
        self.add_line("dome-right", (42, 22), (42, 42))
        self.add_line("dome-base", (42, 42), (6, 42))
        self.add_contour("dome", "dome-left", "dome-arch", "dome-right", "dome-base", closed=True)

        self.add_arc("head-upper", (20, 19), (28, 19), radius_x=4)
        self.add_arc("head-lower", (28, 19), (20, 19), radius_x=4)
        self.add_contour("head", "head-upper", "head-lower", closed=True)

        self.add_arc("shell-upper-right", (24, 23), (32, 28), radius_x=8, radius_y=5)
        self.add_arc("shell-lower-right", (32, 28), (24, 33), radius_x=8, radius_y=5)
        self.add_arc("shell-lower-left", (24, 33), (16, 28), radius_x=8, radius_y=5)
        self.add_arc("shell-upper-left", (16, 28), (24, 23), radius_x=8, radius_y=5)
        self.add_contour("wing-cases", "shell-upper-right", "shell-lower-right", "shell-lower-left", "shell-upper-left", closed=True)
        self.add_line("wing-seam", (24, 23), (24, 33))
        self.relate("connect", "head", "wing-cases")
        self.relate("connect", "wing-seam", "wing-cases")
