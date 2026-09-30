"""hand-holding-banknote (redraw of the new-pipeline traced SVG).

Plan: wide subject on HRECT_L (centerline box (4,8)-(44,40)).
- note: one closed rectangle (16,8)-(44,24), 28x16, round joins give the
  Lucide banknote's soft corners. Its centre mark is a dot at (30,16), 8 from
  the top and bottom walls on centerlines.
- hand: one open contour. The forearm leaves the lower-left corner (4,40),
  bends through a smooth cubic into the level palm at y=34, runs under the
  note and curls up to a fingertip at (38,32). The palm sits 10 below the
  note; the fingertip rises only as far as the 8-unit clearance allows.
Metric issues fixed:
- clearance e0/e1 (oval 2.7 from the note wall) and e1/e2 (oval 6.7 from the
  hand): the hollow oval is replaced by a centre dot 8 from both long walls.
- clearance e0/e2 (hand fingertip 2.7 under the note): palm moved to y=34,
  fingertip stops at y=32, 8 below the note's bottom wall.
- holes at (20.3,17.7) / (38.4,14.7) / (29.1,16.2) (3.0-5.6 wide): the oval
  and its slivers are gone; the note's one opening is 12 tall inside the ink.
- keyshape-short-axis: the suggested HRECT_M (28 tall) cannot hold a note,
  an 8 gap and a hand, so HRECT_L is used and every extreme sits on its box
  (x 4/44 from wrist and note, y 8/40 from note top and wrist).
- stroke-width: the model is authored at stroke 4 with every gap budgeted at
  8 on centerlines.
Not fixable as drawn: the "large hollow oval". A ring needs a 6-unit
inscribed hole (r>=5) and 8 to each wall, so a 26-tall note; with the 8 gap
and the hand below that is 36+ of height against HRECT_L's 32. The dot is the
48-px reduction of Lucide `banknote`'s small centre circle.
no-head: not applicable, the subject is an isolated arm and hand, not a
figure, so no head, torso or mark_human_figure.
Lucide: `banknote` (rect + centre circle) for the note, `hand-coins` palm
line for the upturned hand, both simplified to stroke 4.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5a88b033-48de-5da2-bd8c-9b53bb261082"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1322-hand-holding-banknote/"
    "hand-holding-banknote_raw.svg"
)
AUTHOR = "claude-opus-5-5"

# Note
NOTE_L, NOTE_T, NOTE_R, NOTE_B = 16, 8, 44, 24
MARK = ((NOTE_L + NOTE_R) // 2, (NOTE_T + NOTE_B) // 2)   # (30,16)
# Hand
WRIST = (4, 40)
PALM_Y = NOTE_B + 10        # 34
PALM_START = (14, PALM_Y)
PALM_END = (32, PALM_Y)
TIP = (38, NOTE_B + 8)      # (38,32): exactly 8 below the note wall


class HandHoldingBanknoteRedraw(Solo48):
    icon_id = "hand-holding-banknote-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "finance/money"
    aliases = ("hand holding money", "pay cash", "cash payment")
    keywords = ("banknote", "money", "cash", "hand", "pay", "payment", "bill", "finance")

    def build(self) -> None:
        self.add_polyline(
            "note",
            (NOTE_L, NOTE_T), (NOTE_R, NOTE_T), (NOTE_R, NOTE_B), (NOTE_L, NOTE_B),
            closed=True,
        )
        self.add_dot("mark", MARK)

        # Forearm rises at 45 degrees and eases into the level palm.
        self.add_bezier("arm", WRIST, ((8, 36), (10, PALM_Y), PALM_START))
        self.add_line("palm", PALM_START, PALM_END)
        # Fingers curl up from the level palm.
        self.add_bezier("fingers", PALM_END, ((35, PALM_Y), (37, 33), TIP))
        self.add_contour("hand", "arm", "palm", "fingers")
