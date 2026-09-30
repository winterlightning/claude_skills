"""avatar-jockey-man (redraw of the new-pipeline traced SVG).

Subject: a jockey bust, a round head wearing a racing helmet with a short
front visor, above open rounded shoulders (human_ref/user.svg construction).

Plan on VRECT_L (centerline box (8,4)-(40,44)), one axis at x=24.
VRECT_M (the metrics suggestion) was built first and validated, but its
4-unit visor made the head read as a theta; VRECT_L gives the 32-wide
shoulders of human_ref/user.svg and a 6-unit visor, so it was kept.
- head: circle r=HEAD_R about (24,HEAD_CY); its top half is the helmet shell.
- brim: horizontal line across the head's equator, continued past the right
  side of the head as the visor to x=40 (the right extreme).
- shoulders: flat crest at SHOULDER_Y, quarter arcs r=SHOULDER_R down to
  x=8 / x=40, short vertical sides to y=44, open bottom; split at x=24 so the
  upper torso has a neck junction for mark_human_figure.
- detached head: shoulder crest exactly 8 below the head outline (4-unit ink gap).

Metric issues:
- clearance e0/e1 (helmet 3.3 above head) -> fixed by construction: the helmet
  no longer floats; it is the head's upper half with the brim as a shared
  chord (declared connects). A separate helmet cannot fit: helmet >= 10 (hole 6)
  + 8 + head >= 10 + 8 + shoulders leaves 4 units of shoulder in a 40-unit box.
- clearance e1/e2 and head-gap (2.79, need exactly 8) -> fixed: head bottom
  y=24, shoulder crest y=32, head centred on the shoulder axis x=24.
- keyshape-short-axis (x filled 85%) -> fixed: shoulders span x 8..40 and the
  visor tip reaches x=40; y spans 4..44 (exact VRECT_L fit).
- stroke-width (info) -> redrawn at stroke 4 with all gaps budgeted at 4 ink.
Reference: icon_set/references/human_ref/user.svg (circular head, broad smooth
shoulders, open bottom); Lucide hard-hat / cap construction (dome + brim chord).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d9262e24-63e6-54ce-9aa8-9061addf48f8"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1830-avatar-jockey-man/"
    "avatar-jockey-man_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AX = 24            # shared head / body axis
HEAD_R = 10
HEAD_CY = 14       # top of head y=4
VISOR_TIP = 40
SHOULDER_Y = HEAD_CY + HEAD_R + 8   # 32: exact detached-head gap
SHOULDER_R = 10
LEFT, RIGHT, BOTTOM = 8, 40, 44


class AvatarJockeyManRedraw(Solo48):
    icon_id = "avatar-jockey-man-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/avatars"
    human_construction = "bust"
    aliases = ("jockey avatar", "horse rider avatar")
    keywords = ("jockey", "avatar", "user", "helmet", "rider", "horse racing", "person", "profile")

    def build(self) -> None:
        cx, cy, r = AX, HEAD_CY, HEAD_R
        west, east = (cx - r, cy), (cx + r, cy)
        # Helmet shell = upper half of the head circle.
        self.add_arc("shell-left", west, (cx, cy - r), radius_x=r, sweep=True)
        self.add_arc("shell-right", (cx, cy - r), east, radius_x=r, sweep=True)
        # Face = lower half.
        self.add_arc("face-right", east, (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("face-left", (cx, cy + r), west, radius_x=r, sweep=True)
        self.add_contour("head", "shell-left", "shell-right", "face-right", "face-left", closed=True)

        # Brim across the equator, visor beyond the right side.
        self.add_line("brim", west, east)
        self.add_line("visor", east, (VISOR_TIP, cy))
        self.relate("connect", "brim", "head")
        self.relate("connect", "visor", "head")
        self.relate("connect", "brim", "visor")

        # Shoulders, split at the neck junction on the axis.
        neck = (AX, SHOULDER_Y)
        sr = SHOULDER_R
        self.add_line("crest-left", neck, (LEFT + sr, SHOULDER_Y))
        self.add_arc("shoulder-left", (LEFT + sr, SHOULDER_Y), (LEFT, SHOULDER_Y + sr), radius_x=sr, sweep=False)
        self.add_line("side-left", (LEFT, SHOULDER_Y + sr), (LEFT, BOTTOM))
        self.add_contour("body-left", "crest-left", "shoulder-left", "side-left")
        self.add_line("crest-right", neck, (RIGHT - sr, SHOULDER_Y))
        self.add_arc("shoulder-right", (RIGHT - sr, SHOULDER_Y), (RIGHT, SHOULDER_Y + sr), radius_x=sr, sweep=True)
        self.add_line("side-right", (RIGHT, SHOULDER_Y + sr), (RIGHT, BOTTOM))
        self.add_contour("body-right", "crest-right", "shoulder-right", "side-right")
        self.relate("connect", "body-left", "body-right")

        self.mark_human_figure("jockey", head="head", torso="crest-left", torso_junction="start")
