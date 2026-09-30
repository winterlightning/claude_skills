"""detective-woman-1-avatar (redraw of the new-pipeline traced SVG).

Plan: a user bust on the left and a magnifying glass on the right (the
Lucide `user-search` idea), on HRECT_M (centerline box (4,10)-(44,38)).
- bust: Lucide `user` construction from icon_set/references/human_ref/user.svg.
  Axis x=13. Flat shoulder line y=28 split at the neck (13,28), r6 corner arcs,
  vertical sides x=4 / x=22 down to the bottom extreme y=38.
- head: 4-cardinal-arc r5 circle on the bust axis, outline exactly 8 above the
  shoulder line (4 units of ink); head top y=10 is the top extreme.
- lens: r5 circle about (37,21) (integer radii only), split at the 3-4-5
  lattice node (40,25) and its opposite (34,17), so the handle shares a node.
- handle: 45-degree line (40,25) -> (44,29); its end is the right extreme
  x=44. It leaves 8 degrees off radial, which reads as radial at 48 px.
The lens sits level with the neck, as in the generated image, >= 13.7 from the
bust and >= 14.7 from the head (centerlines). Gender is not drawn: the faceless stick-figure
brief carries no gender cue (warning already recorded in choice.json).

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4; every gap was budgeted at stroke 4.
- keyshape-short-axis: extremes sit on the HRECT_M box exactly (head top y=10,
  bust feet y=38, bust side x=4, handle end x=44) instead of stretching the trace.
- clearance e0-e3 / head-gap e0 (head vs shoulders 3.26): the head outline is
  exactly 8 above the shoulder line, centred on the bust axis.
- clearance e0-e1 (head vs lens 7.47) and e1-e3 (lens vs shoulders 7.64): the
  lens is >= 14.7 from the head and >= 13.7 from the bust.
- head-gap e1 (the lens misread as a head touching e2): the lens is not a head;
  it is an object whose handle connects to it on purpose (declared connect).
None left unfixed. validate_icon(): valid, no warnings; build_gate: PASS.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e9337ccf-6e62-4109-8b9f-fb9a7582cfcb"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1225-detective-woman-1-avatar/"
    "detective-woman-1-avatar_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 13                 # bust axis x
SHOULDER = 28             # shoulder line y
FOOT = 38                 # bottom extreme
HALF = 9                  # half bust width
CORNER = 6                # shoulder corner radius
HEAD_R = 5                # head centerline radius
HEAD_GAP = 8              # head outline to shoulder line, centerlines (4 ink)
LENS = (37, 21)           # lens centre
LENS_R = 5                # lens radius (3-4-5 lattice)
JOIN = (3, 4)             # handle node offset from the lens centre
HANDLE = 4                # handle run on x and y (45 degrees)


class DetectiveWoman1AvatarRedraw(Solo48):
    icon_id = "detective-woman-1-avatar-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people"
    aliases = ("detective", "investigator", "user search", "find person")
    keywords = ("detective", "woman", "avatar", "investigator", "search", "magnifier", "user")

    def build(self) -> None:
        # Head.
        cy, r = SHOULDER - HEAD_GAP - HEAD_R, HEAD_R
        pts = [(AXIS - r, cy), (AXIS, cy - r), (AXIS + r, cy), (AXIS, cy + r), (AXIS - r, cy)]
        for i in range(4):
            self.add_arc(f"head-{i}", pts[i], pts[i + 1], radius_x=r, sweep=True)
        self.add_contour("head", *(f"head-{i}" for i in range(4)), closed=True)

        # Shoulders: flat line split at the neck, rounded corners, sides.
        for d, s in ((-1, "l"), (+1, "r")):
            top_end = (AXIS + d * (HALF - CORNER), SHOULDER)
            side_top = (AXIS + d * HALF, SHOULDER + CORNER)
            self.add_line(f"top-{s}", (AXIS, SHOULDER), top_end)
            self.add_arc(f"corner-{s}", top_end, side_top, radius_x=CORNER, sweep=d > 0)
            self.add_line(f"side-{s}", side_top, (AXIS + d * HALF, FOOT))
            self.add_contour(f"shoulder-{s}", f"corner-{s}", f"side-{s}")
            self.relate("connect", f"top-{s}", f"shoulder-{s}")
        self.relate("connect", "top-l", "top-r")
        self.mark_human_figure("detective", head="head", torso="top-r", torso_junction="start")

        # Magnifying glass: lens split at the handle node, 45-degree handle.
        lx, ly = LENS
        join, opposite = (lx + JOIN[0], ly + JOIN[1]), (lx - JOIN[0], ly - JOIN[1])
        self.add_arc("lens-a", join, opposite, radius_x=LENS_R)
        self.add_arc("lens-b", opposite, join, radius_x=LENS_R)
        self.add_contour("lens", "lens-a", "lens-b", closed=True)
        self.add_line("handle", join, (join[0] + HANDLE, join[1] + HANDLE))
        self.relate("connect", "lens", "handle")
