"""bittorrent-concentric-open-emblem (redraw of the new-pipeline traced SVG).

Plan: concentric open emblem on CIRCLE (centerline radius 20 about (24,24)).
- outer C: arc r20 about (24,24) from (40,36) round the left to (40,12);
  its left point (4,24) and top/bottom (24,4)/(24,44) are the radial extremes.
  The ends sit on the 3-4-5 direction (16,+-12), so the opening faces right
  at +-37 degrees, like the generated image.
- inner C: arc r10 about the same centre from (32,30) to (32,18); the ends
  use the same (8,+-6) direction, so both openings are aligned on one ray.
- centre: a dot at (24,24).
Every part is concentric and mirrored about y=24; gaps are 10 on
centerlines (ink 6) between outer and inner C, and between inner C and dot.
No useful Lucide match beyond `radio`/`circle-dot` style concentric rings;
taken from them only the shared-centre construction.

Metric issues fixed:
- stroke-width: redrawn at stroke 4; every gap budgeted at >= 8 centerline.
- clearance e0/e1 (6.57): the two C arcs are now 10 apart (r20 vs r10).
- clearance e1/e2 (6.63): the centre mark is now 10 from the inner C.

Not kept as traced: the centre was a hollow ring in the image. A hollow
centre needs r >= 4 (smallest outlined circle), then the inner C needs
r >= 12 and the outer C r >= 20: exactly 8 twice with no slack, and r12 has
no integer points off the axes, so its ends could not sit on the grid at
the image's opening angle (only a semicircle). The ring became a dot so
both openings stay aligned and every gap has slack.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7d8f95ed-27bc-4a59-85e2-137bb75f8ea9"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1714-bittorrent-concentric-open-emblem/"
    "bittorrent-concentric-open-emblem_raw.svg"
)
AUTHOR = "claude-opus-5-5"

CENTRE = (24, 24)
OUTER_R, OUTER_END = 20, (16, 12)   # 3-4-5 direction, +-37 degrees
INNER_R, INNER_END = 10, (8, 6)     # same direction, aligned opening


class BittorrentConcentricOpenEmblemRedraw(Solo48):
    icon_id = "bittorrent-concentric-open-emblem-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/software"
    aliases = ("bittorrent", "concentric emblem", "open rings")
    keywords = ("bittorrent", "torrent", "logo", "concentric", "rings", "emblem", "p2p")

    def open_c(self, name, r, end):
        cx, cy = CENTRE
        dx, dy = end
        self.add_arc(name, (cx + dx, cy + dy), (cx + dx, cy - dy),
                     radius_x=r, large_arc=True, sweep=True)

    def build(self) -> None:
        self.open_c("outer", OUTER_R, OUTER_END)
        self.open_c("inner", INNER_R, INNER_END)
        self.add_dot("centre", CENTRE)
