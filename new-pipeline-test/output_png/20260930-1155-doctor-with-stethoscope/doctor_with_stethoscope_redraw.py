"""Doctor with stethoscope: a frontal bust (detached round head over a rounded
shoulder dome) wearing a stethoscope around the neck, its tubes hanging from
the shoulders into a U with the round chestpiece below (redraw of the
new-pipeline traced SVG).

PLAN
- Keyshape VRECT_L, centerline box (8,4)-(40,44). The metrics suggested SQUARE
  (score 1.12, VRECT_L 0.92), but SQUARE's 36-unit height cannot stack head,
  8-unit head gap, the U and a chestpiece ring (with 6-unit holes) at 8-unit
  clearance; VRECT_L's 40-unit height can, and the trace is taller than wide
  (aspect 0.87) anyway.
- Symbols, all on axis x=24 and mirrored:
  head    circle r=6 at (24,10): top on the box edge y=4, bottom y=16.
  body    left wall x=8 (y 44..34), shoulder arc r=10 to (18,24), neckline
          y=24 to (30,24), mirrored arc and wall. Neckline = head bottom + 8
          (human_ref detached bust: exactly 4 units of visible ink gap).
  tubes   the stethoscope hangs from the shoulder/neckline joints (18,24) and
          (30,24): straight legs down to y=28, semicircle r=6 with bottom (24,34).
  chest-  ring r=5 at (24,39) hanging from the U bottom (24,34), its own
  piece   bottom on y=44. Both holes (under the U, inside the ring) are 6+.
- Human figure flag: head -> neck-right (starts at the neck point (24,22)).

METRIC ISSUES
- clearance e0/e1 (head vs shoulders 2.77): fixed, exact 8 on centerlines.
- head-gap e2/e4: the metric took the chestpiece for a head; the real head
  (e0) now has the exact 8-unit centerline gap to its own neckline.
- clearance e1/e2, e1/e3, e1/e4, e2/e3 (stethoscope vs shoulders / itself):
  fixed by redesign. The trace's free-floating stethoscope (earpiece hooks, U,
  lower loop and a ring beside it) needs about 44 units of width at 8-unit
  clearance and cannot sit inside a 32-36 unit chest; the tubes now drape from
  the shoulders (shared, declared joints) and the chestpiece hangs centred
  below the U. Earpiece hooks and the side loop are dropped.
- keyshape-short-axis: fixed; every extreme sits on the VRECT_L box.
- stroke-width (info): drawn at stroke 4 from the start.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1e909a20-b59c-51ff-929f-4d51607994a7"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1155-doctor-with-stethoscope/doctor-with-stethoscope_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
TOP, BOTTOM, WALL = 4, 44, 8     # VRECT_L centerline box: x 8..40, y 4..44
HEAD_R = 6
GAP = 8                          # head outline to neckline, centerlines
NECK_Y = TOP + 2 * HEAD_R + GAP  # 24
TUBE_DX = 6                      # tube legs at 18 and 30
SHOULDER_R = AXIS - TUBE_DX - WALL  # 10: arc ends exactly on the tube joint
U_R = TUBE_DX
LEG_BOTTOM = 28
RING_R = 5


def mx(x: int) -> int:
    return 2 * AXIS - x


class DoctorWithStethoscopeRedraw(Solo48):
    icon_id = "doctor-with-stethoscope-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/medical"
    aliases = ("physician", "medic", "doctor")
    keywords = ("doctor", "stethoscope", "physician", "medical", "health", "person", "bust")

    def build(self) -> None:
        hc = TOP + HEAD_R
        self.add_arc("head-top", (AXIS - HEAD_R, hc), (AXIS + HEAD_R, hc), radius_x=HEAD_R)
        self.add_arc("head-bottom", (AXIS + HEAD_R, hc), (AXIS - HEAD_R, hc), radius_x=HEAD_R)
        self.add_contour("head", "head-top", "head-bottom", closed=True)

        jl, jr = AXIS - TUBE_DX, AXIS + TUBE_DX
        arc_y = NECK_Y + SHOULDER_R
        self.add_line("wall-left", (WALL, BOTTOM), (WALL, arc_y))
        self.add_arc("shoulder-left", (WALL, arc_y), (jl, NECK_Y), radius_x=SHOULDER_R)
        self.add_line("neck-left", (jl, NECK_Y), (AXIS, NECK_Y))
        self.add_line("neck-right", (AXIS, NECK_Y), (jr, NECK_Y))
        self.add_arc("shoulder-right", (jr, NECK_Y), (mx(WALL), arc_y), radius_x=SHOULDER_R)
        self.add_line("wall-right", (mx(WALL), arc_y), (mx(WALL), BOTTOM))
        self.add_contour(
            "body", "wall-left", "shoulder-left", "neck-left", "neck-right",
            "shoulder-right", "wall-right",
        )
        self.mark_human_figure("doctor", head="head", torso="neck-right", torso_junction="start")

        u_bottom = LEG_BOTTOM + U_R
        self.add_line("tube-left", (jl, NECK_Y), (jl, LEG_BOTTOM))
        self.add_arc("tube-u-left", (jl, LEG_BOTTOM), (AXIS, u_bottom), radius_x=U_R, sweep=False)
        self.add_arc("tube-u-right", (AXIS, u_bottom), (jr, LEG_BOTTOM), radius_x=U_R, sweep=False)
        self.add_line("tube-right", (jr, LEG_BOTTOM), (jr, NECK_Y))
        self.add_contour("tubes", "tube-left", "tube-u-left", "tube-u-right", "tube-right")
        self.relate("connect", "tubes", "body")

        ring_top = BOTTOM - 2 * RING_R
        self.add_arc("ring-right", (AXIS, ring_top), (AXIS, BOTTOM), radius_x=RING_R)
        self.add_arc("ring-left", (AXIS, BOTTOM), (AXIS, ring_top), radius_x=RING_R)
        self.add_contour("chestpiece", "ring-right", "ring-left", closed=True)
        self.relate("connect", "tubes", "chestpiece")
