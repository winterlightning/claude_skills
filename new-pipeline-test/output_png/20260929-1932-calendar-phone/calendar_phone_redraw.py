"""Calendar phone (redraw of the new-pipeline traced SVG).

Plan: a tall rounded smartphone outline with a Lucide-style calendar page
centred inside it, on VRECT_L (centerline box (8,4)-(40,44)).
- phone: four standalone edge lines (x=8, x=40, y=4, y=44) joined by four r6
  corner arcs; every extreme sits on the keyshape box.
- calendar: one closed r2 rounded rectangle (16,16)-(32,36), 8 in from both
  phone side walls and 8 above the phone bottom; its outline has nodes at
  the header ends and at both tab feet.
- header: straight line y=26 across the calendar, splitting it into two 10-high
  bands (the minimum that keeps both openings at least 6 inscribed).
- tabs: two binding tabs x=20 and x=28 (8 apart), crossing the calendar top
  like Lucide `calendar`, from y=12 (8 below the phone top) to y=18 (8 above
  the header).
Lucide `calendar` (tabs crossing the top edge, header rule) and `smartphone`
(tall rounded body) informed the construction, redrawn on this grid.

Keyshape: the metrics suggested VRECT_M (score 1.10 vs VRECT_L 0.99). On
VRECT_M the phone interior leaves a calendar only 12 wide, so the two tabs
(which must be 8 apart) land on its rounded corners and the page reads as a
battery; VRECT_L gives a 16-wide page whose tabs sit at 1/4 and 3/4, as in the
reference. VRECT_L was chosen for that reason.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4; every gap was re-budgeted at 8.
- keyshape-short-axis: the phone walls sit on x=8/x=40 and y=4/y=44, so all four
  extremes are exactly on the VRECT_L box (no stretch needed).
- clearance e0/e1, e0/e5 (calendar and header 3 from the phone wall): the
  calendar is now 8 from both side walls and the bottom wall.
- clearance e0/e2, e0/e3, e0/e4 (tabs 7.3 from the phone): tab tips are 8
  below the phone top and 12 from the side walls.
- clearance e1/e4 and the split tab e2/e3: each tab is one line joined to the
  calendar top at a shared node (connect), not a loose touch.
- clearance e1/e5, e2/e5, e3/e5, e4/e5 (header 4.5 below the top, tabs 2.8
  above it): the header is 10 below the calendar top and 8 below the tab ends.
- hole at (21.7, 18.4) 0.6 wide: the sliver came from a tab overlapping the
  header band; both openings are now 12x6 ink (6 inscribed) or larger.
Not reproduced: the reference's thin-stroke proportions (a page wider than
tall with its header high up). At stroke 4 the 40-unit height only fits
8 + tab 4 + 10 + 10 + 8, so the header sits at mid-page.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "fd8eb806-4d12-4ad0-bb86-c0aaf66d08bc"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1932-calendar-phone/calendar-phone_raw.svg"
AUTHOR = "claude-opus-5-5"

LEFT, RIGHT, TOP, BOTTOM = 8, 40, 4, 44   # phone = VRECT_L centerline box
PHONE_R = 6
GAP = 8                                   # SOLO48 centerline clearance
CAL_L, CAL_R = LEFT + GAP, RIGHT - GAP    # 16, 32
CAL_T, CAL_B = 16, BOTTOM - GAP           # 16, 36
CAL_R_CORNER = 2
HEADER_Y = CAL_T + 10                     # 26: two 10-high bands
TABS = (20, 28)
TAB_TOP, TAB_BOTTOM = TOP + GAP, HEADER_Y - GAP   # 12, 18


class CalendarPhoneRedraw(Solo48):
    icon_id = "calendar-phone-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("calendar app", "mobile calendar", "phone schedule")
    keywords = ("calendar", "phone", "smartphone", "mobile", "schedule", "date", "app")

    def phone(self) -> None:
        l, r, t, b, k = LEFT, RIGHT, TOP, BOTTOM, PHONE_R
        self.add_line("phone-top", (l + k, t), (r - k, t))
        self.add_arc("phone-corner-tr", (r - k, t), (r, t + k), radius_x=k)
        self.add_line("phone-right", (r, t + k), (r, b - k))
        self.add_arc("phone-corner-br", (r, b - k), (r - k, b), radius_x=k)
        self.add_line("phone-bottom", (r - k, b), (l + k, b))
        self.add_arc("phone-corner-bl", (l + k, b), (l, b - k), radius_x=k)
        self.add_line("phone-left", (l, b - k), (l, t + k))
        self.add_arc("phone-corner-tl", (l, t + k), (l + k, t), radius_x=k)
        ring = ("phone-top", "phone-corner-tr", "phone-right", "phone-corner-br",
                "phone-bottom", "phone-corner-bl", "phone-left", "phone-corner-tl")
        for a, b in zip(ring, ring[1:] + ring[:1]):
            self.relate("connect", a, b)

    def calendar(self) -> None:
        l, r, t, b, k, h = CAL_L, CAL_R, CAL_T, CAL_B, CAL_R_CORNER, HEADER_Y
        nodes = [(l, h), (l, t + k), (l + k, t), (TABS[0], t), (TABS[1], t),
                 (r - k, t), (r, t + k), (r, h), (r, b - k), (r - k, b),
                 (l + k, b), (l, b - k)]
        corners = {1, 5, 8, 10}
        members = []
        for i, p in enumerate(nodes):
            q = nodes[(i + 1) % len(nodes)]
            name = f"calendar-{i}"
            if i in corners:
                self.add_arc(name, p, q, radius_x=k)
            else:
                self.add_line(name, p, q)
            members.append(name)
        self.add_contour("calendar", *members, closed=True)
        self.add_line("header", (l, h), (r, h))
        self.relate("connect", "calendar", "header")
        for x in TABS:
            self.add_line(f"tab-{x}", (x, TAB_TOP), (x, TAB_BOTTOM))
            self.relate("connect", "calendar", f"tab-{x}")

    def build(self) -> None:
        self.phone()
        self.calendar()
