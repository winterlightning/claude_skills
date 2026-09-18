"""An outlined upward block arrow whose shaft breaks into dashes toward its tail.

Plan: one open outline mirrored about x=24: a 45-degree triangular head, short
shoulders, and two parallel shaft sides 12u apart. Each shaft side is a series
along its own x: a solid run, an 8u gap and a detached dash reaching the base.
Keyshape: VRECT_L, centerline box (8,4)-(40,44).
Reduction: the reference's two dashes per side become one; the second cannot
keep 8u gaps inside the 24u shaft.
Construction reference: Lucide `arrow-big-up` (outlined block arrow head,
shoulders and shaft).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "5443e1f9-f37f-4884-b268-88955bf863e3"
SOURCE_PATH = "/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/arrows/arrow dash up_5443e1f9-f37f-4884-b268-88955bf863e3.svg"
EXPORTED_REFERENCE_PATH = "work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/arrow dash up_5443e1f9-f37f-4884-b268-88955bf863e3.svg"
BRIEF_REFERENCE_PATH = "/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/arrows/arrow dash up_5443e1f9-f37f-4884-b268-88955bf863e3.svg"
AUTHOR = "claude-opus-5"


class UpwardPointingDashedArrowBatch001R3(Solo48):
    icon_id = "upward-pointing-dashed-arrow-batch-001-r3"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "arrows"
    aliases = ("dashed-upward-arrow", "arrow-dash-up")
    keywords = ("arrow", "up", "upward", "dashed", "direction", "navigation")

    def build(self) -> None:
        axis_x, apex_y, head_half, shaft_half = 24, 4, 16, 6
        shoulder_y = apex_y + head_half  # 45-degree head
        solid_end, gap, base = shoulder_y + 10, 8, 44
        l_head, r_head = axis_x - head_half, axis_x + head_half
        l_shaft, r_shaft = axis_x - shaft_half, axis_x + shaft_half
        self.add_polyline(
            "outline",
            (l_shaft, solid_end), (l_shaft, shoulder_y), (l_head, shoulder_y), (axis_x, apex_y),
            (r_head, shoulder_y), (r_shaft, shoulder_y), (r_shaft, solid_end),
        )
        self.add_line("dash-left", (l_shaft, solid_end + gap), (l_shaft, base))
        self.add_line("dash-right", (r_shaft, solid_end + gap), (r_shaft, base))
