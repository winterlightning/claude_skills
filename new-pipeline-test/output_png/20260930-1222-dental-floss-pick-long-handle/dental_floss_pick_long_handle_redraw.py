"""dental-floss-pick-long-handle (redraw of the new-pipeline traced SVG).

Subject: a dental floss pick, a U-shaped fork whose two prong tips hold one
straight floss strand, on a long straight handle.

Plan on VRECT_M (the metrics suggestion; centerline box (10,4)-(38,44)), one
axis at x=24, mirrored left/right. Drawn in single strokes (Lucide style):
the traced hollow outline cannot hold stroke 4 at 48 (its fork hole is 3.98).
- prongs: short vertical nubs (10,4)-(10,FLOSS_Y) and (38,4)-(38,FLOSS_Y), so
  the tips stand above the floss like the posts in the image.
- fork: two circular quarter arcs, r=FORK_R=14, centre (24,FLOSS_Y), tangent
  to the nubs, meeting at the neck (24,22) - the deep U of the image.
- floss: straight line between the prong tips at y=FLOSS_Y, sharing the
  nub/arc endpoints.
- handle: straight line from the neck to y=44 (22 long, longer than the
  18-tall fork; a flatter ry=11 fork was tried and read as a bowl).

Metric issues:
- hole (3.98 inscribed, need 6) -> fixed: the floss/fork opening is now
  a half disc r=14 on centerlines, 10 ink high inscribed; the handle is a
  single stroke so it has no hole.
- keyshape-short-axis (x filled 47%) -> fixed: the fork is widened to the
  box, prong nubs on x=10 and x=38; nubs top y=4, handle end y=44 (exact fit).
- stroke-width (info, 2.64 traced) -> redrawn at stroke 4; every gap budgeted
  at 4 ink.
Reference: no Lucide floss pick exists; construction follows Lucide's
single-stroke tool icons (fork arcs tangent to straight prongs, T-joined stem).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "04874150-d969-4dd6-b73e-e5bb09d38c9d"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1222-dental-floss-pick-long-handle/"
    "dental-floss-pick-long-handle_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AX = 24            # shared axis
LEFT, RIGHT = 10, 38
TOP, BOTTOM = 4, 44
FLOSS_Y = 8        # floss strand; nubs rise 4 above it
FORK_R = AX - LEFT  # 14: fork reaches the box sides
NECK = (AX, FLOSS_Y + FORK_R)


class DentalFlossPickLongHandleRedraw(Solo48):
    icon_id = "dental-floss-pick-long-handle-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health/dental"
    aliases = ("floss pick", "dental floss", "flosser")
    keywords = ("dental", "floss", "pick", "flosser", "teeth", "hygiene", "dentist")

    def build(self) -> None:
        left_tip, right_tip = (LEFT, FLOSS_Y), (RIGHT, FLOSS_Y)
        self.add_line("nub-left", (LEFT, TOP), left_tip)
        self.add_arc("fork-left", left_tip, NECK, radius_x=FORK_R, sweep=False)
        self.add_arc("fork-right", NECK, right_tip, radius_x=FORK_R, sweep=False)
        self.add_line("nub-right", right_tip, (RIGHT, TOP))
        self.add_contour("fork", "nub-left", "fork-left", "fork-right", "nub-right")

        self.add_line("floss", left_tip, right_tip)
        self.relate("connect", "floss", "fork")

        self.add_line("handle", NECK, (AX, BOTTOM))
        self.relate("connect", "handle", "fork")
