"""dancing-person-with-music-notes (redraw of the new-pipeline traced SVG).

Plan: a stick dancer on the right, two eighth notes on the left, SQUARE
(centerline box (6,6)-(42,42)). Extremes: x=6 upper notehead, x=42 kicked
foot, y=6 dancer head top and upper stem top, y=42 planted foot and
lower notehead.
- head: 4-cardinal-arc circle r4 at (DX,10); torso vertical on the same axis,
  neck at y=22 = head bottom 14 + 8 (exact 4-unit ink gap, human-reference.md).
- arms: one shoulder bar at y=24 split on the torso, both hands raised
  diagonally (mirrored about the torso axis); torso split at the shoulder so
  the arms share its endpoint.
- legs: right leg kicked straight out to the side (3:1), left leg bent at the
  knee with the foot planted under the hip.
- notes: one repeat definition (notehead r2, stem 12, flag (5,3)) used twice;
  the upper note reaches y=6 with its stem top, the lower note steps down and
  right so its notehead sits on y=42, clear of the arm and knee. Stem 12 keeps
  each flag 8+ from its own notehead (build-gate internal spacing).
Reference: icon_set/references/human_ref/full_body_ref.png (circular head,
round-ended single-stroke limbs); Lucide `music` for the stem-on-notehead
construction (stem starts at the notehead's side point).

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4 with every gap budgeted at 8.
- stroke-count: 10 traced strokes -> 6 parts (head, torso, arms, legs, 2 notes).
- keyshape-short-axis: x extremes now land exactly on 6 and 42 (notes moved
  to the left edge, kick foot to the right edge) instead of stretching.
- clearance e0/e6, e1/e6 (upper note vs left arm): hand at (19,17), >= 9 away.
- clearance e2/e5, e2/e6, e2/e7 and hole at [26.4,13.4] (head fused to the
  neck/shoulders): head detached with an exact 8-unit centerline gap.
- clearance e3/e4 vs e5/e6 (legs vs shoulder bar): torso lengthened to 10
  (shoulders y=24, hip y=32), legs are 8+ from the shoulder bar.
- clearance e6/e9 (arm vs lower note stem): lower note moved to (10,40).
- head-gap e2: dancer head gap is exactly 8 on centerlines.
- head-gap e0, e8: false positives -- those are the music noteheads, which
  are deliberately connected to their stems, not human heads.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "71810c29-2b03-4b67-8fc7-929b40352813"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1635-dancing-person-with-music-notes/"
    "dancing-person-with-music-notes_raw.svg"
)
AUTHOR = "claude-opus-5-5"

DX = 30            # dancer torso / head axis
HEAD_R = 4
HEAD_CY = 10       # centerline top y=6
NECK_Y = 22        # HEAD_CY + HEAD_R + 8
SHOULDER_Y = 24
HIP = (DX, 32)
ARM_SPAN = 6       # shoulder corner offset from the torso
HAND = (11, 7)     # hand offset from the torso: x out, y up from the shoulders
KICK_FOOT = (42, 36)
KNEE = (25, 37)
PLANT_FOOT = (28, 42)

NOTE_R = 2
STEM = 12
FLAG = (5, 3)
NOTES = {"upper-note": (8, 18), "lower-note": (10, 40)}


class DancingPersonWithMusicNotesRedraw(Solo48):
    icon_id = "dancing-person-with-music-notes-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    aliases = ("dancer", "party music dance")
    keywords = ("dancing", "dance", "music", "notes", "party", "person")

    def _circle(self, name: str, cx: int, cy: int, r: int) -> None:
        self.add_arc(f"{name}-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc(f"{name}-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc(f"{name}-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc(f"{name}-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour(name, f"{name}-1", f"{name}-2", f"{name}-3", f"{name}-4", closed=True)

    def _note(self, name: str, cx: int, cy: int) -> None:
        self._circle(f"{name}-head", cx, cy, NOTE_R)
        sx = cx + NOTE_R
        self.add_polyline(
            f"{name}-stem", (sx, cy), (sx, cy - STEM), (sx + FLAG[0], cy - STEM + FLAG[1])
        )
        self.relate("connect", f"{name}-head", f"{name}-stem")

    def build(self) -> None:
        self._circle("head", DX, HEAD_CY, HEAD_R)

        shoulder = (DX, SHOULDER_Y)
        self.add_line("torso", (DX, NECK_Y), shoulder)
        self.add_line("waist", shoulder, HIP)
        self.relate("connect", "torso", "waist")
        self.mark_human_figure("dancer", head="head", torso="torso", torso_junction="start")

        hx, hy = HAND
        self.add_polyline(
            "arm-left", shoulder, (DX - ARM_SPAN, SHOULDER_Y), (DX - hx, SHOULDER_Y - hy)
        )
        self.add_polyline(
            "arm-right", shoulder, (DX + ARM_SPAN, SHOULDER_Y), (DX + hx, SHOULDER_Y - hy)
        )
        for arm in ("arm-left", "arm-right"):
            self.relate("connect", arm, "torso")
            self.relate("connect", arm, "waist")
        self.relate("connect", "arm-left", "arm-right")

        self.add_line("kick-leg", HIP, KICK_FOOT)
        self.add_polyline("bent-leg", HIP, KNEE, PLANT_FOOT)
        self.relate("connect", "kick-leg", "waist")
        self.relate("connect", "bent-leg", "waist")
        self.relate("connect", "kick-leg", "bent-leg")

        for name, (cx, cy) in NOTES.items():
            self._note(name, cx, cy)
