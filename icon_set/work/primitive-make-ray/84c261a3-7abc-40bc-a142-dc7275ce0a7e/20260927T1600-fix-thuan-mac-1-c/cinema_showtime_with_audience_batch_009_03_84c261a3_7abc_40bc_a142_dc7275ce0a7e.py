"""Cinema showtime with audience: a large clock above two audience head arches.

Revision of the disapproved drawing, where a frame, curtains and a clock overlapped
into clutter. Plan (SQUARE, centerline (6,6)-(42,42)): clock ring r13 about (24,19)
with hour hand to (24,15) and minute hand to (28,19) (tips 9 inside the ring); two
audience arches r5 from (6,42)-(16,42) and (32,42)-(42,42) whose apexes keep 9.2 units
from the ring. The reference's screen frame, curtains and third arch are omitted: a
clock with readable hands needs r13, which leaves no 8-unit room for them. Lucide
`clock` informs the ring and hands.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "84c261a3-7abc-40bc-a142-dc7275ce0a7e"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__cinema-showtime-with-audience-batch-009-03/20260927T150749Z-thuan-mac-1/reference/movie cinema clock_84c261a3-7abc-40bc-a142-dc7275ce0a7e.svg"
AUTHOR = "claude-fable-5-1"


class CinemaShowtimeWithAudience(Solo48):
    icon_id = "cinema-showtime-with-audience-batch-009-03"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    aliases = ("movie showtime", "cinema clock")
    keywords = ("cinema", "showtime", "audience", "clock", "movie", "theater", "time")

    def build(self) -> None:
        cx, cy, r = 24, 19, 13
        pts = [(cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)]
        for j in range(4):
            self.add_arc(f"ring-{j}", pts[j], pts[(j + 1) % 4], radius_x=r)
        self.add_contour("ring", "ring-0", "ring-1", "ring-2", "ring-3", closed=True)
        self.add_polyline("hands", (24, 15), (24, 19), (28, 19))
        self.add_arc("audience-left", (6, 42), (16, 42), radius_x=5)
        self.add_arc("audience-right", (32, 42), (42, 42), radius_x=5)
