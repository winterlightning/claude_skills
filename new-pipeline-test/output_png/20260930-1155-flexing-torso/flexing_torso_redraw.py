"""flexing-torso (redraw of the new-pipeline traced SVG).

Plan: a stick figure flexing both arms, mirrored about x=24, on HRECT_L
(centerline box (4,8)-(44,40)), the keyshape the metrics suggest (wide shape).
- head: 4-cardinal-arc ring, r5, centre (24,13); its top is the top extreme
  (y=8). Ring inner opening 6 (the hole floor).
- torso: one vertical line from the neck (24,26) to (24,40), the bottom
  extreme. The neck sits exactly 8 centerline units under the head outline
  (18 + 8), a 4-unit ink gap (human-reference.md).
- arms: two detached mirrored L strokes, as in the generated image. Each
  starts at the shoulder line y=26, 8 clear of the torso (inner ends x=16 and
  x=32), runs level outward, turns up through an r4 tangent elbow arc and
  rises to the fist at y=14 (about head-centre height, as in the image).
  The vertical forearms are the left/right extremes x=4 and x=44.
References: icon_set/references/human_ref/full_body_ref.png (ring head,
round-ended single-stroke limbs); Lucide has no flexing figure, so the pose
follows the generated image; the r4 rounded corner follows Lucide's
rounded-corner construction (line - quarter arc - line, tangent at both ends).

Metric issues:
- clearance e0/e1 and e0/e2 (head 5.9 from the arm inner ends): the arm inner
  ends (16,26)/(32,26) are 15.3 from the head centre, 10.3 from its outline.
- clearance e1/e3 and e2/e3 (arms 3.7 from the torso): the arm inner ends
  stop exactly 8 from the torso line.
- clearance e1/e2 (the two arms 7.4 apart): the arm ends are now 16 apart.
- keyshape-short-axis (x filled 80%): the forearms reach x=4 and x=44, so all
  four HRECT_L extremes are on the box.
- no-head (human subject, no head circle traced): the head is a true ring,
  flagged with mark_human_figure at the exact 8-unit neck gap.
- stroke-width (trace 2.46): redrawn at stroke 4 with 8-unit centerline gaps.
None left unrepaired. validate_icon() valid, build_gate.py PASS (0/0).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "40884d36-f762-4ecf-a351-e11189a03a5d"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1155-flexing-torso/flexing-torso_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24                 # body axis
HEAD_R = 5
HEAD_CY = 13            # head top at y=8 (HRECT_L top)
NECK_Y = HEAD_CY + HEAD_R + 8
FOOT_Y = 40             # HRECT_L bottom
ARM_Y = NECK_Y          # level upper arms at shoulder height
ARM_GAP = 8             # arm inner end to torso centerline
ARM_X = 20              # axis to forearm (x=4 / x=44)
ELBOW_R = 4
FIST_Y = 14


class FlexingTorsoRedraw(Solo48):
    icon_id = "flexing-torso-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/activities"
    aliases = ("flexing person", "strong person", "muscle pose")
    keywords = ("flex", "flexing", "strong", "strength", "muscle", "fitness", "gym", "biceps")

    def build(self) -> None:
        r = HEAD_R
        self.add_arc("head-1", (AX, HEAD_CY - r), (AX + r, HEAD_CY), radius_x=r, sweep=True)
        self.add_arc("head-2", (AX + r, HEAD_CY), (AX, HEAD_CY + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (AX, HEAD_CY + r), (AX - r, HEAD_CY), radius_x=r, sweep=True)
        self.add_arc("head-4", (AX - r, HEAD_CY), (AX, HEAD_CY - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        self.add_line("torso", (AX, NECK_Y), (AX, FOOT_Y))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")

        # Mirrored L arms: level from the shoulder, r4 elbow, forearm up to the fist.
        for side, s in (("left", -1), ("right", 1)):
            inner = (AX + s * ARM_GAP, ARM_Y)
            elbow_in = (AX + s * (ARM_X - ELBOW_R), ARM_Y)
            elbow_out = (AX + s * ARM_X, ARM_Y - ELBOW_R)
            fist = (AX + s * ARM_X, FIST_Y)
            self.add_line(f"{side}-upper", inner, elbow_in)
            self.add_arc(f"{side}-elbow", elbow_in, elbow_out, radius_x=ELBOW_R, sweep=(s < 0))
            self.add_line(f"{side}-forearm", elbow_out, fist)
            self.add_contour(f"{side}-arm", f"{side}-upper", f"{side}-elbow", f"{side}-forearm")
