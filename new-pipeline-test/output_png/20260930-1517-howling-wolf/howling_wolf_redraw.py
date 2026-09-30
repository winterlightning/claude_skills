"""howling-wolf (redraw of the new-pipeline traced SVG).

Plan: VRECT_M (the suggested keyshape, the tall fit), centerline box
(10,4)-(38,44). One open contour tracing the profile of a wolf's head
and neck with the muzzle raised to howl, read from the generated image:
- neck: a cubic from the open neck end (10,36) up to the nape (17,22), with a
  deliberate corner at the base of the ear.
- ear: one pointed triangle folded back, tip (10,13), front base (19,15).
- brow: a cubic forehead dome from the ear base to the nose (33,4).
- muzzle: a short blunt nose (33,4)-(36,7), the upper jaw back to the mouth
  corner (29,16), and the lower jaw out to its tip (38,18). The upper and lower
  jaws form the open howling V (about 65 degrees).
- throat/chest: the under-jaw line (38,18)-(35,24), then a cubic tangent to it
  that bulges out to the chest and ends at (31,44).
Extremes: left 10 (neck end, ear tip), top 4 (nose), right 38 (jaw tip),
bottom 44 (chest).
Metric issues fixed:
- keyshape-short-axis (y filled 96%): the nose sits on y=4 and the chest end on
  y=44, and the ear tip, neck end and jaw tip sit on x=10 and x=38. All four
  extremes lie on the VRECT_M box with no stretch.
- stroke-width (2.55 traced, target 4): authored at stroke 4. The mouth is
  rebuilt wider than the trace: the upper jaw is 8.3 from the lower-jaw tip
  and 9.6 from the throat corner. At the trace's proportions the upper jaw and
  the under-jaw line were 4.4 apart, which failed the MIC check.
Dropped: the small fur tuft (zigzag) on the chest. It is about 2 units in the
trace and fills in at stroke 4. The lower jaw is lowered from the image's
upturned angle, because a shorter V cannot keep 8 between the jaws.
Lucide: no wolf/howl glyph. The construction follows Lucide `dog`/`cat`:
one continuous outline with pointed ears as straight-edged corners.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "02bbed8d-19bf-42c9-9539-d93fbda86791"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1517-howling-wolf/howling-wolf_raw.svg"
AUTHOR = "claude-opus-5-5"

NECK = (10, 36)
NAPE = (17, 22)
EAR = (10, 13)
BROW = (19, 15)
NOSE = (33, 4)
NOSE_FRONT = (36, 7)
MOUTH = (29, 16)
JAW = (38, 18)
THROAT = (35, 24)
CHEST = (31, 44)


class HowlingWolfRedraw(Solo48):
    icon_id = "howling-wolf-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ("wolf howling", "howl")
    keywords = ("wolf", "howl", "howling", "canine", "wild", "night", "moon", "animal")

    def build(self) -> None:
        self.add_bezier("neck", NECK, ((11, 31), (17, 28), NAPE))
        self.add_line("ear-back", NAPE, EAR)
        self.add_line("ear-front", EAR, BROW)
        self.add_bezier("brow", BROW, ((22, 11), (27, 8), NOSE))
        self.add_line("nose", NOSE, NOSE_FRONT)
        self.add_line("upper-jaw", NOSE_FRONT, MOUTH)
        self.add_line("lower-jaw", MOUTH, JAW)
        self.add_line("jaw-under", JAW, THROAT)
        self.add_bezier("chest", THROAT, ((33, 28), (38, 35), CHEST))
        self.add_contour("wolf", "neck", "ear-back", "ear-front", "brow", "nose",
                         "upper-jaw", "lower-jaw", "jaw-under", "chest")
