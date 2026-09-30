"""interlocking-chain-link-symbol-solo-redraw (redraw of the new-pipeline traced SVG).

Plan: SQUARE (suggested, fill 1.0/1.0). Lucide `link` construction: two
identical open links on the x+y=48 diagonal, the lower-left link being the
upper-right one turned 180 degrees about (24,24). Each link is one open
contour: a short free rail, an r10 far cap, the long rail, and an r10 hook
that curls round the link's near end into the other link's opening.
Both links share the rail lines x+y=34 / x+y=62 (half-width 9.9). The caps
are integer r10 arcs with 6-8-10 end points (about 8 degrees off tangent,
the grid-safe cap for a 45 degree tube); the far cap centres (32,16) and
(16,32) put the cardinal apexes exactly on the SQUARE centerline box
(6,6)-(42,42). The hook centre sits 5 back along the axis from the far cap,
so each hook tip passes 9.9 from both rails of the other link.

Metric issues:
- clearance e0/e1 3.63 apart (error): fixed. The hooks are re-centred and
  cut 8 degrees past the axis, so the two links are 8.4+ apart everywhere.
- stroke-width 2.77 (info): redrawn at stroke 4; every gap above was
  measured at the final stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "55bd9f6e-12a9-4d3a-9646-c1852d270efe"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1527-interlocking-chain-link-symbol-solo/interlocking-chain-link-symbol-solo_raw.svg"
AUTHOR = "claude-opus-5-5"

R = 10                 # cap and hook radius (6-8-10 end points)
CAP = (32, 16)         # far cap centre of the upper-right link
HOOK_BACK = 5          # hook centre = CAP moved this far down-left per axis
FREE = 1               # free rail length per axis, as in Lucide's short tail


def _turn(p):
    return (48 - p[0], 48 - p[1])


class InterlockingChainLinkSymbolSoloRedraw(Solo48):
    icon_id = "interlocking-chain-link-symbol-solo-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ("chain link", "hyperlink", "link")
    keywords = ("link", "chain", "url", "hyperlink", "connect", "join", "attachment", "web")

    def build(self) -> None:
        cx, cy = CAP
        hx, hy = cx - HOOK_BACK, cy + HOOK_BACK
        cap_start = (cx - 6, cy - 8)                 # on x+y=34
        free_end = (cap_start[0] - FREE, cap_start[1] + FREE)
        cap_end = (cx + 8, cy + 6)                   # on x+y=62
        rail_end = (hx + 6, hy + 8)                  # on x+y=62
        hook_end = (hx - 8, hy + 6)                  # 8 degrees past the axis
        for name, f in (("ne", lambda p: p), ("sw", _turn)):
            self.add_line(f"{name}-free", f(free_end), f(cap_start))
            self.add_arc(f"{name}-cap", f(cap_start), f(cap_end), radius_x=R, sweep=True)
            self.add_line(f"{name}-rail", f(cap_end), f(rail_end))
            self.add_arc(f"{name}-hook", f(rail_end), f(hook_end), radius_x=R, sweep=True)
            self.add_contour(f"{name}-link", f"{name}-free", f"{name}-cap", f"{name}-rail", f"{name}-hook")
