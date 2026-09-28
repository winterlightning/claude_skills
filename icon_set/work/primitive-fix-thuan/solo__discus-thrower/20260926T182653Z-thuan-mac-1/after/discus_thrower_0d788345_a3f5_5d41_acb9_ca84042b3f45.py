"""Discus thrower: an athlete winding up a discus throw -- upright torso, the
throwing arm bent back and up holding the discus, the other arm flung out and up
to the side, legs in a wide stance.

Revision (disapproved, reason not recorded): the rejected drawing tipped the
torso into a crouch with the head floating off to one side over a flat arm, and
the discus sat against the head; the original is an upright wind-up with the
head centred over the torso, the discus held high behind at the end of a bent
arm, and the free arm raised on the far side. That pose is restored.

Symbol plan (stick figure, shared human reference full_body_ref.png): head
radius 4 about (24,10) (top 6), straight above the neck (24,22): 8 on
centerlines, 4 ink. Torso (24,22)-(24,32). Free arm from the shoulder (24,24) out
and up to (42,17). Throwing arm from the shoulder back to the elbow (14,28) and
up to the hand (9,19), which holds the discus: a radius-3 ring about (9,16)
(left edge x=6). Legs from the hip (24,32): the back leg straight to (12,42),
the front leg bent through the knee (32,36) to the foot (30,42).
Human reference: icon_set/references/human_ref/full_body_ref.png.
Lucide construction: no direct match; stick figure from the human reference.
Keyshape SQUARE: centerline x 6 (discus) .. 42 (hand), y 6 (head) .. 42 (feet).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "0d788345-a3f5-5d41-acb9-ca84042b3f45"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__discus-thrower/20260926T182653Z-thuan-mac-1/reference/discus throwing_0d788345-a3f5-5d41-acb9-ca84042b3f45.svg"
AUTHOR = "claude-opus-5-5"
HUMAN_REFERENCE = "icon_set/references/human_ref/full_body_ref.png"


class DiscusThrower(Solo48):
    icon_id = "discus-thrower"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("discus-throwing", "discus")
    keywords = ("discus", "throw", "thrower", "athletics", "olympics", "sport", "track", "field")

    def ring(self, name, cx, cy, r):
        self.add_arc(f"{name}-a", (cx - r, cy), (cx, cy - r), radius_x=r)
        self.add_arc(f"{name}-b", (cx, cy - r), (cx + r, cy), radius_x=r)
        self.add_arc(f"{name}-c", (cx + r, cy), (cx, cy + r), radius_x=r)
        self.add_arc(f"{name}-d", (cx, cy + r), (cx - r, cy), radius_x=r)
        self.add_contour(name, f"{name}-a", f"{name}-b", f"{name}-c", f"{name}-d", closed=True)

    def build(self) -> None:
        self.ring("head", 24, 10, 4)
        self.add_line("neck", (24, 22), (24, 24))
        self.add_line("torso", (24, 24), (24, 32))
        self.add_contour("body", "neck", "torso")
        self.add_line("free-arm", (24, 24), (42, 17))
        self.add_polyline("throwing-arm", (24, 24), (14, 28), (9, 19))
        self.ring("discus", 9, 16, 3)
        self.add_line("back-leg", (24, 32), (12, 42))
        self.add_polyline("front-leg", (24, 32), (32, 36), (30, 42))
        for part in ("free-arm", "throwing-arm", "back-leg", "front-leg"):
            self.relate("connect", "body", part)
        self.relate("connect", "free-arm", "throwing-arm")
        self.relate("connect", "back-leg", "front-leg")
        self.relate("connect", "throwing-arm", "discus")
        self.mark_human_figure("thrower", head="head", torso="neck", torso_junction="start")
