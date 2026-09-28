"""dancing-woman-with-music-notes (redraw of the new-pipeline traced SVG).

Plan: a stick dancer on the left, leaning into the step, with two music notes
on the right. The keyshape is SQUARE, so the centerline box is (6,6)-(42,42).
The four extremes are x=6 (the lowered hand), x=42 (the eighth-note flag end),
y=6 (the top of the head) and y=42 (both feet).
- head: a circle of four cardinal arcs, r4 at (HX,10). The neck is a short
  vertical run from (HX,22) to the shoulder, so the head sits straight above it
  with an exact 8-unit centerline gap (4 units of ink), per human-reference.md.
- torso: the shoulder node leans down and right to the hip (5:8), following the
  trace's diagonal body line.
- arms: both arms start at the shoulder node. One sweeps down to the left and
  the other reaches up to the right through an elbow, and its forearm stays
  8+ from the head outline.
- legs: both legs bend. The left leg steps down and to the left, and the right
  knee pushes out to the right before the shin comes back down to the floor.
- notes: one shared notehead (a solid r2 ring) with the stem on its east point.
  The upper note is an eighth note with a (4,3) flag and the lower note is a
  quarter note, stepped down and 2 to the right as in the trace.
References: icon_set/references/human_ref/full_body_ref.png (circular head,
round-ended single-stroke limbs), Lucide `music` (stem rising from the
notehead's side point, flag leaving the stem top).

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4 with every gap budgeted at 8.
- stroke-count: 9 traced strokes reduced to 6 parts (head, torso, arms, legs,
  and two notes).
- clearance e0/e1, e0/e3, e0/e6, e1/e6, e3/e6 (head crowding the neck, the
  raised arm and the lowered arm): the head is detached at exactly 8 above the
  neck, and both arms leave the shared shoulder node 2 below the neck, so the
  raised forearm clears the head outline.
- clearance e2/e3 (torso vs raised arm at 7.87): the arms and the torso now share
  one shoulder node and are declared connected, so no separate gap exists.
- clearance e5/e7 (upper note vs lower note stem at 5.6): the lower stem top is
  now 8+ from the upper notehead.
- loose-join e4/e5 (flag short of the stem): stem and flag are one polyline
  sharing the stem top.
- hole at [14.1,9.5] (3.1 wide): the head is now an r4 ring with a 4-wide
  inner opening, and the traced notehead holes are solid dots.
- no-head (warn): the head is an explicit circle, flagged with
  mark_human_figure("dancer", ...).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6c6896b3-8871-41eb-bf24-63a28db82e65"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1639-dancing-woman-with-music-notes/"
    "dancing-woman-with-music-notes_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HX = 15            # head / neck axis
HEAD_R = 4
HEAD_CY = 10       # centerline top y=6
NECK = (HX, 22)    # HEAD_CY + HEAD_R + 8
SHOULDER = (HX, 24)
HIP = (20, 32)
LOW_HAND = (6, 32)
ELBOW = (24, 19)
HIGH_HAND = (30, 9)
LEFT_KNEE, LEFT_FOOT = (16, 37), (11, 42)
RIGHT_KNEE, RIGHT_FOOT = (27, 37), (25, 42)

NOTE_R = 2
FLAG = (4, 3)
# name: (notehead centre, stem length, flagged)
NOTES = {"upper-note": ((36, 19), 9, True), "lower-note": ((38, 37), 8, False)}


class DancingWomanWithMusicNotesRedraw(Solo48):
    icon_id = "dancing-woman-with-music-notes-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    aliases = ("dancer", "party music dance woman")
    keywords = ("dancing", "dance", "music", "notes", "party", "woman")

    def _circle(self, name: str, cx: int, cy: int, r: int) -> None:
        self.add_arc(f"{name}-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc(f"{name}-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc(f"{name}-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc(f"{name}-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour(name, f"{name}-1", f"{name}-2", f"{name}-3", f"{name}-4", closed=True)

    def _note(self, name: str, centre: tuple[int, int], stem: int, flagged: bool) -> None:
        cx, cy = centre
        self._circle(f"{name}-head", cx, cy, NOTE_R)
        sx = cx + NOTE_R
        points = [(sx, cy), (sx, cy - stem)]
        if flagged:
            points.append((sx + FLAG[0], cy - stem + FLAG[1]))
        self.add_polyline(f"{name}-stem", *points)
        self.relate("connect", f"{name}-head", f"{name}-stem")

    def build(self) -> None:
        self._circle("head", HX, HEAD_CY, HEAD_R)

        self.add_line("torso", NECK, SHOULDER)
        self.add_line("waist", SHOULDER, HIP)
        self.relate("connect", "torso", "waist")
        self.mark_human_figure("dancer", head="head", torso="torso", torso_junction="start")

        self.add_line("arm-low", SHOULDER, LOW_HAND)
        self.add_polyline("arm-high", SHOULDER, ELBOW, HIGH_HAND)
        for arm in ("arm-low", "arm-high"):
            self.relate("connect", arm, "torso")
            self.relate("connect", arm, "waist")
        self.relate("connect", "arm-low", "arm-high")

        self.add_polyline("leg-left", HIP, LEFT_KNEE, LEFT_FOOT)
        self.add_polyline("leg-right", HIP, RIGHT_KNEE, RIGHT_FOOT)
        self.relate("connect", "leg-left", "waist")
        self.relate("connect", "leg-right", "waist")
        self.relate("connect", "leg-left", "leg-right")

        for name, (centre, stem, flagged) in NOTES.items():
            self._note(name, centre, stem, flagged)
