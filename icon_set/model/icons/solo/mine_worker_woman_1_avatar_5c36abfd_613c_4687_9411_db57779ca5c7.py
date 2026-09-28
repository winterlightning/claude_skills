"""Mine worker woman avatar: a woman in a miner's hard hat with a headlamp on its
crown and a wide brim, her bob of hair hanging from under the brim.

Revision (disapproved, reason not recorded): the rejected drawing squeezed a small
ring head under a helmet with its lamp as a ring inside the dome, stuck short bars
out of the brim as hair and hung a boxy body below, so it read neither as a woman
nor as the reference. The original is a head portrait: a tall hard-hat dome with
the lamp at its crown, a brim wider than the dome, a long face below it and hair
falling past the cheeks and curling in at the bottom. That is restored.

Symbol plan: mirror axis x=24. The lamp is a radius-5 ring about (24,9) (top 4), as large as the reference's.
The dome is two cubics from the brim at (11,23)/(37,23) rising to the lamp's side
points (21,7)/(27,7), meeting them level. The brim is one line (8,23)-(40,23), 9 below the lamp.
The face hangs from the brim at (16,23)/(32,23): straight cheeks to y=30 and a
radius-8 jaw (chin 38). The hair falls from the brim ends straight down x=8/40,
8 from the cheeks, and curls in to (12,44)/(36,44).
Omissions: the shoulders (the reference is a head portrait with none) and the hair's inner strands (no 8-unit room beside the face).
Human reference: icon_set/references/human_ref/user.svg (head proportions).
Lucide construction: 'hard-hat' dome and brim; 'circle' lamp.
Keyshape VRECT_L: centerline x 8..40 (brim, hair), y 4 (lamp) .. 44 (hair).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "5c36abfd-613c-4687-9411-db57779ca5c7"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__mine-worker-woman-1-avatar/20260926T175625Z-thuan-mac-1/reference/mine worker woman_5c36abfd-613c-4687-9411-db57779ca5c7.svg"
AUTHOR = "claude-opus-5-5"
HUMAN_REFERENCE = "icon_set/references/human_ref/user.svg"

CX = 24
LAMP_Y, LAMP_R = 9, 5
BRIM_Y = 23
CHEEK_BOTTOM, JAW_R = 30, 8


class MineWorkerWoman1Avatar(Solo48):
    icon_id = "mine-worker-woman-1-avatar-solo"
    human_construction = "bust"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ("miner-woman", "coal-miner-woman")
    keywords = ("woman", "mine", "miner", "worker", "hard", "hat", "helmet", "headlamp", "avatar", "portrait")

    def build(self) -> None:
        ll, lr = (CX - LAMP_R, LAMP_Y), (CX + LAMP_R, LAMP_Y)
        self.add_arc("lamp-top-left", ll, (CX, LAMP_Y - LAMP_R), radius_x=LAMP_R)
        self.add_arc("lamp-top-right", (CX, LAMP_Y - LAMP_R), lr, radius_x=LAMP_R)
        self.add_arc("lamp-bottom-right", lr, (CX, LAMP_Y + LAMP_R), radius_x=LAMP_R)
        self.add_arc("lamp-bottom-left", (CX, LAMP_Y + LAMP_R), ll, radius_x=LAMP_R)
        self.add_contour("lamp", "lamp-top-left", "lamp-top-right", "lamp-bottom-right", "lamp-bottom-left", closed=True)
        self.add_bezier("dome-left", (11, BRIM_Y), ((11, 14), (14, LAMP_Y), ll))
        self.add_bezier("dome-right", lr, ((34, LAMP_Y), (37, 14), (37, BRIM_Y)))
        self.relate("connect", "lamp", "dome-left")
        self.relate("connect", "lamp", "dome-right")

        fl, fr = CX - JAW_R, CX + JAW_R
        self.add_line("brim-1", (8, BRIM_Y), (11, BRIM_Y))
        self.add_line("brim-2", (11, BRIM_Y), (fl, BRIM_Y))
        self.add_line("brim-3", (fl, BRIM_Y), (fr, BRIM_Y))
        self.add_line("brim-4", (fr, BRIM_Y), (37, BRIM_Y))
        self.add_line("brim-5", (37, BRIM_Y), (40, BRIM_Y))
        self.add_contour("brim", "brim-1", "brim-2", "brim-3", "brim-4", "brim-5")
        self.relate("connect", "brim", "dome-left")
        self.relate("connect", "brim", "dome-right")

        self.add_line("cheek-left", (fl, BRIM_Y), (fl, CHEEK_BOTTOM))
        self.add_arc("jaw", (fl, CHEEK_BOTTOM), (fr, CHEEK_BOTTOM), radius_x=JAW_R, sweep=False)
        self.add_line("cheek-right", (fr, CHEEK_BOTTOM), (fr, BRIM_Y))
        self.add_contour("face", "cheek-left", "jaw", "cheek-right")
        self.relate("connect", "brim", "face")

        self.add_line("hair-left", (8, BRIM_Y), (8, 36))
        self.add_bezier("hair-left-curl", (8, 36), ((8, 40), (9, 44), (12, 44)))
        self.add_contour("hair-left-lock", "hair-left", "hair-left-curl")
        self.add_line("hair-right", (40, BRIM_Y), (40, 36))
        self.add_bezier("hair-right-curl", (40, 36), ((40, 40), (39, 44), (36, 44)))
        self.add_contour("hair-right-lock", "hair-right", "hair-right-curl")
        self.relate("connect", "brim", "hair-left-lock")
        self.relate("connect", "brim", "hair-right-lock")
