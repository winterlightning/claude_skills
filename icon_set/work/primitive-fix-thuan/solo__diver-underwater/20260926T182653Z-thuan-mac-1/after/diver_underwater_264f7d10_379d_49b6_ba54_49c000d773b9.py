"""Diver underwater: a free diver swimming head-first below the water surface,
fins trailing behind and one arm reaching down ahead.

Revision (disapproved, reason not recorded): the rejected drawing left out the
water surface (the scalloped wave line that says "underwater"), its fin was a
thin triangle fused into the leg, and the swimmer's head floated just above a
flat arm. The original shows the wave line across the top with the diver swimming
below it. The surface is restored and the swimmer redrawn.

Symbol plan (stick figure, shared human reference full_body_ref.png):
Surface: four downward scallops, radius-5 arcs between cusps (6,6)..(42,6).
Swimmer: level torso (15,30)-(25,30); head radius-3 ring about (36,30) level
beside the neck (8 on centerlines); the leg trails up-left from the hip to the
ankle (9,22), where the fin crosses it as a plate (6,26)-(12,18); the arm leaves
the shoulder (23,30) and reaches down ahead to (30,42), 8+ below the head.
Omissions: the vertical rope line at the right (it cannot keep 8 from the head
inside the keyshape) and the second leg.
Human reference: icon_set/references/human_ref/full_body_ref.png.
Lucide construction: 'waves' scallops.
Keyshape SQUARE: centerline x 6 (surface, fin) .. 42 (surface), y 6 .. 42 (hand).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "264f7d10-379d-49b6-ba54-49c000d773b9"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__diver-underwater/20260926T182653Z-thuan-mac-1/reference/diving scuba free diving_264f7d10-379d-49b6-ba54-49c000d773b9.svg"
AUTHOR = "claude-opus-5-5"
HUMAN_REFERENCE = "icon_set/references/human_ref/full_body_ref.png"


class DiverUnderwater(Solo48):
    icon_id = "diver-underwater"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "outdoors"
    aliases = ("free-diver", "scuba-diving")
    keywords = ("diving", "scuba", "diver", "underwater", "freediving", "swimming", "sea", "fin")

    def build(self) -> None:
        cusps = [(6, 6), (15, 6), (24, 6), (33, 6), (42, 6)]
        names = []
        for i, (a, b) in enumerate(zip(cusps, cusps[1:])):
            self.add_arc(f"wave-{i}", a, b, radius_x=5, sweep=False)
            names.append(f"wave-{i}")
        self.add_contour("surface", *names)

        cx, cy, r = 36, 30, 3
        self.add_arc("head-a", (cx - r, cy), (cx, cy - r), radius_x=r)
        self.add_arc("head-b", (cx, cy - r), (cx + r, cy), radius_x=r)
        self.add_arc("head-c", (cx + r, cy), (cx, cy + r), radius_x=r)
        self.add_arc("head-d", (cx, cy + r), (cx - r, cy), radius_x=r)
        self.add_contour("head", "head-a", "head-b", "head-c", "head-d", closed=True)
        self.add_line("torso-back", (15, 30), (23, 30))
        self.add_line("torso-neck", (23, 30), (25, 30))
        self.add_contour("torso", "torso-back", "torso-neck")
        self.add_line("leg", (15, 30), (9, 22))
        self.add_line("fin-low", (6, 26), (9, 22))
        self.add_line("fin-high", (9, 22), (12, 18))
        self.add_contour("fin", "fin-low", "fin-high")
        self.add_line("arm", (23, 30), (30, 42))
        self.relate("connect", "torso", "leg")
        self.relate("connect", "torso", "arm")
        self.relate("connect", "leg", "fin")
        self.mark_human_figure("diver", head="head", torso="torso-neck", torso_junction="end")
