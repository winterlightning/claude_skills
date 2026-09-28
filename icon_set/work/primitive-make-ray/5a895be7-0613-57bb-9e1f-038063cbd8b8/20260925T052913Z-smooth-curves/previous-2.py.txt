"""The Android robot mascot: a domed head with two antennae over a rounded body on two short legs.

Plan: one closed outline mirrored about x=24. The dome is a tangent-continuous
chain: r10 shoulder arcs rising from vertical at the walls into an r20 crown
arc; the two radii are internally tangent at P=(12,11)/(36,11), exact integer
nodes where the antennae attach, leaving the dome close to its normal. The
body walls drop to r4 corners, and two U legs (8u inner width, r4 feet) share
the outline. A horizontal seam joins the dome's base nodes.
Keyshape: VRECT_L, centerline box (8,4)-(40,44).
Proportions follow the reference: dome 12u, body 17u, legs 8u.
Reduction: none; the blank face, blank torso and armless body are kept.
Construction reference: Lucide `bot` (antenna leaving the head outline and
a flat head seam); no mascot match exists in the local bundle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "5a895be7-0613-57bb-9e1f-038063cbd8b8"
SOURCE_PATH = "/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/apps/android_5a895be7-0613-57bb-9e1f-038063cbd8b8.svg"
EXPORTED_REFERENCE_PATH = "work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/android_5a895be7-0613-57bb-9e1f-038063cbd8b8.svg"
BRIEF_REFERENCE_PATH = "/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/apps/android_5a895be7-0613-57bb-9e1f-038063cbd8b8.svg"
AUTHOR = "claude-opus-5"


class AndroidMascotRobotIconBatch001R3(Solo48):
    icon_id = "android-mascot-robot-icon-batch-001-r3"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "apps"
    aliases = ("android-robot-mascot", "android")
    keywords = ("android", "robot", "mascot", "antenna", "technology", "mobile")

    def build(self) -> None:
        axis_x, left, top = 24, 8, 4
        right = 2 * axis_x - left
        seam_y, crown_r, shoulder_r = 19, 20, 10
        node_l, node_r = (12, 11), (2 * axis_x - 12, 11)  # r10/r20 tangency, verified integer
        body_bottom, corner_r = 36, 4
        leg_outer, leg_inner, foot_y = 12, 20, 40  # left leg walls; right leg mirrors
        mirror = lambda x: 2 * axis_x - x  # noqa: E731

        self.add_arc("shoulder-left", (left, seam_y), node_l, radius_x=shoulder_r)
        self.add_arc("crown", node_l, node_r, radius_x=crown_r)
        self.add_arc("shoulder-right", node_r, (right, seam_y), radius_x=shoulder_r)
        self.add_line("wall-right", (right, seam_y), (right, body_bottom - corner_r))
        self.add_arc("corner-right", (right, body_bottom - corner_r), (mirror(leg_outer), body_bottom),
                     radius_x=corner_r)
        self.add_line("leg-right-outer", (mirror(leg_outer), body_bottom), (mirror(leg_outer), foot_y))
        self.add_arc("foot-right", (mirror(leg_outer), foot_y), (mirror(leg_inner), foot_y),
                     radius_x=(leg_inner - leg_outer) // 2)
        self.add_line("leg-right-inner", (mirror(leg_inner), foot_y), (mirror(leg_inner), body_bottom))
        self.add_line("crotch", (mirror(leg_inner), body_bottom), (leg_inner, body_bottom))
        self.add_line("leg-left-inner", (leg_inner, body_bottom), (leg_inner, foot_y))
        self.add_arc("foot-left", (leg_inner, foot_y), (leg_outer, foot_y),
                     radius_x=(leg_inner - leg_outer) // 2)
        self.add_line("leg-left-outer", (leg_outer, foot_y), (leg_outer, body_bottom))
        self.add_arc("corner-left", (leg_outer, body_bottom), (left, body_bottom - corner_r),
                     radius_x=corner_r)
        self.add_line("wall-left", (left, body_bottom - corner_r), (left, seam_y))
        self.add_contour(
            "outline", "shoulder-left", "crown", "shoulder-right", "wall-right", "corner-right",
            "leg-right-outer", "foot-right", "leg-right-inner", "crotch", "leg-left-inner",
            "foot-left", "leg-left-outer", "corner-left", "wall-left", closed=True,
        )
        self.add_line("seam", (left, seam_y), (right, seam_y))
        for member in ("shoulder-left", "wall-left", "shoulder-right", "wall-right"):
            self.relate("connect", "seam", member)
        # Antennae leave the tangency nodes outward and up to the top edge.
        self.add_line("antenna-left", node_l, (left, top))
        self.add_line("antenna-right", node_r, (right, top))
        for member in ("shoulder-left", "crown"):
            self.relate("connect", "antenna-left", member)
        for member in ("shoulder-right", "crown"):
            self.relate("connect", "antenna-right", member)
