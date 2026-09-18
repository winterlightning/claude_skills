"""A front-facing human brain: two mirrored lobed hemispheres divided by a continuous vertical seam.

Plan: one closed outline mirrored about the seam x=24, plus the seam itself.
Each hemisphere is a chain of four lobes (upper, two side, lower), itself
mirrored top-to-bottom about y=24. Every lobe
apex sits exactly on the keyshape bound with an axis-aligned tangent, and each
arc from an apex to its neighbouring notch has an integer radius
r = (a^2 + b^2) / 2b, so all nodes are integer and every lobe is a true
circular arc. Notches between lobes open at 90 and 106 degrees; the two
hemispheres meet the seam at 106-degree notches top and bottom, so no cusp
pinches.
Lobe chain (left; right mirrors): T(24,8) -r10- (18,6) -r6- K1(12,12) -r6-
(6,18) -r10- K2(8,24) -r10- (6,30) -r6- K3(12,36) -r6- (18,42) -r10- B(24,40).
Keyshape: SQUARE, centerline box (6,6)-(42,42).
Reduction: the reference's four bulges per side are kept; its short inward
folds are omitted: any fold leaving a notch comes within 5.5u of the
neighbouring lobe or 6u of the seam, below the 8u clearance.
Construction reference: Lucide `brain` (overlapping round lobes about a
vertical seam, notches where lobes meet).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "4cc51cde-8646-5c24-82c4-d7386922eb24"
SOURCE_PATH = "/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/artificial-intelligence/brain_4cc51cde-8646-5c24-82c4-d7386922eb24.svg"
EXPORTED_REFERENCE_PATH = "work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/brain_4cc51cde-8646-5c24-82c4-d7386922eb24.svg"
BRIEF_REFERENCE_PATH = "/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/artificial-intelligence/brain_4cc51cde-8646-5c24-82c4-d7386922eb24.svg"
AUTHOR = "claude-opus-5"

SEAM_X = 24
# Left hemisphere, traversed top notch -> bottom notch: (node, radius of the arc arriving there).
LEFT_CHAIN = (
    ((24, 8), None),
    ((18, 6), 10),   # upper lobe apex on the top bound
    ((12, 12), 6),   # notch K1
    ((6, 18), 6),    # upper side lobe apex on the left bound
    ((8, 24), 10),   # notch K2 on the horizontal axis
    ((6, 30), 10),   # lower side lobe apex on the left bound
    ((12, 36), 6),   # notch K3
    ((18, 42), 6),   # lower lobe apex on the bottom bound
    ((24, 40), 10),  # bottom notch on the seam
)


class HumanBrainHemispheresBatch001R3(Solo48):
    icon_id = "human-brain-hemispheres-batch-001-r3"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "artificial-intelligence"
    aliases = ("brain-hemispheres", "brain")
    keywords = ("brain", "mind", "hemisphere", "anatomy", "intelligence", "neural")

    def build(self) -> None:
        mirror = lambda p: (2 * SEAM_X - p[0], p[1])  # noqa: E731
        members = []
        # Left side, top to bottom: counterclockwise on screen.
        for index in range(1, len(LEFT_CHAIN)):
            start, (end, radius) = LEFT_CHAIN[index - 1][0], LEFT_CHAIN[index]
            member = f"left-lobe-{index}"
            self.add_arc(member, start, end, radius_x=radius, sweep=False)
            members.append(member)
        # Right side, bottom to top: the mirror reversed, still counterclockwise.
        for index in range(len(LEFT_CHAIN) - 1, 0, -1):
            (start, radius), end = LEFT_CHAIN[index], LEFT_CHAIN[index - 1][0]
            member = f"right-lobe-{index}"
            self.add_arc(member, mirror(start), mirror(end), radius_x=radius, sweep=False)
            members.append(member)
        self.add_contour("outline", *members, closed=True)
        top, bottom = LEFT_CHAIN[0][0], LEFT_CHAIN[-1][0]
        self.add_line("seam", top, bottom)
        last = len(LEFT_CHAIN) - 1
        for member in ("left-lobe-1", "right-lobe-1", f"left-lobe-{last}", f"right-lobe-{last}"):
            self.relate("connect", "seam", member)
