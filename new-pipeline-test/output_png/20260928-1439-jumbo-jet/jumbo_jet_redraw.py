"""jumbo-jet (redraw of the new-pipeline traced SVG).

Plan: top-down airliner flying up-right on SQUARE (centerline box (6,6)-(42,42)),
mirrored exactly about its own axis x+y=48 with M(x,y) = (48-y, 48-x).
- fuselage: two 45-degree sides, upper on x+y=42 and lower on x+y=54
  (8.49 apart, the narrowest outlined tube that clears 8 between centerlines);
  quarter-arc nose r6 about (36,12) sits on the x=42 / y=6 extremes, quarter-arc
  tail r6 about (16,32) closes the rear right behind the tailplanes.
- wings: one swept triangle per side, closed by the fuselage side segment
  between its roots; the pointed tips are the x=6 / y=42 extremes.
- tailplanes: a small swept triangle per side with a pointed tip like the
  wings, closed by the fuselage side segment between its
  roots, sitting at the very end of the fuselage: its trailing root is where
  the tail cap starts, with no fuselage stub behind it.
  It is the smallest pointed fin whose hole clears the 6-unit floor
  (inradius 3.05) while its leading edge stays 8 from the wing's trailing edge.
One closed silhouette contour carries the outline; the four root segments of the
fuselage sides are loose lines connected at both ends.
Fixed from the trace metrics: the fuselage was 6.6 wide, every wing / tail hole
was 2.7-4 wide and the tailplanes sat 4.2 from each other at the tail. The
fuselage is widened to 8.49; the wing moved two steps forward to leave 8 between
its trailing edge and the tailplane's leading edge.
Review history: pointed triangle tailplanes, open notched fins, and trapezoid
tailplanes with a fuselage stub behind them were all rejected; the user asked
for the two tailplanes at the very end of the body, with sharp tips.
Lucide `plane` informed the rounded nose and swept, pointed wing tips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1439-jumbo-jet/jumbo-jet_raw.svg"
AUTHOR = "claude-opus-5-5"

NOSE_R = 6
NOSE_A = (36, 6)            # upper side meets nose, arc centre (36,12)
TAIL_R = 6
TAIL_A = (10, 32)           # tail cap starts at the tailplane trailing root, arc centre (16,32)
WING_LEAD = (32, 10)        # upper wing roots on x+y=42
WING_TRAIL = (24, 18)
WING_TIP = (6, 10)
TAILPLANE_LEAD = (17, 25)   # upper tailplane roots on x+y=42
TAILPLANE_TRAIL = TAIL_A
TAILPLANE_TIP = (6, 22)         # pointed tip


def m(p):
    return (48 - p[1], 48 - p[0])


class JumboJetRedraw(Solo48):
    icon_id = "jumbo-jet-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/aircraft"
    aliases = ("airliner", "jet airliner", "passenger jet", "airplane", "plane")
    keywords = ("jumbo jet", "jet", "airplane", "plane", "flight", "aircraft", "travel", "airport")

    def build(self) -> None:
        # Silhouette, from the nose's upper end down the upper side to the tail.
        pts = [
            NOSE_A, WING_LEAD, WING_TIP, WING_TRAIL, TAILPLANE_LEAD,
            TAILPLANE_TIP, TAIL_A,
        ]
        members = []
        for i, (a, b) in enumerate(zip(pts, pts[1:])):
            self.add_line(f"upper-{i}", a, b)
            members.append(f"upper-{i}")
        self.add_arc("tail", TAIL_A, m(TAIL_A), radius_x=TAIL_R, sweep=False)
        members.append("tail")
        low = [m(p) for p in reversed(pts)]
        for i, (a, b) in enumerate(zip(low, low[1:])):
            self.add_line(f"lower-{i}", a, b)
            members.append(f"lower-{i}")
        self.add_arc("nose", m(NOSE_A), NOSE_A, radius_x=NOSE_R, sweep=False)
        members.append("nose")
        self.add_contour("silhouette", *members, closed=True)

        # Fuselage side segments behind the wing and tailplane roots.
        for side, f in (("upper", lambda p: p), ("lower", m)):
            self.add_line(f"{side}-wing-root", f(WING_LEAD), f(WING_TRAIL))
            self.add_line(f"{side}-tail-root", f(TAILPLANE_LEAD), f(TAILPLANE_TRAIL))
            self.relate("connect", f"{side}-wing-root", "silhouette")
            self.relate("connect", f"{side}-tail-root", "silhouette")
