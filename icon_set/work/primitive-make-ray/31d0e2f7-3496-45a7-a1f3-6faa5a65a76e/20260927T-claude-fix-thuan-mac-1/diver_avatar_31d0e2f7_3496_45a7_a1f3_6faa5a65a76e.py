"""Diver avatar: a snorkel diver's head -- a wide diving mask strapped across the
face, a snorkel tube running from the mouth up past the right side of the head.

Revision (disapproved, reason not recorded): the rejected drawing was a
moustached bust with a thin band across the head, so neither the mask nor the
snorkel read; the original is a head portrait whose face is covered by a wide
mask that juts past both cheeks, with the snorkel rising beside it. Mask and
snorkel are restored and the bust body (absent in the reference) is dropped.

Symbol plan: head axis x=21. Crown: radius-10 arc about (21,16) (top 6) standing
on the mask. Mask: a closed rounded band (6,16)-(33,26), radius-3 corners,
wider than the head on both sides as in the reference. Jaw: radius-10 arc about
(21,26) under the mask (chin 36). Snorkel: a J-tube from the mouth at the jaw's
6-8-10 point (27,34): two cubics drop under the chin to the bottom (34,42) and
turn up at (42,34), and the tube rises straight to (42,6), 9 from the mask.
Omissions: the mask's nose notch, the mouthpiece ring (neither keeps 8 from the
jaw) and the neck.
Human reference: icon_set/references/human_ref/user.svg (head proportions).
Lucide construction: rounded-rectangle 'glasses' band; no snorkel in Lucide.
Keyshape SQUARE: centerline x 6 (mask) .. 42 (snorkel), y 6 (crown, snorkel) .. 42 (J-bend).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "31d0e2f7-3496-45a7-a1f3-6faa5a65a76e"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__diver-avatar/20260926T182653Z-thuan-mac-1/reference/diver_31d0e2f7-3496-45a7-a1f3-6faa5a65a76e.svg"
AUTHOR = "claude-opus-5-5"
HUMAN_REFERENCE = "icon_set/references/human_ref/user.svg"

HX, R = 21, 10
MASK_TOP, MASK_BOTTOM, MASK_L, MASK_R, CORNER = 16, 26, 6, 33, 3


class DiverAvatar(Solo48):
    icon_id = "diver-avatar"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ("snorkel-diver", "scuba-diver-head")
    keywords = ("diver", "diving", "snorkel", "mask", "scuba", "underwater", "avatar", "portrait")

    def build(self) -> None:
        cl, cr = HX - R, HX + R
        self.add_arc("crown", (cl, MASK_TOP), (cr, MASK_TOP), radius_x=R)
        self.add_line("mask-top-left", (MASK_L + CORNER, MASK_TOP), (cl, MASK_TOP))
        self.add_line("mask-top-mid", (cl, MASK_TOP), (cr, MASK_TOP))
        self.add_line("mask-top-right", (cr, MASK_TOP), (MASK_R - CORNER, MASK_TOP))
        self.add_arc("mask-tr", (MASK_R - CORNER, MASK_TOP), (MASK_R, MASK_TOP + CORNER), radius_x=CORNER)
        self.add_line("mask-right", (MASK_R, MASK_TOP + CORNER), (MASK_R, MASK_BOTTOM - CORNER))
        self.add_arc("mask-br", (MASK_R, MASK_BOTTOM - CORNER), (MASK_R - CORNER, MASK_BOTTOM), radius_x=CORNER)
        self.add_line("mask-bottom-right", (MASK_R - CORNER, MASK_BOTTOM), (cr, MASK_BOTTOM))
        self.add_line("mask-bottom-mid", (cr, MASK_BOTTOM), (cl, MASK_BOTTOM))
        self.add_line("mask-bottom-left", (cl, MASK_BOTTOM), (MASK_L + CORNER, MASK_BOTTOM))
        self.add_arc("mask-bl", (MASK_L + CORNER, MASK_BOTTOM), (MASK_L, MASK_BOTTOM - CORNER), radius_x=CORNER)
        self.add_line("mask-left", (MASK_L, MASK_BOTTOM - CORNER), (MASK_L, MASK_TOP + CORNER))
        self.add_arc("mask-tl", (MASK_L, MASK_TOP + CORNER), (MASK_L + CORNER, MASK_TOP), radius_x=CORNER)
        self.add_contour("mask", "mask-top-left", "mask-top-mid", "mask-top-right", "mask-tr", "mask-right",
                         "mask-br", "mask-bottom-right", "mask-bottom-mid", "mask-bottom-left", "mask-bl",
                         "mask-left", "mask-tl", closed=True)
        self.relate("connect", "mask", "crown")
        self.add_arc("jaw-right", (cr, MASK_BOTTOM), (27, 34), radius_x=R)
        self.add_arc("jaw-left", (27, 34), (cl, MASK_BOTTOM), radius_x=R)
        self.add_contour("jaw", "jaw-right", "jaw-left")
        self.relate("connect", "mask", "jaw")
        self.add_bezier("snorkel-drop", (27, 34), ((27, 39), (30, 42), (34, 42)))
        self.add_bezier("snorkel-bend", (34, 42), ((38, 42), (42, 39), (42, 34)))
        self.add_line("snorkel-tube", (42, 34), (42, 6))
        self.add_contour("snorkel", "snorkel-drop", "snorkel-bend", "snorkel-tube")
        self.relate("connect", "jaw", "snorkel")
