"""A hand reaching in from the upper right, its thumb pinching the top-right corner of a portrait identity card.

Plan: root = the scene; card and hand form one physical grip.
- Card: portrait rounded rectangle (r4). Its top edge stops where the back of
  the hand crosses it (the fingers pass behind the card) and its right edge
  stops on the thumb, so the hand hides the card's top-right corner as in the
  reference. The card owns a portrait, set left of the thumb like an ID photo:
  circular head (r3) above an elliptical shoulder arch standing on the card's
  bottom edge, with the exact 8u centerline (4u ink) head-to-body gap of the
  shared human reference.
- Hand: every run shares the steep 3-4-5 direction (3,-4) toward the wrist at
  the upper right. The thumb lies in front of the card: an r5 capsule end
  (offsets (4,3)) split where the card's right edge meets it; its upper edge is
  the thumb crease running to the top bound, its lower edge exits at the right
  bound. The short back-of-hand run leaves the card top 9.6u above the crease.
Keyshape: SQUARE, centerline box (6,6)-(42,42).
Reduction: the knuckle bump and the separate index-finger line are dropped;
the long thumb and the back-of-hand run carry the grip. The bust is narrowed
(shoulder half-width 4) to keep 9u clear of the card wall and the thumb. The
portrait's flat base becomes shoulders standing on the card edge (Lucide
contact construction).
Construction reference: Lucide `contact-round` (portrait on a card edge) and
`id-card`; hand band construction follows the thumb of `hand-coins`.
Human reference: icon_set/references/human_ref/user.svg (bust proportions and
detached head gap).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "cb16642c-e584-52b6-ae9d-bff1579af112"
SOURCE_PATH = "/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/apps/digital policies data breach user_cb16642c-e584-52b6-ae9d-bff1579af112.svg"
EXPORTED_REFERENCE_PATH = "work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/digital policies data breach user_cb16642c-e584-52b6-ae9d-bff1579af112.svg"
AUTHOR = "claude-opus-5"


class HandHoldingIdentityCardBatch001R3(Solo48):
    icon_id = "hand-holding-identity-card-batch-001-r3"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "apps"
    aliases = ("digital-policies-data-breach-user", "show-id-card")
    keywords = ("hand", "identity", "card", "id", "badge", "user", "verification", "holding")

    def build(self) -> None:
        # Thumb: tip centre C, radius 5; edges offset by (-4,-3)/(4,3); runs along (3,-4).
        cx, cy, tip_r = 35, 21, 5
        thumb_upper, thumb_lower = (cx - 4, cy - 3), (cx + 4, cy + 3)
        thumb_front, thumb_tip, card_meet = (cx - 5, cy), (cx - 3, cy + 4), (cx + 3, cy + 4)
        wrist = lambda p, k: (p[0] + 3 * k, p[1] - 4 * k)  # noqa: E731  steps toward the wrist
        # Card: right edge ends on the thumb; top edge ends at the back of the hand.
        left, top, right, bottom, r = 6, 14, card_meet[0], 42, 4
        grip = (23, top)

        self.add_line("card-top", grip, (left + r, top))
        self.add_arc("card-corner-tl", (left + r, top), (left, top + r), radius_x=r, sweep=False)
        self.add_line("card-left", (left, top + r), (left, bottom - r))
        self.add_arc("card-corner-bl", (left, bottom - r), (left + r, bottom), radius_x=r, sweep=False)
        axis_x, shoulder_rx, shoulder_ry = 19, 4, 4
        s_left, s_right = (axis_x - shoulder_rx, bottom), (axis_x + shoulder_rx, bottom)
        neck = (axis_x, bottom - shoulder_ry)
        self.add_line("card-bottom-left", (left + r, bottom), s_left)
        self.add_contour("card", "card-top", "card-corner-tl", "card-left", "card-corner-bl",
                         "card-bottom-left")
        self.add_line("card-bottom-right", s_right, (right - r, bottom))
        self.add_arc("card-corner-br", (right - r, bottom), (right, bottom - r), radius_x=r, sweep=False)
        self.add_line("card-right", (right, bottom - r), card_meet)
        self.add_contour("card-lower-right", "card-bottom-right", "card-corner-br", "card-right")

        # Portrait bust.
        self.add_arc("shoulder-left", s_left, neck, radius_x=shoulder_rx, radius_y=shoulder_ry)
        self.add_arc("shoulder-right", neck, s_right, radius_x=shoulder_rx, radius_y=shoulder_ry)
        self.add_contour("shoulders", "shoulder-left", "shoulder-right")
        self.relate("connect", "card-bottom-left", "shoulder-left")
        self.relate("connect", "card-bottom-right", "shoulder-right")
        head_r = 3
        head_cy = neck[1] - 8 - head_r  # exact 8u centerline gap to the shoulders
        self.add_arc("head-top", (axis_x - head_r, head_cy), (axis_x + head_r, head_cy), radius_x=head_r)
        self.add_arc("head-bottom", (axis_x + head_r, head_cy), (axis_x - head_r, head_cy), radius_x=head_r)
        self.add_contour("head", "head-top", "head-bottom", closed=True)
        self.mark_human_figure("card-portrait", head="head", torso="shoulder-left", torso_junction="end")

        # Hand.
        self.add_line("back-of-hand", grip, wrist(grip, 2))
        self.relate("connect", "card-top", "back-of-hand")
        self.add_line("thumb-crease", wrist(thumb_upper, 3), thumb_upper)
        self.add_arc("thumb-tip-upper", thumb_upper, thumb_front, radius_x=tip_r, sweep=False)
        self.add_arc("thumb-tip-front", thumb_front, thumb_tip, radius_x=tip_r, sweep=False)
        self.add_arc("thumb-tip-under", thumb_tip, card_meet, radius_x=tip_r, sweep=False)
        self.add_arc("thumb-tip-lower", card_meet, thumb_lower, radius_x=tip_r, sweep=False)
        self.add_line("thumb-lower", thumb_lower, (right + 4, thumb_lower[1] - 4))
        self.add_contour("thumb", "thumb-crease", "thumb-tip-upper", "thumb-tip-front",
                         "thumb-tip-under", "thumb-tip-lower", "thumb-lower")
        for member in ("thumb-tip-under", "thumb-tip-lower"):
            self.relate("connect", "card-right", member)
