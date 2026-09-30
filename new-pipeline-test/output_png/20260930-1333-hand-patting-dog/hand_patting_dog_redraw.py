"""hand-patting-dog (redraw of the new-pipeline traced SVG).

Subject: a hand reaching in from the upper left, palm down, about to pat
the head of a floppy-eared dog seen in profile.

Plan: SQUARE (the suggested keyshape; centerline box (6,6)-(42,42)).
- hand: one open stroke. The forearm starts on the (6,6) corner, runs 45
  degrees down, turns tangent into a flat palm at y=11, and the fingertips
  curl down in an r4 half circle (apex x=40) ending at (36,19).
- dog head: one open contour. Floppy ear: inner line x=16 hangs from y=31,
  r4 round bottom, outer side x=8 rising into the r10 skull arc (top y=22);
  the skull rolls over into a concave stop, a flat muzzle top at y=30, an r4
  nose (apex x=42) and the jaw sweeps down-left to the throat end at y=42.
- eye: one dot at (25,33), over 8 clear of ear, skull, stop and jaw (a dash
  sat exactly 8 from the ear line, which the gate returns as review).
Extremes: x=6 arm start, y=6 arm start, x=42 nose apex, y=42 throat end.
References: the generated PNG (arm hook above, dog head below, ear on the
left, eye); human-reference.md for the arm (an arm alone, no figure, so
no head). No useful Lucide match: lucide/dog is a front-facing face and
lucide/hand an open palm; only Lucide's r=half-width round ends were taken.

Metric issues (svg_metrics) and what happened to them:
- stroke-width (info): fixed, redrawn at stroke 4 with every gap between
  distinct parts budgeted at >= 8 on centerlines.
- keyshape-short-axis (SQUARE x filled 87%): fixed, arm start on x=6 and
  nose apex on x=42; y extremes on 6 (arm) and 42 (throat).
- clearance e0/e1 (hand hook 4.1 above the skull): fixed, palm lifted to
  y=11 and the fingertip curl ends over the muzzle, >= 8 from the stop.
- clearance e1/e2 (eye 3.6 from the stop): fixed, the eye (now a dot) moved onto
  the cheek, >= 8 from every outline part.
- hole (ear loop 4.8 inscribed): fixed, the ear inner line stops 8 below
  the skull so the ear is open, not an enclosed hole.
- no-head (warn): not applicable; the subject has an arm, not a stick
  figure, so there is no head to trace and no mark_human_figure.
Deliberate change: the hand's lower palm edge (4 under the upper one in the
trace) became a curled fingertip; a full 8-thick palm loop left the dog
head only 14 tall with no room for the eye.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ef1c856a-063a-4941-92f0-78189ee7aba9"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1333-hand-patting-dog/hand-patting-dog_raw.svg"
AUTHOR = "claude-opus-5-5"

PALM_Y = 11          # flat palm line
PALM_END = 36        # where the fingertip curl starts
CURL_R = 4
SKULL_C, SKULL_R = (18, 32), 10
EAR_IN, EAR_TOP, EAR_R = 16, 31, 4
EAR_LOW = 37         # centre height of the ear's round bottom
MUZZLE_Y, NOSE_X, NOSE_R = 30, 38, 4
EYE = (25, 33)


class HandPattingDogRedraw(Solo48):
    icon_id = "hand-patting-dog-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/pets"
    aliases = ("pet the dog", "patting a dog", "stroking dog")
    keywords = ("hand", "dog", "pat", "pet", "stroke", "puppy", "care",
                "affection", "animal", "friendly")

    def build(self) -> None:
        # Hand: forearm, flat palm, curled fingertips.
        self.add_line("forearm", (6, 6), (9, 9))
        self.add_bezier("wrist", (9, 9), ((10.5, 10.5), (11.5, PALM_Y), (13, PALM_Y)))
        self.add_line("palm", (13, PALM_Y), (PALM_END, PALM_Y))
        self.add_arc("fingertips", (PALM_END, PALM_Y), (PALM_END, PALM_Y + 2 * CURL_R),
                     radius_x=CURL_R)
        self.add_contour("hand", "forearm", "wrist", "palm", "fingertips")

        # Dog head: ear, skull, stop, muzzle, nose, jaw.
        cx, cy = SKULL_C
        ear_out = EAR_IN - 2 * EAR_R
        self.add_line("ear-inner", (EAR_IN, EAR_TOP), (EAR_IN, EAR_LOW))
        self.add_arc("ear-tip", (EAR_IN, EAR_LOW), (ear_out, EAR_LOW), radius_x=EAR_R)
        self.add_line("ear-outer", (ear_out, EAR_LOW), (ear_out, cy))
        self.add_arc("skull", (cx - SKULL_R, cy), (cx, cy - SKULL_R), radius_x=SKULL_R)
        self.add_bezier("brow", (cx, cy - SKULL_R),
                        ((24, 22), (29, 24), (32, 27)),
                        ((33, 28), (33.5, MUZZLE_Y), (35, MUZZLE_Y)))
        self.add_line("muzzle", (35, MUZZLE_Y), (NOSE_X, MUZZLE_Y))
        self.add_arc("nose", (NOSE_X, MUZZLE_Y), (NOSE_X, MUZZLE_Y + 2 * NOSE_R),
                     radius_x=NOSE_R)
        self.add_bezier("jaw", (NOSE_X, MUZZLE_Y + 2 * NOSE_R),
                        ((33, 38), (30.5, 39.5), (28, 42)))
        self.add_contour("dog", "ear-inner", "ear-tip", "ear-outer", "skull",
                         "brow", "muzzle", "nose", "jaw")

        self.add_dot("eye", EYE)
