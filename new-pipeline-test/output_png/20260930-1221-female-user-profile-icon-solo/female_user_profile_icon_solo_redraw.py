"""female-user-profile-icon-solo (redraw of the new-pipeline traced SVG).

Subject: a user profile bust, a hollow round head floating above one rounded
shoulder arc that is open at the bottom (human_ref/user.svg construction).
The generated image follows the stick-figure brief (no hair, no face), so the
drawing keeps that neutral user silhouette rather than inventing a female cue.

Plan on SQUARE (the metrics suggestion; centerline box (6,6)-(42,42)), one
axis at x=24, mirrored left/right.
- head: circle r=HEAD_R=9 about (24,15); top y=6 on the box edge.
- shoulders: flat crest at SHOULDER_Y=32, quarter arcs r=SHOULDER_R=10 down to
  (6,42) and (42,42), vertical tangent at the ends, open bottom. Split at x=24
  so the upper torso has a neck junction for mark_human_figure.
- detached head: head outline bottom y=24, shoulder crest y=32 -> exactly 8 on
  centerlines, 4-unit visible ink gap.

Metric issues:
- clearance e0/e1 (4.15, need 8) -> fixed: head bottom y=24, crest y=32.
- head-gap (4.15, need exactly 8, head centred on the torso axis) -> fixed:
  exactly 8 on centerlines, head centre on the shoulder axis x=24.
- keyshape-short-axis (x filled 87%) -> fixed: shoulder ends reach x=6 and
  x=42; head top y=6, shoulder ends y=42 (exact SQUARE fit).
- stroke-width (info, 2.4 traced) -> redrawn at stroke 4; head hole is 14 wide
  inscribed and every gap is budgeted at 4 ink.
Reference: icon_set/references/human_ref/user.svg (circular head r=9, broad
smooth shoulders, open bottom); Lucide `user` (circle over a shoulder arc).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7e7928dc-c2b2-4979-be45-5ca674afd12d"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1221-female-user-profile-icon-solo/"
    "female-user-profile-icon-solo_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AX = 24            # shared head / body axis
HEAD_R = 9
HEAD_CY = 15       # top of head y=6
SHOULDER_Y = HEAD_CY + HEAD_R + 8   # 32: exact detached-head gap
SHOULDER_R = 10
LEFT, RIGHT, BOTTOM = 6, 42, 42


class FemaleUserProfileIconSoloRedraw(Solo48):
    icon_id = "female-user-profile-icon-solo-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/avatars"
    aliases = ("female user", "woman profile", "user profile")
    keywords = ("female", "woman", "user", "profile", "account", "avatar", "person")

    def build(self) -> None:
        cx, cy, r = AX, HEAD_CY, HEAD_R
        west, east = (cx - r, cy), (cx + r, cy)
        self.add_arc("head-top", west, east, radius_x=r, sweep=True)
        self.add_arc("head-bottom", east, west, radius_x=r, sweep=True)
        self.add_contour("head", "head-top", "head-bottom", closed=True)

        # Shoulders, split at the neck junction on the axis.
        neck = (AX, SHOULDER_Y)
        sr = SHOULDER_R
        self.add_line("crest-left", neck, (LEFT + sr, SHOULDER_Y))
        self.add_arc("shoulder-left", (LEFT + sr, SHOULDER_Y), (LEFT, BOTTOM), radius_x=sr, sweep=False)
        self.add_contour("body-left", "crest-left", "shoulder-left")
        self.add_line("crest-right", neck, (RIGHT - sr, SHOULDER_Y))
        self.add_arc("shoulder-right", (RIGHT - sr, SHOULDER_Y), (RIGHT, BOTTOM), radius_x=sr, sweep=True)
        self.add_contour("body-right", "crest-right", "shoulder-right")
        self.relate("connect", "body-left", "body-right")

        self.mark_human_figure("user", head="head", torso="crest-left", torso_junction="start")
