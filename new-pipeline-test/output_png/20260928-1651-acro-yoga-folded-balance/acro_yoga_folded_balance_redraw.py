"""acro-yoga-folded-balance (redraw of the new-pipeline traced SVG).

Plan: two stick figures in side view on SQUARE (centerline box (6,6)-(42,42)),
the metrics' suggested keyshape (fill 1.0 x 1.0).
- base: lying on the back along the floor. Head r4 ring at (10,38) (left
  extreme x=6, bottom extreme y=42); level torso neck (22,38) -> hip (34,38),
  exactly 8 centerline units (4 ink) right of the head; one straight raised
  leg from the hip up to the foot on the flyer's thigh (37,15).
- flyer: folded forward at the hips over the base's foot, an inverted V with
  the hip apex (32,6) as the top extreme. Legs run down-right on a 5:9 line
  to the feet (42,24) (right extreme), split at the base's foot (37,15) so
  the contact is a shared node. The back hangs down-left to the shoulder
  (26,20), then a 2-long level neck run to (24,20); the head r4 ring at
  (12,20) sits level beside it at exactly 8. The arms dangle from the
  shoulder down-left to (21,29).
  The flyer head is offset 2 right and 18 up from the base head so the two
  rings do not stack into a ":" at 48 px.
References: icon_set/references/human_ref (round r4 heads, single-stroke
limbs, detached head with a 4-unit ink gap, level neck run so the gap is
axis-aligned). No useful Lucide match: Lucide has no partner-balance figure.

Metric issues fixed:
- clearance e0/e2 (6.97, base leg vs flyer back beside their joint): the
  base's foot now lands on the flyer's leg line at (37,15), 8.1 from the
  flyer's back line, and the straight leg diverges from it below.
- clearance e0/e4 (2.26, base torso running into its head): the base torso
  starts exactly 8 right of the head ring on a level line.
- clearance e2/e3 (2.66, flyer back touching its head): the flyer head sits
  level beside a horizontal neck run at exactly 8; the arms stay 12.2 from
  the head centre.
- hole (2.09 at the flyer's head/back pinch) and hole (1.84 at the base's
  head/torso pinch): both heads are detached r4 rings (exempt small
  circles), so no sliver holes remain.
- junctions e0/e2 and e1/e0 (t-junctions): every contact is a shared
  endpoint declared with relate("connect"); the stray foot tick (e1) and
  the zig-zag base leg are replaced by one straight raised leg.
- stroke-width (2.77 trace): redrawn at stroke 4 with every gap budgeted
  at 8.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "672c58c9-cf49-5d74-ba11-e6398667c047"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1651-acro-yoga-folded-balance/"
    "acro-yoga-folded-balance_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HEAD_R = 4
GAP = 8                              # head-to-neck centerline gap

# base, lying on the floor
BASE_HEAD = (10, 38)
BASE_NECK = (BASE_HEAD[0] + HEAD_R + GAP, 38)
BASE_HIP = (34, 38)

# flyer, folded over the base's foot
APEX = (32, 6)                       # hips, top extreme
FOOT_CONTACT = (37, 15)              # on the 5:9 leg line from APEX
FLYER_FEET = (42, 24)                # same line, right extreme
SHOULDER = (26, 20)
FLYER_NECK = (24, 20)
FLYER_HEAD = (FLYER_NECK[0] - GAP - HEAD_R, 20)
HANDS = (21, 29)

class AcroYogaFoldedBalanceRedraw(Solo48):
    icon_id = "acro-yoga-folded-balance-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("folded leaf", "acro yoga pose", "partner yoga")
    keywords = ("acro yoga", "yoga", "balance", "partner", "base", "flyer", "pose")

    def _head(self, name: str, centre: tuple[int, int]) -> None:
        cx, cy = centre
        r = HEAD_R
        self.add_arc(f"{name}-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc(f"{name}-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc(f"{name}-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc(f"{name}-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour(name, f"{name}-1", f"{name}-2", f"{name}-3", f"{name}-4", closed=True)

    def build(self) -> None:
        # Base: level torso beside the head, raised leg to the flyer's thigh.
        self._head("base-head", BASE_HEAD)
        self.add_line("base-torso", BASE_NECK, BASE_HIP)
        self.mark_human_figure("base", head="base-head", torso="base-torso", torso_junction="start")
        self.add_line("base-leg", BASE_HIP, FOOT_CONTACT)
        self.relate("connect", "base-leg", "base-torso")

        # Flyer: inverted V over the base's foot, head level beside the neck run.
        self._head("flyer-head", FLYER_HEAD)
        self.add_line("flyer-back", APEX, SHOULDER)
        self.add_line("flyer-torso", SHOULDER, FLYER_NECK)
        self.relate("connect", "flyer-back", "flyer-torso")
        self.mark_human_figure("flyer", head="flyer-head", torso="flyer-torso", torso_junction="end")
        self.add_line("flyer-arms", SHOULDER, HANDS)
        self.relate("connect", "flyer-arms", "flyer-back")
        self.relate("connect", "flyer-arms", "flyer-torso")
        self.add_line("flyer-thigh", APEX, FOOT_CONTACT)
        self.add_line("flyer-shins", FOOT_CONTACT, FLYER_FEET)
        self.relate("connect", "flyer-thigh", "flyer-back")
        self.relate("connect", "flyer-thigh", "flyer-shins")

        # The base's foot presses on the flyer's thigh line.
        self.relate("connect", "base-leg", "flyer-thigh")
        self.relate("connect", "base-leg", "flyer-shins")
