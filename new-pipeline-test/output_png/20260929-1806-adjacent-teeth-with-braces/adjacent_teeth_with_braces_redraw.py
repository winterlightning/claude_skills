"""Adjacent teeth with braces (redraw of the new-pipeline traced SVG).

Plan: two molars side by side with a white gap between them, a bracket on
each crown and one archwire running through both brackets and across the
gap, on HRECT_L (centerline box (4,8)-(44,40), ink (2,6)-(46,42)).
Everything is mirrored about x=24: the right tooth is the left tooth
mirrored, and each tooth is itself mirrored about its own axis (x=12, x=36).
- tooth: one closed contour. Two crown lobes (8,8)/(16,8) round a shallow
  dip (12,11); rounded shoulders into straight side walls x=4 / x=20 from
  y=16 to y=28 (split at the wire height 22); roots end in tip knots
  (6,40)/(18,40) round a notch whose arch top is (12,33).
- gap: the teeth are 16 wide each and 8 apart on centerlines (4 of white
  ink), 16+8+16 = the 40-unit box width. The inner walls are straight, so
  the 8-unit gap certifies exactly.
- brackets: a hollow square cannot fit (its own sides 8 apart plus 8 to each
  wall needs 24 of the 16-unit tooth), so each bracket is a solid vertical
  bar (12,20)-(12,24), split at the wire. It keeps 8 to both straight side
  walls, 9 to the crown dip and 9 to the notch arch.
- wire: (12,22)-(20,22)-(28,22)-(36,22): bracket, wall node, gap, wall
  node, bracket; every join is a shared endpoint declared with connect.
Height budget: lobe 8, dip 11, gap 9, bracket 20-24, gap 9, notch 33, root
tips 40.
Traced shape: adjacent-teeth-with-braces_raw.svg (read for the subject only;
nothing copied from its coordinates). Lucide: no tooth icon with braces; no
useful match. The root construction follows the repo's
broad-molar-with-two-rounded-roots (outer wall to a tip knot, inner wall up
to a level notch arch). A first draft with the teeth touching at their
widest point also passed, but the kissing walls merged into one thick bar at
48 px, so the gap version was kept.

Metric issues:
- clearance e0/e1 (teeth 2.11 apart): fixed, the inner walls are 8 apart.
- clearance e0/e4, e1/e4 (wire crossing the tooth walls at 0): fixed, the
  wire is split at the walls and ends on shared, declared wall nodes.
- clearance e0/e2, e1/e3 (bracket 3.86 from the root notch): fixed, the
  bracket keeps 9 from the notch arch and 9 from the crown dip.
- hole x8 (slivers 1.8-2.8 wide between brackets, wire and walls): fixed,
  the brackets are solid bars, so each tooth encloses one open interior.
- keyshape-short-axis (y fills 86% of HRECT_M): fixed by moving to HRECT_L;
  a crown dip, bracket and root notch need 32 units of height (9 + 4 + 9
  plus crown and root depth), which HRECT_M's 28 cannot give. Lobes sit on
  y=8, root tips on y=40, outer walls on x=4 and x=44.
- stroke-width (info): drawn at stroke 4; every gap budgeted for 4.
Not kept: the hollow brackets of the generated image (width budget, above).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4fe6a86e-b26a-405a-9e35-84f3c5a12b9e"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1806-adjacent-teeth-with-braces/adjacent-teeth-with-braces_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24            # mirror axis of the pair (centre of the gap)
TA = 12            # left tooth axis
WIRE_Y = 22        # wire height, mid-way down the straight side walls
BRACKET = 2        # bracket half height
SIDE = (16, 28)    # straight run of each side wall

# Left half of the left tooth, from the crown dip round to the notch arch.
# Straight wall pieces are ("line", a, b); curves are (a, c1, c2, b).
HALF = (
    ((12, 11), (10.5, 11), (10, 8), (8, 8)),        # dip -> lobe
    ((8, 8), (5.5, 8), (4, 11), (4, SIDE[0])),      # lobe -> side wall
    ("line", (4, SIDE[0]), (4, WIRE_Y)),            # side wall, split at
    ("line", (4, WIRE_Y), (4, SIDE[1])),            # the wire height
    ((4, SIDE[1]), (4, 34), (5, 40), (6, 40)),      # outer root wall -> tip
    ((6, 40), (8, 40), (9, 33), (12, 33)),          # inner root wall -> notch
)


def mx(seg, axis):
    return tuple(s if s == "line" else (2 * axis - s[0], s[1]) for s in seg)


def reverse(seg):
    return ("line",) + tuple(reversed(seg[1:])) if seg[0] == "line" else tuple(reversed(seg))


def tooth_segments():
    """Left half, then the right half mirrored about the tooth axis."""
    right = [mx(reverse(seg), TA) for seg in reversed(HALF)]
    return list(HALF) + right


class AdjacentTeethWithBracesRedraw(Solo48):
    icon_id = "adjacent-teeth-with-braces-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health/dental"
    aliases = ("braces", "dental-braces", "orthodontics")
    keywords = ("teeth", "tooth", "braces", "orthodontic", "dental", "dentist",
                "bracket", "wire", "molar")

    def build(self) -> None:
        inner_x = 2 * TA - 4                      # left tooth's inner wall x (20)
        gap_l, gap_r = (inner_x, WIRE_Y), (2 * AX - inner_x, WIRE_Y)
        self.add_line("wire-gap", gap_l, gap_r)
        for side, flip in (("l", False), ("r", True)):
            ids = []
            for j, seg in enumerate(tooth_segments()):
                seg = mx(seg, AX) if flip else seg
                eid = f"tooth-{side}-{j}"
                if seg[0] == "line":
                    self.add_line(eid, seg[1], seg[2])
                else:
                    self.add_bezier(eid, seg[0], tuple(seg[1:]))
                ids.append(eid)
            self.add_contour(f"tooth-{side}", *ids, closed=True)

            cx = 2 * AX - TA if flip else TA
            mid = (cx, WIRE_Y)
            wall = gap_r if flip else gap_l
            self.add_line(f"bracket-{side}-top", (cx, WIRE_Y - BRACKET), mid)
            self.add_line(f"bracket-{side}-bottom", mid, (cx, WIRE_Y + BRACKET))
            self.add_line(f"wire-{side}", mid, wall)
            for part in ("top", "bottom"):
                self.relate("connect", f"wire-{side}", f"bracket-{side}-{part}")
            # Members 8 and 9 are the inner wall's two lines meeting at the wire.
            for j in (8, 9):
                self.relate("connect", f"wire-{side}", f"tooth-{side}-{j}")
                self.relate("connect", "wire-gap", f"tooth-{side}-{j}")
            self.relate("connect", "wire-gap", f"wire-{side}")
