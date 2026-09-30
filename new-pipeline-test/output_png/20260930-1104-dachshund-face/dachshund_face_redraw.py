"""dachshund-face (redraw of the new-pipeline traced SVG).

Plan: a front-view dachshund head on CIRCLE (centerline radius 20 about
(24,24)), mirrored about x = 24.
- head: one closed contour. A radius-13 dome centred at SKULL (24,17) whose
  top (24,4) is the top extreme; it runs down to CHEEK (12,22) (5-12-13
  lattice point), then a jaw taper leaves along the dome tangent and lands
  vertically on JAW (15,30). A straight muzzle wall runs to (15,35) and a
  radius-9 tip arc about the nose closes the long snout at (24,44), the
  bottom extreme. Tangent-continuous all the way round.
- ears: one two-cubic flap per side from the dome's widest point (11,17).
  It rises over the temple, drops through (4,24) on the keyshape circle
  (the side extreme), rounds the lobe and ends on the muzzle foot (15,35),
  so each ear closes a teardrop hole against the jaw. Both ends are shared
  nodes and declared with `connect`.
- eyes: two dots at (20,17)/(28,17), 8 apart, 4 off the dome centre so 9
  from the dome. nose: a dot at (24,35), the tip-arc centre, 9 from the
  muzzle walls and tip.
Keyshape: CIRCLE instead of the suggested VRECT_L. The eyes need a skull 26
wide on centerlines (8 between the dots plus 9 to each curved wall), which
leaves 3 per side in VRECT_L's 32 for the ears. The metrics' keyshape table
scores VRECT_L on the trace's aspect only; at stroke 4 no ear hole fits. On
CIRCLE the ears use the 40 of width at mid-height.
Dropped: the short eye dashes (dashes need 2 more per eye than the width
allows, so they are dots) and the hollow triangular nose (a hole of 6 inside
the 18-wide muzzle leaves no clearance to the walls, so it is a dot).
Lucide `dog` (icon_set/references/lucide/original/dog.svg) gave the dot eyes
and ear flaps that close against the head outline; the long snout, domed
skull and low-hanging ears follow the image.

Metric issues (dachshund-face_metrics.json), re-measured with svg_metrics.py
on the redraw (--keyshape CIRCLE): no issues left.
- stroke-width (info, trace 2.47 fitted): redrawn at stroke 4 with every gap
  budgeted for 4.
- keyshape-short-axis (warn, VRECT_L y fill 92%): moot on CIRCLE; the top,
  bottom and both sides touch radius 20 exactly.
- clearance e0/e1, e0/e2 (error, 2.9): the ear's free lower lobe hung beside
  the muzzle. Each ear now ends on the muzzle wall, so the lobe closes
  against the jaw instead of running parallel to it.
- clearance e0/e3, e0/e4, e1/e3, e2/e4 (error, 3.1-4.1): eyes sat against
  the head wall and ear roots; they are 9 from the dome now, and the ears
  leave the head beside them at (11,17).
- clearance e0/e5, e1/e5, e2/e5 (error, 2.4-7.7): the nose is 9 from the
  muzzle walls and the tip arc, and 20 from the ears.
- clearance e3/e4 (error, 6.7): eyes 8 apart (dots, exact on the minimum).
- narrow-join e1/e0, e2/e0 (warn, 22.9 deg): the ear now leaves the dome
  at about 77 degrees and meets the muzzle foot at about 63 degrees.
- holes at (12.3,27.2)/(35.6,27.2) (error, 4.47): the ear holes are now 5.81
  wide, which svg_metrics accepts as ok (its raster measure). They cannot be
  made wider: at the lobe the ear is already on the keyshape circle and the
  jaw is 9 from the nose.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "44442ee3-de41-53ab-af82-3e69c47a0ecc"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1104-dachshund-face/dachshund-face_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
SKULL = (24, 17)       # dome centre; the dome's top (24,4) is the top extreme
SKULL_R = 13           # eyes sit 4 off the centre, so 9 from the dome
EYE_DX = 4             # eye dots at x = 20 / 28: 8 apart
NOSE = (24, 35)        # muzzle-tip centre and nose dot
MUZZLE_R = 9           # tip (24,44) is the bottom extreme; 9 to the nose
EAR_ROOT = (11, 17)    # SKULL - (13,0): widest point of the dome
CHEEK = (12, 22)       # SKULL + (-12, 5): dome ends, jaw taper begins
JAW = (15, 30)         # muzzle wall turns vertical here
EAR_TIP = (15, 35)     # muzzle wall meets the tip arc; the ear rejoins here
EAR_OUT = (4, 24)      # left extreme on the radius-20 keyshape circle
TAPER = 0.3            # jaw-taper control length along the dome tangent


def _m(p):
    """Mirror a point or control across the vertical axis."""
    return (2 * AXIS - p[0], p[1])


class DachshundFaceRedraw(Solo48):
    icon_id = "dachshund-face-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/dog"
    aliases = ("dachshund", "wiener dog", "sausage dog", "dog face")
    keywords = ("dachshund", "dog", "puppy", "hound", "pet", "animal",
                "face", "head", "floppy ears", "snout")

    def build(self) -> None:
        top = (AXIS, SKULL[1] - SKULL_R)
        tip = (AXIS, NOSE[1] + MUZZLE_R)
        # Jaw taper leaves CHEEK along the dome tangent (5,12) and lands
        # vertically on JAW, so both ends are tangent-continuous.
        c1 = (CHEEK[0] + 5 * TAPER, CHEEK[1] + 12 * TAPER)
        c2 = (JAW[0], JAW[1] - 3)
        # Ear: out from the root to the keyshape edge, round the lobe and
        # back in to the muzzle foot.
        ear_top = ((10, 12.5), (5, 13.5), EAR_OUT)
        ear_low = ((4, 32), (9, 38), EAR_TIP)

        self.add_arc("head-dome-l", top, EAR_ROOT, radius_x=SKULL_R, sweep=False)
        self.add_arc("head-temple-l", EAR_ROOT, CHEEK, radius_x=SKULL_R, sweep=False)
        self.add_bezier("head-jaw-l", CHEEK, (c1, c2, JAW))
        self.add_line("head-muzzle-l", JAW, EAR_TIP)
        self.add_arc("head-tip-l", EAR_TIP, tip, radius_x=MUZZLE_R, sweep=False)
        self.add_arc("head-tip-r", tip, _m(EAR_TIP), radius_x=MUZZLE_R, sweep=False)
        self.add_line("head-muzzle-r", _m(EAR_TIP), _m(JAW))
        self.add_bezier("head-jaw-r", _m(JAW), (_m(c2), _m(c1), _m(CHEEK)))
        self.add_arc("head-temple-r", _m(CHEEK), _m(EAR_ROOT), radius_x=SKULL_R, sweep=False)
        self.add_arc("head-dome-r", _m(EAR_ROOT), top, radius_x=SKULL_R, sweep=False)
        self.add_contour(
            "head", "head-dome-l", "head-temple-l", "head-jaw-l", "head-muzzle-l",
            "head-tip-l", "head-tip-r", "head-muzzle-r", "head-jaw-r",
            "head-temple-r", "head-dome-r", closed=True,
        )

        for side, f in (("l", lambda p: p), ("r", _m)):
            self.add_bezier(
                f"ear-{side}", f(EAR_ROOT),
                tuple(f(p) for p in ear_top),
                tuple(f(p) for p in ear_low),
            )
        self.relate("connect", "ear-l", "head-dome-l", "head-temple-l")
        self.relate("connect", "ear-l", "head-muzzle-l", "head-tip-l")
        self.relate("connect", "ear-r", "head-dome-r", "head-temple-r")
        self.relate("connect", "ear-r", "head-muzzle-r", "head-tip-r")

        self.add_dot("eye-l", (AXIS - EYE_DX, SKULL[1]))
        self.add_dot("eye-r", (AXIS + EYE_DX, SKULL[1]))
        self.add_dot("nose", NOSE)
