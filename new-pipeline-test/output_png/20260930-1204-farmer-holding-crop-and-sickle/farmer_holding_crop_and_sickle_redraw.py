"""farmer-holding-crop-and-sickle (redraw of the new-pipeline traced SVG).

Plan: a frontal stick-figure farmer holding a sickle in one hand and a crop
sprig in the other, on SQUARE (centerline box (6,6)-(42,42)), the suggested
keyshape (score 1.24; every other candidate fills under 82%).
- Head: ring r5 centred on the torso axis x=24, top on y=6. Its bottom (y=16)
  is exactly GAP (8) above the neck, the start of the upright torso
  (human_ref full-body stick figure: 4 units of visible ink gap).
- Body: torso (24,24)-(24,32); two straight legs splay to the ground line
  y=42. Both arms leave the neck point and run down-outward to the hands.
- Sickle (viewer's left): a C blade r5 centred (11,24), opening toward the
  figure. It runs from the tip (15,21) over the top, round the left extreme
  (6,24) to the bottom (11,29) and continues straight down as the handle to
  (11,38); the left arm grips the handle at (11,33).
- Sprig (viewer's right): the right hand holds it at the leaf node (37,28);
  the stem runs down to (37,38) and two r8 leaves curl up from the node, the
  outer one to the right extreme (42,21) and the inner one to (34,20).
- Everything except the head is one connected body, so only the head needs
  the 8-unit clearance; inside the body every visible opening was still kept
  at 3+ units of ink.
- Six strokes: head, left arm + torso, legs, sickle (blade + handle),
  right arm + stem, leaves.
Human construction: icon_set/references/human_ref/full_body_ref.png (ring head
over an upright torso, straight splayed legs, arms from the neck). No useful
Lucide match for a sickle, a sprig in hand or a farmer.

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap was set for stroke 4.
- stroke-count (8, budget 6): fixed; the drawing is six strokes.
- keyshape-short-axis (y fills 99%): fixed; head top y=6, feet y=42, blade
  x=6 and outer leaf tip x=42 sit exactly on the SQUARE box.
- clearance e0/e3, e0/e4, e0/e7 and head-gap (head 2.92 from the neck):
  fixed; the head is exactly 8 from the neck on centerlines and 13+ from the
  arms, blade and leaves.
- clearance e0/e5 (head 5.07 from the sprig): fixed; the sprig sits low
  beside the head, its nearest leaf tip 14 from the head centre.
- clearance e1/e4 (sickle 2.3 from the arm): fixed by construction; the arm
  now joins the handle below the blade (shared, declared joint) and the blade
  opens toward the figure, so no blade ink sits over the arm.
- clearance e2/e7, e3/e5, e3/e7, e4/e7 (legs, arms, torso and sprig under 8):
  fixed; these parts are one connected body (shared joints at neck, hip and
  hands) and the leg, arm and leaf angles leave no near-parallel runs.
- hole at [24.3, 9.7] (3.26 wide): fixed; the r5 head leaves a 6-wide opening.
Deliberate changes: the sickle and sprig swap hands, and the sickle's C opens
toward the figure; with the head's 8-unit clearance a right-opening blade on
the right side sits directly over its arm. The trace's two hollow leaves
become two open curled leaves: a leaf with a 6-wide opening needs a 10-wide
lens, and two of them do not fit beside the head.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1efaaba1-675b-4453-93c8-175f701635ac"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1204-farmer-holding-crop-and-sickle/"
    "farmer-holding-crop-and-sickle_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
TOP, BOTTOM, LEFT, RIGHT = 6, 42, 6, 42       # SQUARE centerline box
HEAD_R = 5
GAP = 8                                       # head outline -> neck, centerlines
HEAD_C = (AXIS, TOP + HEAD_R)                 # (24, 11)
NECK = (AXIS, TOP + 2 * HEAD_R + GAP)         # (24, 24)
HIP = (AXIS, 32)
FEET = ((18, BOTTOM), (30, BOTTOM))
BLADE_R = 5
BLADE_C = (LEFT + BLADE_R, NECK[1])           # (11, 24): left extreme on x=6
BLADE_TIP = (BLADE_C[0] + 4, BLADE_C[1] - 3)  # 3-4-5 point on the blade circle
BLADE_BOTTOM = (BLADE_C[0], BLADE_C[1] + BLADE_R)
LEFT_HAND = (BLADE_C[0], 33)
HANDLE_END = (BLADE_C[0], 38)
NODE = (37, 28)                               # right hand = sprig leaf node
STEM_END = (NODE[0], HANDLE_END[1])
LEAF_OUT = (RIGHT, 21)
LEAF_IN = (34, 20)
LEAF_R = 8


class FarmerHoldingCropAndSickleRedraw(Solo48):
    icon_id = "farmer-holding-crop-and-sickle-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "agriculture/farming"
    aliases = ("farmer harvesting", "harvester", "farmer with sickle")
    keywords = ("farmer", "sickle", "crop", "sprout", "harvest", "agriculture",
                "farming", "person", "field")

    def build(self) -> None:
        cx, cy = HEAD_C
        r = HEAD_R
        self.add_arc("head-top", (cx - r, cy), (cx + r, cy), radius_x=r)
        self.add_arc("head-bottom", (cx + r, cy), (cx - r, cy), radius_x=r)
        self.add_contour("head", "head-top", "head-bottom", closed=True)

        # left arm into the torso: hand -> neck -> hip
        self.add_polyline("arm-torso", LEFT_HAND, NECK, HIP)
        self.mark_human_figure("farmer", head="head", torso="arm-torso-2",
                               torso_junction="start")
        self.add_polyline("legs", FEET[0], HIP, FEET[1])
        self.relate("connect", "arm-torso", "legs")

        # sickle: tip -> over the top -> left -> bottom, then the handle
        top = (BLADE_C[0], BLADE_C[1] - BLADE_R)
        self.add_arc("blade-1", BLADE_TIP, top, radius_x=BLADE_R, sweep=False)
        self.add_arc("blade-2", top, BLADE_BOTTOM, radius_x=BLADE_R, sweep=False)
        self.add_line("handle-1", BLADE_BOTTOM, LEFT_HAND)
        self.add_line("handle-2", LEFT_HAND, HANDLE_END)
        self.add_contour("sickle", "blade-1", "blade-2", "handle-1", "handle-2")
        self.relate("connect", "sickle", "arm-torso")

        # right arm into the sprig stem: neck -> hand/node -> stem end
        self.add_polyline("arm-stem", NECK, NODE, STEM_END)
        self.relate("connect", "arm-stem", "arm-torso")
        self.add_arc("leaf-in", LEAF_IN, NODE, radius_x=LEAF_R, sweep=False)
        self.add_arc("leaf-out", NODE, LEAF_OUT, radius_x=LEAF_R, sweep=False)
        self.add_contour("leaves", "leaf-in", "leaf-out")
        self.relate("connect", "leaves", "arm-stem")
