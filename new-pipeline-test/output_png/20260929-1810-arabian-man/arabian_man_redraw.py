"""arabian-man (redraw of the new-pipeline traced SVG).

Subject: the bust of a man wearing a ghutra (headcloth) held by an agal
(headband). The generated PNG was a generic user bust (circle head over a
shoulder arc); the choice.json warning said Arabian identity was not visible,
so the redraw keeps the bust but dresses it: the headcloth is what makes the
figure read as an Arabian man at 48 px.

Plan on SQUARE (centerline box (6,6)-(42,42)), mirrored about x=24:
- cloth: one open contour, the ghutra. Half-ellipse crown rx16 ry10 about
  (24,16) from the left drape over the y=6 top to the right drape, then
  straight drapes down to jaw level (y=24) on x=8 / x=40, 8 outside the face.
  (A first try carried the drapes on down and flared them into the shoulders;
  at 48 px that read as a helmet or bell, so the shoulders are a separate
  body now, and the drapes stop where they would crowd the shoulder arcs.)
- agal: straight band on the crown's springline y=16, sharing both drape
  endpoints (connect); split at the face so the face shares its knots.
- face: lower half-circle r8 hanging from the band (connect), centre x=24.
- body: user.svg-style bust. Quarter-circle shoulders r10 from the x=6 / x=42
  floor points up to a straight top at y=32, exactly 8 centerline units under
  the jaw (4-unit ink gap); the top is split at the x=24 neck junction and
  marked with mark_human_figure.

Metric issues:
- clearance e0/e1 4.78 (need 8): fixed, jaw to body top is 8 on centerlines;
  drapes are 8 from the face and more than 8 from the shoulder arcs.
- head-gap 4.78 (need exactly 8, head centred on the torso axis): fixed,
  face centre x=24 is the neck junction, gap exactly 8.
- keyshape-short-axis (x filled 86%): fixed, the shoulders reach x=6 and x=42
  and the crown reaches y=6, the floor y=42, so SQUARE is met on all sides.
- stroke-width 2.39 (info): redrawn at stroke 4; every gap was budgeted at
  stroke 4.
- choice.json warning (generic bust, no Arabian identity): addressed by the
  headcloth and agal.
References: icon_set/references/human_ref/user.svg (circular head centred on
the body axis, 4-unit ink gap); Lucide user-round for the half-circle face
construction. The trace's head/shoulder coordinates were not reused.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "dd92cb2d-e66d-53d1-835f-92be92e0873e"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1810-arabian-man/arabian-man_raw.svg"
AUTHOR = "claude-opus-5-5"

CX = 24                 # figure axis
FACE_R = 8
CROWN_R = FACE_R + 8    # half-width of the headcloth: drapes sit 8 outside the face
CROWN_RY = 10           # flattened crown so the face gets the height
CROWN_Y = 6 + CROWN_RY  # springline = agal band
JAW_Y = CROWN_Y + FACE_R
DRAPE_END = JAW_Y       # drapes fall to jaw level; lower would crowd the shoulders
HEAD_GAP = 8            # detached head: 4-unit ink gap = 8 on centerlines
BODY_TOP = JAW_Y + HEAD_GAP
SHOULDER_R = 42 - BODY_TOP   # quarter-circle shoulders from the body top to the floor
FLOOR = 42


class ArabianManRedraw(Solo48):
    icon_id = "arabian-man-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ("man in ghutra", "man in keffiyeh")
    keywords = ("arabian", "arab", "man", "ghutra", "keffiyeh", "agal", "headdress", "bust")

    def build(self) -> None:
        left, right = CX - CROWN_R, CX + CROWN_R
        self.add_line("cloth-left-drape", (left, DRAPE_END), (left, CROWN_Y))
        self.add_arc(
            "cloth-crown", (left, CROWN_Y), (right, CROWN_Y),
            radius_x=CROWN_R, radius_y=CROWN_RY, sweep=True,
        )
        self.add_line("cloth-right-drape", (right, CROWN_Y), (right, DRAPE_END))
        self.add_contour("cloth", "cloth-left-drape", "cloth-crown", "cloth-right-drape")

        self.add_line("agal-left", (left, CROWN_Y), (CX - FACE_R, CROWN_Y))
        self.add_line("agal-mid", (CX - FACE_R, CROWN_Y), (CX + FACE_R, CROWN_Y))
        self.add_line("agal-right", (CX + FACE_R, CROWN_Y), (right, CROWN_Y))
        self.add_contour("agal", "agal-left", "agal-mid", "agal-right")
        self.relate("connect", "cloth", "agal")

        self.add_arc("face", (CX + FACE_R, CROWN_Y), (CX - FACE_R, CROWN_Y), radius_x=FACE_R, sweep=True)
        self.relate("connect", "face", "agal")

        l_top, r_top = 6 + SHOULDER_R, 42 - SHOULDER_R
        self.add_arc("body-left-shoulder", (6, FLOOR), (l_top, BODY_TOP), radius_x=SHOULDER_R, sweep=True)
        self.add_line("body-top-left", (l_top, BODY_TOP), (CX, BODY_TOP))
        self.add_line("body-top", (CX, BODY_TOP), (r_top, BODY_TOP))
        self.add_arc("body-right-shoulder", (r_top, BODY_TOP), (42, FLOOR), radius_x=SHOULDER_R, sweep=True)
        self.add_contour("body", "body-left-shoulder", "body-top-left", "body-top", "body-right-shoulder")
        self.mark_human_figure("man", head="face", torso="body-top", torso_junction="start")
