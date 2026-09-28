"""A power cable coiled into a loop, its plug at the top.

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: the cable is three quarter arcs of a r15 circle about (21,27),
from its top node (21,12) round the left and the bottom to the free end at
the east node (36,27), leaving an open quarter at the top right. At the top
node the cable runs tangentially into the plug: a D-shaped body (a r6 left
cap about (27,12), flat back at x=32) with two prongs leaving the back 2
inside its corners (8 apart) and running to x=42.
Revision: the rejected drawing gave a short C of cable under an oversized
plug and read as a letter; the cable now coils three quarters of the way
round and the plug is a small head on it.
Construction reference: Lucide `plug` (body with two prongs) and `cable`.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '79eae0ea-a0a3-48d0-a56a-a874914d50c3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__looped-power-cable-79eae0ea-solo/20260926T160211Z-thuan-mac-1/reference/circle cable_79eae0ea-a0a3-48d0-a56a-a874914d50c3.svg'
AUTHOR = "claude-opus-5-5"

LOOP, LOOP_R = (21, 27), 15
CAP, CAP_R, BACK_X, PRONG_END = (27, 12), 6, 32, 42
PRONG_INSET = 2


class Drawing(Solo48):
    icon_id = 'looped-power-cable-79eae0ea-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('circle cable', 'coiled power cord')
    keywords = ('cable', 'power', 'plug', 'cord', 'electric', 'charger', 'loop', 'wire')

    def build(self):
        cx, cy = LOOP
        top, west, south, east = (cx, cy - LOOP_R), (cx - LOOP_R, cy), (cx, cy + LOOP_R), (cx + LOOP_R, cy)
        self.add_arc('cable-a', east, south, radius_x=LOOP_R, sweep=True)
        self.add_arc('cable-b', south, west, radius_x=LOOP_R, sweep=True)
        self.add_arc('cable-c', west, top, radius_x=LOOP_R, sweep=True)
        px, py = CAP
        cap_top, cap_bot = (px, py - CAP_R), (px, py + CAP_R)
        self.add_arc('plug-cap-upper', top, cap_top, radius_x=CAP_R, sweep=True)
        self.add_line('plug-top', cap_top, (BACK_X, py - CAP_R))
        self.add_line('plug-bottom', (BACK_X, py + CAP_R), cap_bot)
        self.add_arc('plug-cap-lower', cap_bot, top, radius_x=CAP_R, sweep=True)
        self.add_line('plug-back', (BACK_X, py - CAP_R), (BACK_X, py - CAP_R + PRONG_INSET))
        self.add_line('plug-back-mid', (BACK_X, py - CAP_R + PRONG_INSET), (BACK_X, py + CAP_R - PRONG_INSET))
        self.add_line('plug-back-low', (BACK_X, py + CAP_R - PRONG_INSET), (BACK_X, py + CAP_R))
        self.add_line('prong-top', (BACK_X, py - CAP_R + PRONG_INSET), (PRONG_END, py - CAP_R + PRONG_INSET))
        self.add_line('prong-bottom', (BACK_X, py + CAP_R - PRONG_INSET), (PRONG_END, py + CAP_R - PRONG_INSET))
        self.add_contour('plug', 'plug-cap-upper', 'plug-top', 'plug-back', 'plug-back-mid', 'plug-back-low', 'plug-bottom', 'plug-cap-lower', closed=True)
        self.add_contour('cable', 'cable-a', 'cable-b', 'cable-c')
        self.relate('connect', 'cable', 'plug')
        self.relate('connect', 'prong-top', 'plug')
        self.relate('connect', 'prong-bottom', 'plug')
