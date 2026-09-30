"""bearded-pirate-with-crossed-hat-mark (redraw of the new-pipeline traced SVG).

Plan: a pirate's pointed-beard face under a tricorn hat marked with an X,
mirrored about x=24, on VRECT_L (centerline box (8,4)-(40,44)).
- hat: one closed contour. Crown = r12 dome about (24,16) whose apex (24,4) is
  the upper extreme; below each dome side a cubic flares out to a rounded brim
  tip at (8,19)/(40,19) (the x extremes); the underside curls back from the
  tip, passes the beard joins at (13,25)/(35,25) tangent-continuously and
  flattens to its lowest point (24,29).
- cross: four 3-unit arms from one shared centre (24,17), declared connected;
  its arm ends sit >= 8.4 from the dome and 9 above the brim.
- beard: one open contour hanging from the brim joins: straight sides x=13/35
  down to y=33, a 2-unit inward cheek jog, then mirrored cubics meeting in the
  beard point (24,44), the lower extreme. Each side shares its endpoint with
  the underside node and is declared `connect`.
Traced shape: bearded-pirate-with-crossed-hat-mark_raw.svg and the generated
PNG (read for the subject only; nothing copied from their coordinates).
Lucide: no pirate/tricorn original; the dome over flared brim follows the
generic Lucide hat construction (arc crown, smooth flare), the rest follows
the generated image.

Keyshape: VRECT_L instead of the suggested SQUARE. The subject is taller than
wide (metrics aspect 0.87, VRECT_L x fill 1.0); the extra 4 of height pays
for the 8-unit gaps around the cross.

Deliberate change from the image: the hat does not float. With stroke 4 the
cross needs 8 clear all round, so the brim cannot rise above y=29; a floating
beard 8 below it was only 10 tall and read as a smile. The beard sides now
meet the brim underside (face under the hat), which gives a 19-tall pointed
beard.

Metric issues:
- clearance e2/e4, e2/e5, e3/e4, e3/e5 (cross 2.9 from the hat outline):
  fixed, the cross is >= 8.4 from the dome and 9 from the brim.
- clearance e4/e5 (the two cross strokes 0.1 apart): fixed, the cross is one
  connected mark of four arms sharing the centre.
- clearance e2/e6 (brim 3.1 from the beard): fixed, the beard joins the brim
  at shared, declared endpoints; elsewhere it stays >= 8 away.
- holes at [23.9,9.5], [31.3,17.7], [16.6,17.7], [23.9,18.0] (slivers
  around the cross): fixed, the hat interior is one hole ~6.9 inscribed; the
  face hole is ~10.5.
- loose-join e0/e1/e2/e3 (brim tip fragments): fixed, the hat is one closed
  contour with the tips drawn as part of it.
- keyshape-short-axis (x fill 87% on SQUARE): fixed by VRECT_L; the brim tips
  reach x=8/40, the crown y=4 and the beard point y=44.
- stroke-count (7 strokes, budget 6): fixed, three parts (hat, cross, beard).
- stroke-width (info): drawn at stroke 4; all gaps budgeted for 4.
- no-head (warn): not fixed on purpose. The subject is a face under a hat,
  not a stick figure; there is no separate head circle or torso, so no human
  head gap applies and mark_human_figure is not used.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "871b202b-58cd-4c8b-af66-2a006eddce86"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1835-bearded-pirate-with-crossed-hat-mark/"
    "bearded-pirate-with-crossed-hat-mark_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AX = 24
TOP = 4                          # crown top (upper extreme)
DOME_R = 12                      # crown dome radius, centre (24, TOP + DOME_R)
TIP_X, TIP_Y = 16, 19            # brim tips at x = 8 / 40
FLARE_DOWN, FLARE_OUT = 3, 3     # flare cubic handles below the dome side / inside the tip
TIP_TURN = (0, 2)                # underside handle leaving the tip (in, down): rounds the tip end
UNDER_IN, UNDER_DROP = 2, 1      # underside handles either side of the beard join
UNDER_FLAT, BRIM = 6, 29         # underside front: flat handle run, lowest point
X_C, X_R = 17, 3                 # cross centre y and arm reach
BEARD_W, JOIN_Y, JOG = 11, 25, 2 # beard half width, where it meets the brim, cheek jog
CHEEK_Y = 33                     # straight side ends, jog begins
CHIN = 44                        # beard point (lower extreme)


def _m(p):
    return (2 * AX - p[0], p[1])


class BeardedPirateWithCrossedHatMarkRedraw(Solo48):
    icon_id = "bearded-pirate-with-crossed-hat-mark-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people"
    aliases = ("pirate", "pirate-captain", "buccaneer")
    keywords = ("pirate", "beard", "tricorn", "hat", "captain", "buccaneer", "costume")

    def build(self) -> None:
        dome_y = TOP + DOME_R
        top = (AX, TOP)
        side_r, side_l = (AX + DOME_R, dome_y), (AX - DOME_R, dome_y)
        tip_r, tip_l = (AX + TIP_X, TIP_Y), (AX - TIP_X, TIP_Y)
        low = (AX, BRIM)
        flare = ((side_r[0], dome_y + FLARE_DOWN), (tip_r[0] - FLARE_OUT, TIP_Y))
        join_r, join_l = (AX + BEARD_W, JOIN_Y), (AX - BEARD_W, JOIN_Y)
        du, dd = UNDER_IN, UNDER_DROP
        under_a = ((tip_r[0] - TIP_TURN[0], TIP_Y + TIP_TURN[1]), (join_r[0] + du, JOIN_Y - dd))
        under_b = ((join_r[0] - du, JOIN_Y + dd), (AX + UNDER_FLAT, BRIM))
        self.add_arc("dome-right", top, side_r, radius_x=DOME_R)
        self.add_bezier("flare-right", side_r, (*flare, tip_r))
        self.add_bezier("brim-right-outer", tip_r, (*under_a, join_r))
        self.add_bezier("brim-right-inner", join_r, (*under_b, low))
        self.add_bezier("brim-left-inner", low, (_m(under_b[1]), _m(under_b[0]), join_l))
        self.add_bezier("brim-left-outer", join_l, (_m(under_a[1]), _m(under_a[0]), tip_l))
        self.add_bezier("flare-left", tip_l, (_m(flare[1]), _m(flare[0]), side_l))
        self.add_arc("dome-left", side_l, top, radius_x=DOME_R)
        self.add_contour("hat", "dome-right", "flare-right", "brim-right-outer", "brim-right-inner",
                         "brim-left-inner", "brim-left-outer",
                         "flare-left", "dome-left", closed=True)

        c = (AX, X_C)
        for name, dx, dy in (("nw", -1, -1), ("ne", 1, -1), ("se", 1, 1), ("sw", -1, 1)):
            self.add_line(f"cross-{name}", c, (AX + dx * X_R, X_C + dy * X_R))
        self.relate("connect", "cross-nw", "cross-ne", "cross-se", "cross-sw")

        r0, r1 = join_r, (AX + BEARD_W, CHEEK_Y)
        r2 = (AX + BEARD_W - JOG, CHEEK_Y + JOG)
        chin = (AX, CHIN)
        self.add_line("beard-side-right", r0, r1)
        self.add_line("beard-cheek-right", r1, r2)
        self.add_bezier("beard-jaw-right", r2, ((r2[0], CHIN - 3), (AX + 3, CHIN - 1), chin))
        self.add_bezier("beard-jaw-left", chin, ((AX - 3, CHIN - 1), (_m(r2)[0], CHIN - 3), _m(r2)))
        self.add_line("beard-cheek-left", _m(r2), _m(r1))
        self.add_line("beard-side-left", _m(r1), _m(r0))
        self.add_contour("beard", "beard-side-right", "beard-cheek-right", "beard-jaw-right",
                         "beard-jaw-left", "beard-cheek-left", "beard-side-left")
        self.relate("connect", "beard-side-right", "brim-right-outer", "brim-right-inner")
        self.relate("connect", "beard-side-left", "brim-left-inner", "brim-left-outer")
