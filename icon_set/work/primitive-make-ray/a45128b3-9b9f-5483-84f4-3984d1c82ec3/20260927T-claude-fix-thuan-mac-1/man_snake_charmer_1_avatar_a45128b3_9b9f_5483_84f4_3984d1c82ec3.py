"""Man snake charmer avatar: a turbaned man beside a snake rising out of a pot.

Revision (disapproved, reason not recorded): the rejected drawing was a bust with
a curl on top of the head and a diagonal line across the chest; the snake and its
pot, the charmer's defining props, were missing and the curl read as a fruit
stalk. The original shows a turbaned man with a snake rising from a pot on his
right. Snake and pot are restored and the turban is drawn as a wrap.

Symbol plan: the man stands left, the pot sits in front of his right shoulder.
The turban is a radius-10 dome about (16,16) (top 6, sides 6/26) closed by a
straight hem; the face is a radius-8 jaw hanging from the hem at (8,16)/(24,16)
(bottom 24), so the wrap is wider than the face as in the reference. The body is
a radius-10 shoulder circle about (16,38) (top 28, 4 below the jaw: touching ink,
avatar rule, jaw and shoulder share the x=16 axis) with sides down to y=42; its
right side ends on the pot rim at (24,32), hidden behind the pot. The pot is a
rim (24,32)-(42,32) over a radius-9 bowl (bottom 41). The snake is three cubics
rising from the rim centre (33,32) in an S to a hooked head at the top (40,6),
9+ from the turban.
Omissions: the turban's diagonal fold (it splits the dome into regions below the
hole minimum) and the pot's neck flare.
Human reference: icon_set/references/human_ref/user.svg (bust proportions).
Lucide construction: 'user-round' bust; 'snake' S-curve; 'cooking-pot' bowl.
Keyshape SQUARE: centerline x 6 (head, arch) .. 42 (pot), y 6 (head, snake) .. 42.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = "a45128b3-9b9f-5483-84f4-3984d1c82ec3"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__man-snake-charmer-1-avatar/20260926T175625Z-thuan-mac-1/reference/man snake charmer_a45128b3-9b9f-5483-84f4-3984d1c82ec3.svg"
AUTHOR = "claude-opus-5-5"
HUMAN_REFERENCE = "icon_set/references/human_ref/user.svg"

HX, HY, R = 16, 16, 10
HEAD_BOTTOM = HY + 8


class ManSnakeCharmer1Avatar(Solo48):
    icon_id = "man-snake-charmer-1-avatar"
    human_construction = "bust"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ("snake-charmer", "fakir")
    keywords = ("man", "snake", "charmer", "turban", "pot", "basket", "cobra", "avatar", "bust", "portrait")

    def build(self) -> None:
        self.add_arc("turban-left", (HX - R, HY), (HX, HY - R), radius_x=R)
        self.add_arc("turban-right", (HX, HY - R), (HX + R, HY), radius_x=R)
        self.add_line("hem-right", (HX + R, HY), (HX + 8, HY))
        self.add_line("hem-mid", (HX + 8, HY), (HX - 8, HY))
        self.add_line("hem-left", (HX - 8, HY), (HX - R, HY))
        self.add_contour("turban", "turban-left", "turban-right", "hem-right", "hem-mid", "hem-left", closed=True)
        self.add_arc("jaw", (HX + 8, HY), (HX - 8, HY), radius_x=8)
        self.relate("connect", "turban", "jaw")

        # Shoulders: circle r10 about (16,38); top 28 = jaw bottom 24 + 4.
        self.add_line("body-left-side", (6, 42), (6, 38))
        self.add_arc("body-left-shoulder", (6, 38), (HX, 28), radius_x=10)
        self.add_arc("body-right-shoulder", (HX, 28), (24, 32), radius_x=10)
        self.add_contour("body", "body-left-side", "body-left-shoulder", "body-right-shoulder")
        self.relate("connect", "jaw", "body")

        self.add_line("pot-rim-left", (24, 32), (33, 32))
        self.add_line("pot-rim-right", (33, 32), (42, 32))
        self.add_arc("pot-bowl", (42, 32), (24, 32), radius_x=9)
        self.add_contour("pot", "pot-rim-left", "pot-rim-right", "pot-bowl", closed=True)
        self.relate("connect", "pot", "body")
        self.add_bezier("snake", (33, 32),
                        ((33, 27), (37, 26), (37, 21)),
                        ((37, 16), (34, 15), (34, 11)),
                        ((34, 7), (37, 6), (40, 6)))
        self.relate("connect", "pot", "snake")
