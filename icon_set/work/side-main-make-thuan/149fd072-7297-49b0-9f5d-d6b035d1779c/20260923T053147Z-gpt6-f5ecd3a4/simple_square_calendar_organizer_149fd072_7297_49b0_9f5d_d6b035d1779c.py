"""An empty calendar page with two binding tabs."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "149fd072-7297-49b0-9f5d-d6b035d1779c"
SOURCE_PATH = "pictographic-primitives/interface-essential/calendar_149fd072-7297-49b0-9f5d-d6b035d1779c.svg"
AUTHOR = "gpt-6"


class SimpleSquareCalendarOrganizer(Solo48):
    icon_id = "simple-square-calendar-organizer"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/calendar"
    aliases = ("calendar", "date planner")
    keywords = ("appointment", "schedule", "organizer")

    def build(self) -> None:
        # A radius-four page frame with a split top edge for paired tabs and
        # split side edges for the full-width header divider.
        frame = []
        def line(name, a, b):
            self.add_line(name, a, b); frame.append(name)
        def arc(name, a, b):
            self.add_arc(name, a, b, radius_x=4); frame.append(name)
        line("top-left", (10, 10), (16, 10))
        line("top-center", (16, 10), (32, 10))
        line("top-right", (32, 10), (38, 10))
        arc("corner-ne", (38, 10), (42, 14))
        line("right-header", (42, 14), (42, 22))
        line("right-body", (42, 22), (42, 38))
        arc("corner-se", (42, 38), (38, 42))
        line("bottom", (38, 42), (10, 42))
        arc("corner-sw", (10, 42), (6, 38))
        line("left-body", (6, 38), (6, 22))
        line("left-header", (6, 22), (6, 14))
        arc("corner-nw", (6, 14), (10, 10))
        self.add_contour("page-frame", *frame, closed=True)
        for x, side, top in ((16, "left", "top-left"), (32, "right", "top-center")):
            self.add_line(f"{side}-tab-above", (x, 6), (x, 10))
            self.add_line(f"{side}-tab-below", (x, 10), (x, 14))
            self.relate("connect", f"{side}-tab-above", top)
            self.relate("connect", f"{side}-tab-below", top)
        self.add_line("header-divider", (6, 22), (42, 22))
        self.relate("connect", "header-divider", "left-body")
        self.relate("connect", "header-divider", "right-header")
