"""Two wireless earbuds standing in their charging case, with the case's charge indicator lit.

Plan: root = the case, a rounded rectangle with square-ish top corners (r4) and
generous bottom corners (r8). It owns two earbuds mirrored about x=24. Each bud
is a "P": its straight stem runs up the head's inner side (as the reference's
stem continues the head's inner wall), and a half-ellipse bowl bulges outward
from the stem top to a lower stem node, closing the head. A centred indicator
dot sits on the case front.
Keyshape: VRECT_L, centerline box (8,4)-(40,44).
Reduction: the outlined lightning bolt becomes the case's status-light dot:
a zigzag needs parallel runs 8u apart plus 8u case clearance, which the 19u
case cannot hold together with the buds. Speaker-grille ticks are dropped.
Construction reference: Lucide `headphones` (rounded ear cups joined by clean
tangent strokes); no earbuds match exists in the local bundle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_001_r3_shapes import rounded_rect

SOURCE_ICON_ID = "9ae8162b-1fa3-4f3e-a7f2-5375c421b45f"
SOURCE_PATH = "/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/audio/earpods charge_9ae8162b-1fa3-4f3e-a7f2-5375c421b45f.svg"
EXPORTED_REFERENCE_PATH = "work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/earpods charge_9ae8162b-1fa3-4f3e-a7f2-5375c421b45f.svg"
AUTHOR = "claude-opus-5"


class WirelessEarbudsChargingCaseBatch001R3(Solo48):
    icon_id = "wireless-earbuds-charging-case-batch-001-r3"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "audio"
    categories = ("audio", "primitives")
    aliases = ("earpods-charge", "earbuds-case")
    keywords = ("earbuds", "earpods", "wireless", "charging", "case", "audio", "headphones")

    def build(self) -> None:
        axis_x = 24
        case_left, case_right, case_bottom = 8, 40, 44
        stem_offset, head_top, bowl_rx, bowl_ry = 5, 4, 8, 6
        head_bottom = head_top + 2 * bowl_ry
        case_top = head_bottom + 9  # 9u: the case contour is curved
        stems = []
        for side, sign in (("left", -1), ("right", 1)):
            x = axis_x + sign * stem_offset
            upper, lower, bowl = f"stem-{side}-upper", f"stem-{side}-lower", f"bowl-{side}"
            self.add_line(upper, (x, head_top), (x, head_bottom))
            self.add_line(lower, (x, head_bottom), (x, case_top))
            # Half ellipse bulging outward: counterclockwise on the left, clockwise on the right.
            self.add_arc(bowl, (x, head_bottom), (x, head_top), radius_x=bowl_rx, radius_y=bowl_ry,
                         sweep=sign < 0)
            self.add_contour(f"bud-{side}", upper, lower)
            self.relate("connect", upper, bowl)
            self.relate("connect", lower, bowl)
            self.relate("connect", upper, lower)
            stems.append((lower, x))
        case = rounded_rect(self, "case", case_left, case_top, case_right, case_bottom,
                            corners=(4, 4, 8, 8), top_nodes=tuple(x for _, x in stems))
        for stem, x in stems:
            for member in case[(x, case_top)]:
                self.relate("connect", member, stem)
        self.add_dot("charge-indicator", (axis_x, (case_top + case_bottom) // 2))
