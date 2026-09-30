"""diagonal-chain-link-rounded (redraw of the new-pipeline traced SVG).

Plan: Lucide `link` (two hooked capsule halves, no centre bar) on the
45-degree diagonal, point-symmetric about (24,24), on SQUARE (centerline
box (6,6)-(42,42)). Each link is one open contour:
- far cap: r10 arc about the integer centre (32,16) with 6-8-10 lattice
  ends (26,8) / (40,22), so the sides lie on x+y=34 and x+y=62 (half-width
  9.9) and the apex reaches the keyshape top 6 and right 42 exactly.
- free side: a short run on x+y=34 ending at (24,10): the link's opening.
- hook side: x+y=62 down to (34,28), then an r10 hook about (28,20)
  (3-4-5 style lattice offset, 8 degree kink like the cap) curling back
  to (22,28), past the diagonal axis and into the other link's opening.
The lower link is the point reflection (x,y) -> (48-x, 48-y).

Metric issues fixed:
- clearance e0/e1 (4.02 on centerlines): the trace's hooks ran round the
  other link's free end. The free sides are shortened to stubs and the
  hooks end at (22,28)/(26,20), so the closest pair (hook vs the other
  link's hook / free end) is 8.44 apart on centerlines.
- stroke-width (info): authored at stroke 4 with gaps budgeted for it.
Changed from the trace: the free sides are shorter than drawn, which is
what makes room for the interlock at 8-unit clearance; a searched family
of longer free sides only passed with the hooks pulled apart (no overlap),
which reads as two separate brackets rather than a chain.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ee4e9e4a-096c-56f9-a0cf-4ffbe3e3593c"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1154-diagonal-chain-link-rounded/"
    "diagonal-chain-link-rounded_raw.svg"
)
AUTHOR = "claude-opus-5-5"

R = 10                    # cap and hook radius
CAP_A, CAP_B = (26, 8), (40, 22)   # 6-8-10 lattice ends about (32,16)
FREE_END = (24, 10)       # free side end on x+y=34
HOOK_START = (34, 28)     # hook side end on x+y=62
HOOK_END = (22, 28)       # r10 about (28,20)


def _mirror(p):
    return (48 - p[0], 48 - p[1])


class DiagonalChainLinkRoundedRedraw(Solo48):
    icon_id = "diagonal-chain-link-rounded-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/connection"
    aliases = ("chain link", "link", "hyperlink", "url")
    keywords = ("link", "chain", "connect", "hyperlink", "url", "attach", "join")

    def _link(self, name: str, flip: bool) -> None:
        m = _mirror if flip else (lambda p: p)
        self.add_line(f"{name}-free", m(FREE_END), m(CAP_A))
        self.add_arc(f"{name}-cap", m(CAP_A), m(CAP_B), radius_x=R, sweep=True)
        self.add_line(f"{name}-side", m(CAP_B), m(HOOK_START))
        self.add_arc(f"{name}-hook", m(HOOK_START), m(HOOK_END), radius_x=R, sweep=True)
        self.add_contour(name, f"{name}-free", f"{name}-cap", f"{name}-side", f"{name}-hook")

    def build(self) -> None:
        self._link("link-upper", flip=False)
        self._link("link-lower", flip=True)
