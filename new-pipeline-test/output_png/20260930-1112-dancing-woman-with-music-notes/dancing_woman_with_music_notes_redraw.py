"""dancing-woman-with-music-notes (redraw of the new-pipeline traced SVG).

Plan: stick-figure dancer on the left, two eighth notes stacked on the right,
on SQUARE (centerline box (6,6)-(42,42)).
- head: 4-cardinal-arc ring, r4, centre (HX,10). The neck S sits exactly 8
  centerline units under the head outline (4-unit ink gap, human-reference.md),
  centred on the vertical torso axis x=HX.
- arms: one smooth wave through the shoulder. Left arm raised: hand (6,6) is
  the top-left extreme, a vertical run down to (6,14), an r8 quarter arc to
  (14,22) and a level run into S. Right arm leaves S on the same horizontal
  tangent (tangent-continuous across the shoulder) and dips to the hand
  (29,27), which reaches into the space between the notes. The level run
  into the neck is a standalone line so the exact head gap certifies.
- torso + standing leg: vertical x=HX from S to the foot (HX,42), the bottom
  extreme, split at the hip where the bent leg attaches.
- bent leg: a back heel-kick. Thigh down-left to the knee (11,38), 8 clear
  of the standing leg; shin up-left to the lifted foot (6,31) at the left
  extreme.
- notes: ring head r3 (the exempt 6-circle, reads as a near-solid note head),
  a 11-unit stem up from the head's right tangent point, flag (4,1) to x=42
  (the right extreme). Upper note at (35,17), lower at (35,39) (bottom 42);
  the stem top sits 11 from its own head centre (internal spacing) and the
  lower stem top 11+ from the upper head.
References: icon_set/references/human_ref/full_body_ref.png (ring head,
round-ended single-stroke limbs); Lucide `music` (ring note heads on stems);
Lucide has no dancer, so the pose follows the generated image.

Metric issues:
- clearance e0/e3, e1/e3 and head-gap e3 (head 2.9 from the arms/torso): the
  neck is exactly 8 under the head outline and the arms run level at the neck.
- head-gap e4 (a note head misread as a human head, 0 from its stem): not a
  head; the note heads are joined to their stems on purpose (connect).
- clearance e0/e4, e0/e5, e0/e8, e4/e6, e4/e8, e7/e8 (the right hand, notes
  and the stray dot e7 crowding each other): the hand stops between the
  notes, 8+ from both rings and the lower stem; the notes are stacked 8+
  apart; the stray dot e7 is dropped.
- clearance e0/e2, e1/e2 and holes at (17.3,9.8) and (23.0,29.1): the bent
  leg no longer tucks against the standing leg under the right arm. It kicks
  back to the left under the raised arm, knee 8 clear of the standing leg,
  so no sliver hole remains. (The image bends the leg forward to the right;
  there its knee cannot be 8 clear of the lower note and the hand in the
  36-unit box, so that leg's direction changed.) The hole at (17.3,9.8) was
  the traced head ring (2.7 wide); the redrawn r4 head is a ring primitive.
- stroke-count (9 vs 6): head, arms, torso+leg, bent leg, two notes = 6 strokes.
- stroke-width (trace 2.77): redrawn at stroke 4 with 8-unit centerline gaps.
None left unrepaired. validate_icon() valid, build_gate.py PASS (0/0).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6c6896b3-8871-41eb-bf24-63a28db82e65"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1112-dancing-woman-with-music-notes/"
    "dancing-woman-with-music-notes_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HX = 19                 # head / torso axis
HEAD_R = 4
HEAD_CY = 10            # head top at y=6 (SQUARE top)
NECK = (HX, 22)         # HEAD_CY + HEAD_R + 8
HIP = (HX, 31)
FOOT = (HX, 42)
LEFT_HAND = (6, 6)
ARM_R = 8               # raised-arm elbow arc
HAND = (29, 27)
KNEE = (11, 38)
LIFTED_FOOT = (6, 31)
NOTE_R = 3
NOTES = {               # name: (head centre, stem top y)
    "note-top": ((35, 17), 6),
    "note-low": ((35, 39), 28),
}
FLAG = (4, 1)           # flag run from the stem top


class DancingWomanWithMusicNotesRedraw(Solo48):
    icon_id = "dancing-woman-with-music-notes-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/activities"
    aliases = ("dancer", "dancing person", "woman dancing")
    keywords = ("dance", "dancing", "music", "notes", "party", "rhythm", "woman")

    def ring(self, name: str, centre: tuple[int, int], r: int) -> None:
        cx, cy = centre
        self.add_arc(f"{name}-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc(f"{name}-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc(f"{name}-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc(f"{name}-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour(name, f"{name}-1", f"{name}-2", f"{name}-3", f"{name}-4", closed=True)

    def build(self) -> None:
        self.ring("head", (HX, HEAD_CY), HEAD_R)

        # Torso and standing leg, split at the hip for the bent leg.
        self.add_line("torso", NECK, HIP)
        self.add_line("leg", HIP, FOOT)
        self.relate("connect", "torso", "leg")
        self.mark_human_figure("dancer", head="head", torso="torso", torso_junction="start")

        # Raised left arm: hand -> vertical -> r8 elbow arc -> level into the neck.
        lx, ly = LEFT_HAND
        elbow_top = (lx, NECK[1] - ARM_R)
        elbow_bottom = (lx + ARM_R, NECK[1])
        self.add_line("left-forearm", LEFT_HAND, elbow_top)
        self.add_arc("left-elbow", elbow_top, elbow_bottom, radius_x=ARM_R, sweep=False)
        self.add_line("left-upper", elbow_bottom, NECK)
        self.add_contour("left-arm", "left-forearm", "left-elbow")
        # The level run under the head stays a standalone line so the exact
        # 8-unit head gap certifies against the ring's cardinal arcs.
        self.relate("connect", "left-arm", "left-upper")
        # Right arm: leaves the neck on the same level tangent, dips to the hand.
        self.add_bezier("right-arm", NECK, ((24, 22), (25, 28), HAND))
        self.relate("connect", "left-upper", "torso")
        self.relate("connect", "right-arm", "torso")
        self.relate("connect", "left-upper", "right-arm")

        # Bent leg: level thigh back to the knee, shin tucked toward the standing leg.
        self.add_polyline("bent-leg", HIP, KNEE, LIFTED_FOOT)
        self.relate("connect", "bent-leg", "torso")
        self.relate("connect", "bent-leg", "leg")

        # Eighth notes: ring head, stem from its right tangent point, short flag.
        for name, ((cx, cy), top) in NOTES.items():
            self.ring(f"{name}-head", (cx, cy), NOTE_R)
            sx = cx + NOTE_R
            self.add_line(f"{name}-stem", (sx, cy), (sx, top))
            self.add_line(f"{name}-flag", (sx, top), (sx + FLAG[0], top + FLAG[1]))
            self.add_contour(name, f"{name}-stem", f"{name}-flag")
            self.relate("connect", f"{name}-head", name)
