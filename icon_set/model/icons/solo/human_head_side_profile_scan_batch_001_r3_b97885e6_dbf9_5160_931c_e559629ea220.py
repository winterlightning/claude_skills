"""A left-facing human head in profile inside a scan frame whose edges become the head's outline.

Interpretation (the saved brief's open question): the frame is integrated
with the head rather than an independent enclosure. Its top edge flows
tangentially into the back of the skull, and its bottom edge meets the front of
the neck, exactly as the reference draws them.

Plan: one open stroke carries the whole subject: forehead hook (r4) ->
straight forehead -> 45-degree nose -> lips -> jaw back to the neck -> neck
front -> frame bottom -> frame left ->
frame top -> skull (r20 about (22,26), horizontal where it leaves the top
edge) -> nape, whose line continues the skull's tangent. The ear is a separate
C (r3) opening toward the face, at least 8.8u clear of every other run.
Keyshape: SQUARE, centerline box (6,6)-(42,42).
Reduction: the reference's separate forehead stroke joins the profile run, the
lip notch and the rounded chin become one straight lip line and jaw, and ear
detail beyond the C is omitted.
Construction reference: Lucide `scan-face` (scan corners around a head) for
the frame; human anatomy follows icon_set/references/human_ref (user.svg head
proportions). No detached head/body pair exists, so no human-figure flag or
head-gap rule applies.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "b97885e6-dbf9-5160-931c-e559629ea220"
SOURCE_PATH = "/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/artificial-intelligence/deepfake side_b97885e6-dbf9-5160-931c-e559629ea220.svg"
EXPORTED_REFERENCE_PATH = "work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/deepfake side_b97885e6-dbf9-5160-931c-e559629ea220.svg"
BRIEF_REFERENCE_PATH = "/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/artificial-intelligence/deepfake side_b97885e6-dbf9-5160-931c-e559629ea220.svg"
AUTHOR = "claude-opus-5"


class HumanHeadSideProfileScanBatch001R3(Solo48):
    icon_id = "human-head-side-profile-scan-batch-001-r3"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "artificial-intelligence"
    aliases = ("head-profile-scan", "deepfake-side")
    keywords = ("head", "profile", "scan", "face", "human", "identity", "deepfake")

    def build(self) -> None:
        left, top, bottom, corner = 6, 6, 42, 4
        skull_c, skull_r = (22, 26), 20
        skull_top = (skull_c[0], skull_c[1] - skull_r)          # (22,6) on the frame top
        nape = (skull_c[0] + 16, skull_c[1] + 12)                # (16,12,20) point on the skull
        face_x, chin_y, neck_x, jaw_y = 19, 32, 25, 34
        # Profile: small forehead hook -> straight forehead -> 45-degree nose -> lips -> jaw.
        self.add_arc("forehead-hook", (face_x + 4, 15), (face_x, 19), radius_x=4, sweep=False)
        self.add_line("forehead", (face_x, 19), (face_x, 23))
        self.add_line("nose-ridge", (face_x, 23), (face_x - 5, 28))
        self.add_line("nose-base", (face_x - 5, 28), (face_x, 29))
        self.add_line("lips", (face_x, 29), (face_x, chin_y))
        self.add_line("jaw", (face_x, chin_y), (neck_x, jaw_y))  # 8u above the frame bottom at the neck
        self.add_line("neck-front", (neck_x, jaw_y), (neck_x, bottom))
        # Frame: bottom, left and top edges, then the skull and the nape.
        self.add_line("frame-bottom", (neck_x, bottom), (left + corner, bottom))
        self.add_arc("frame-corner-bottom", (left + corner, bottom), (left, bottom - corner),
                     radius_x=corner)
        self.add_line("frame-left", (left, bottom - corner), (left, top + corner))
        self.add_arc("frame-corner-top", (left, top + corner), (left + corner, top), radius_x=corner)
        self.add_line("frame-top", (left + corner, top), skull_top)
        self.add_arc("skull", skull_top, nape, radius_x=skull_r)
        self.add_line("nape", nape, (nape[0] - 3, bottom))  # continues the skull tangent (-3,4)
        self.add_contour(
            "profile", "forehead-hook", "forehead", "nose-ridge", "nose-base", "lips", "jaw", "neck-front",
            "frame-bottom", "frame-corner-bottom", "frame-left", "frame-corner-top", "frame-top",
            "skull", "nape",
        )
        ear_c, ear_r = (30, 24), 3
        self.add_arc("ear", (ear_c[0], ear_c[1] - ear_r), (ear_c[0], ear_c[1] + ear_r), radius_x=ear_r)
