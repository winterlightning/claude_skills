"""diagonal-chain-link-connector (redraw of the new-pipeline traced SVG).

Plan: Lucide `link-2` (two open capsule brackets + a centre bar) rotated to
the 45-degree diagonal x - y, point-symmetric about (24,24), on SQUARE
(centerline box (6,6)-(42,42)).
- links: one open capsule per end. Cap = r10 arc about an integer centre
  (32,16) / (16,32) whose ends sit on the 6-8-10 lattice points, so the
  sides are the lattice lines x+y=34 and x+y=62 (half-width 9.9). The cap
  apex reaches the keyshape edge exactly: top 6 + right 42 for the upper
  link, left 6 + bottom 42 for the lower one.
- sides run inward to x-y=+-6, leaving the two colinear side ends
  (20,14)/(14,20) and (34,28)/(28,34) 8.49 apart: the link opening.
- connector: the axis x+y=48 from (17,31) to (31,17), inside both capsules,
  9.9 from every side and 8.59 from each cap arc.

Metric issues fixed:
- clearance e0/e1 (3.57) and e1/e2 (3.64): the trace squeezed a thin
  capsule round the bar ends. The capsules are now wide enough for the bar
  to run inside them at 9.9 from the sides, and the bar ends stop 8.59 from
  the caps, so every gap is >= 8 on centerlines.
- stroke-width (info): authored at stroke 4 with gaps budgeted for it.
Dropped: the trace's small inward curls at the link openings (they were the
parts crowding the bar); the openings are plain straight ends like Lucide.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "519a60bc-1eb9-42a3-b501-4f1c01b78a2a"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1151-diagonal-chain-link-connector/"
    "diagonal-chain-link-connector_raw.svg"
)
AUTHOR = "claude-opus-5-5"

R = 10                   # cap radius (6-8-10 lattice ends)
CAP = (32, 16)           # upper link cap centre; lower link = point reflection
OPEN = 6                 # side ends stop at x - y = +-OPEN
BAR_END = (31, 17)       # connector end, 1.41 inside the cap centre


def _mirror(p):
    return (48 - p[0], 48 - p[1])


class DiagonalChainLinkConnectorRedraw(Solo48):
    icon_id = "diagonal-chain-link-connector-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/connection"
    aliases = ("chain link", "link", "hyperlink", "url")
    keywords = ("link", "chain", "connect", "connector", "hyperlink", "url", "attach")

    def _link(self, name: str, flip: bool) -> None:
        cx, cy = CAP
        a = (cx - 6, cy - 8)                 # (26,8)  on x+y=34
        b = (cx + 8, cy + 6)                 # (40,22) on x+y=62
        a_end = ((34 + OPEN) // 2, (34 - OPEN) // 2)   # (20,14)
        b_end = ((62 + OPEN) // 2, (62 - OPEN) // 2)   # (34,28)
        m = _mirror if flip else (lambda p: p)
        self.add_line(f"{name}-side-a", m(a_end), m(a))
        self.add_arc(f"{name}-cap", m(a), m(b), radius_x=R, sweep=True)
        self.add_line(f"{name}-side-b", m(b), m(b_end))
        self.add_contour(name, f"{name}-side-a", f"{name}-cap", f"{name}-side-b")

    def build(self) -> None:
        self._link("link-upper", flip=False)
        self._link("link-lower", flip=True)
        self.add_line("connector", _mirror(BAR_END), BAR_END)
