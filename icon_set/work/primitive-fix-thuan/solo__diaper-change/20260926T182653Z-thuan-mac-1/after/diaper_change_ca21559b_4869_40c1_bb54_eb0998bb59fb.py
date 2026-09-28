"""Diaper change: a parent bending over a changing table, reaching down to a baby
lying on it.

Revision (disapproved, reason not recorded): in the rejected drawing the parent
was an upright stick with a stub arm, and the baby was a vertical bar beside a
ring floating over a loose line, so no one was bending over anyone. The original
shows the parent bent forward from the hips with both arms reaching down to a
baby lying on its back on the table. That pose is restored.

Symbol plan (stick figures, shared human reference full_body_ref.png):
Parent, standing at the table's left end: head radius 4 about (12,10) (top 6),
neck (12,22) 8 below the head outline, torso to the hip (12,30), legs to (6,42)
and (16,42). The arm leaves the shoulder (12,24) and reaches forward and down to
the baby's hips (20,27), where the hands change the diaper.
Baby, lying on its back on the table: torso (20,27)-(28,27), head radius 3 about
(39,27) level beside it (8 on centerlines); legs raised and bent from the hips
up to (24,19), as in the reference.
Table: top (24,39)-(42,39), 9 below the baby's head, with legs at x=25 and x=40.
A bent-over parent (attempts/bent-parent-attempt.py.txt) put the head 12 units
beside a level neck and fused the baby's leg into the parent's hip; the upright
parent keeps the head certified straight above the neck.
Omissions: the parent's skirt and the baby's second leg and arms (no 8-unit room
between the figures).
Human reference: icon_set/references/human_ref/full_body_ref.png.
Lucide construction: no direct match; stick figures from the human reference.
Keyshape SQUARE: centerline x 6 (parent's back foot) .. 42 (baby head, table),
y 6 (parent head) .. 42 (feet, table legs).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ca21559b-4869-40c1-bb54-eb0998bb59fb"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__diaper-change/20260926T182653Z-thuan-mac-1/reference/family baby change diaper_ca21559b-4869-40c1-bb54-eb0998bb59fb.svg"
AUTHOR = "claude-opus-5-5"
HUMAN_REFERENCE = "icon_set/references/human_ref/full_body_ref.png"


class DiaperChange(Solo48):
    icon_id = "diaper-change"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/family"
    aliases = ("baby-changing", "changing-table")
    keywords = ("diaper", "nappy", "change", "baby", "parent", "family", "changing", "table")

    def ring(self, name, cx, cy, r):
        self.add_arc(f"{name}-a", (cx - r, cy), (cx, cy - r), radius_x=r)
        self.add_arc(f"{name}-b", (cx, cy - r), (cx + r, cy), radius_x=r)
        self.add_arc(f"{name}-c", (cx + r, cy), (cx, cy + r), radius_x=r)
        self.add_arc(f"{name}-d", (cx, cy + r), (cx - r, cy), radius_x=r)
        self.add_contour(name, f"{name}-a", f"{name}-b", f"{name}-c", f"{name}-d", closed=True)

    def build(self) -> None:
        # Parent
        self.ring("parent-head", 12, 10, 4)
        self.add_line("parent-neck", (12, 22), (12, 24))
        self.add_line("parent-torso", (12, 24), (12, 30))
        self.add_contour("parent-body", "parent-neck", "parent-torso")
        self.add_line("parent-leg-back", (12, 30), (6, 42))
        self.add_line("parent-leg-front", (12, 30), (16, 42))
        self.add_line("parent-arm", (12, 24), (20, 27))
        for part in ("parent-leg-back", "parent-leg-front", "parent-arm"):
            self.relate("connect", "parent-body", part)
        self.relate("connect", "parent-leg-back", "parent-leg-front")
        self.mark_human_figure("parent", head="parent-head", torso="parent-neck", torso_junction="start")

        # Baby
        self.add_line("baby-torso", (20, 27), (28, 27))
        self.ring("baby-head", 39, 27, 3)
        self.add_line("baby-leg", (20, 27), (24, 19))
        self.relate("connect", "baby-torso", "baby-leg")
        self.relate("connect", "baby-torso", "parent-arm")
        self.relate("connect", "baby-leg", "parent-arm")
        self.mark_human_figure("baby", head="baby-head", torso="baby-torso", torso_junction="end")

        # Changing table
        self.add_line("table-top-left", (24, 39), (25, 39))
        self.add_line("table-top-mid", (25, 39), (40, 39))
        self.add_line("table-top-right", (40, 39), (42, 39))
        self.add_contour("table-top", "table-top-left", "table-top-mid", "table-top-right")
        self.add_line("table-leg-left", (25, 39), (25, 42))
        self.add_line("table-leg-right", (40, 39), (40, 42))
        self.relate("connect", "table-top", "table-leg-left")
        self.relate("connect", "table-top", "table-leg-right")
