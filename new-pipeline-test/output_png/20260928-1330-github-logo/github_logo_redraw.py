"""github-logo (redraw of the new-pipeline traced SVG).

Plan: the Octocat seen from behind, one closed silhouette on VRECT_L
(centerline box (8,4)-(40,44)), mirrored about x=24 except the tail.
- head: broad round head, widest at y=19 on x=8 / x=40, two pointed ears
  whose tips reach y=4, a shallow crown between the inner ear bases.
- body: straight walls at x=16 and x=32 drop from the neck corners (y=28)
  to y=40 and close with two r4 half-circle feet that meet at (24,40).
- leg split: a short line up from the feet junction, 8 from each wall.
- tail: one stroke hooking right and up from the right foot junction; its
  tip stays 8+ clear of the head.
Traced shape: 20260928-1330-github-logo/github-logo_raw.svg (the body walls
are widened from the trace so the leg split clears both walls).
No useful Lucide match: lucide/github is the face-in-circle mark, not this
full-body silhouette.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1330-github-logo/github-logo_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
NECK_Y = 28      # head bottom meets the body walls
WALL_DX = 8      # walls at AXIS -/+ 8
FOOT_Y = 40      # walls end, feet begin
FOOT_R = 4       # half-circle feet, bottom at y=44
SPLIT_TOP = 36


def mirror(p):
    return (2 * AXIS - p[0], p[1])


class GithubLogoRedraw(Solo48):
    icon_id = "github-logo-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ("octocat",)
    keywords = ("github", "octocat", "git", "logo", "brand", "developer", "code", "cat")

    def build(self) -> None:
        wl, wr = AXIS - WALL_DX, AXIS + WALL_DX
        neck_l, neck_r = (wl, NECK_Y), (wr, NECK_Y)
        widest = (8, 19)
        ear_base = (10, 12)
        ear_tip = (10, 4)
        inner = (17, 8)

        # Left half of the head, from the neck corner up to the crown.
        left = [
            ("head-l1", neck_l, ((11, 27), (8, 24), widest)),
            ("head-l2", widest, ((8, 16), (9, 14), ear_base)),
            ("ear-l-out", ear_base, ((9, 9), (9, 6), ear_tip)),
            ("ear-l-in", ear_tip, ((13, 4.5), (15.5, 6), inner)),
        ]
        for name, start, (c1, c2, end) in left:
            self.add_bezier(name, start, (c1, c2, end))
        self.add_bezier("crown", inner, ((21, 6.5), (27, 6.5), mirror(inner)))
        # Right half: mirrored, walked back down to the right neck corner.
        right_names = []
        for name, start, (c1, c2, end) in reversed(left):
            rname = name.replace("-l", "-r")
            self.add_bezier(rname, mirror(end), (mirror(c2), mirror(c1), mirror(start)))
            right_names.append(rname)

        self.add_line("wall-r", neck_r, (wr, FOOT_Y))
        self.add_arc("foot-r", (wr, FOOT_Y), (AXIS, FOOT_Y), radius_x=FOOT_R, sweep=True)
        self.add_arc("foot-l", (AXIS, FOOT_Y), (wl, FOOT_Y), radius_x=FOOT_R, sweep=True)
        self.add_line("wall-l", (wl, FOOT_Y), neck_l)
        self.add_contour(
            "cat",
            *[n for n, *_ in left], "crown", *right_names,
            "wall-r", "foot-r", "foot-l", "wall-l",
            closed=True,
        )

        self.add_line("split", (AXIS, FOOT_Y), (AXIS, SPLIT_TOP))
        self.relate("connect", "split", "cat")

        self.add_bezier("tail", (wr, FOOT_Y), ((37, 41), (40, 38), (40, 32)))
        self.relate("connect", "tail", "cat")
