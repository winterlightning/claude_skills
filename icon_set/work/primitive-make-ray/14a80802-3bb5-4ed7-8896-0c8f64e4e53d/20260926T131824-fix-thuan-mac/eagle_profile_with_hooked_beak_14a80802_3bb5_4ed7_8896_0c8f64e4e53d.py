"""Eagle profile with hooked beak and a folded wing.

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: the eagle faces right. A straight back rises from the base
corner (6,42) to (12,24), then the head curves over to the crown line y=6;
the beak runs along the crown and hooks down with an r8 quarter arc to the
tip (42,20), returning up-left to the gape (34,16). The throat and chest fall
from the gape in an S-curve to the base. The folded wing (review feedback)
springs from the back at (12,24), sweeps right and down inside the body and
closes against the base line, 9 clear of the chest. A dot eye sits 9 from
the crown line and the gape.
Revision: the wing curve inside the body was missing; it is now drawn.
Deliberate asymmetry: a profile subject.
Construction reference: no useful local Lucide eagle; `bird` checked for the
back-to-head curve only.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '14a80802-3bb5-4ed7-8896-0c8f64e4e53d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__eagle-profile-with-hooked-beak/20260926T125429Z-thuan-mac/reference/eagle_14a80802-3bb5-4ed7-8896-0c8f64e4e53d.svg'
AUTHOR = "claude-opus-5-5"

BASE_L = (6, 42)
NAPE = (12, 24)        # where the wing leaves the back
CROWN = (26, 6)
HOOK_START = (34, 6)
HOOK_R = 8
TIP = (42, 20)
GAPE = (34, 16)
WING_END = (21, 42)
CHEST_END = (30, 42)


class BatchIcon(Solo48):
    icon_id = 'eagle-profile-with-hooked-beak'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('eagle head', 'raptor')
    keywords = ('eagle', 'bird', 'beak', 'wing', 'raptor', 'animal', 'profile')

    def build(self):
        hook_end = (HOOK_START[0] + HOOK_R, HOOK_START[1] + HOOK_R)      # (42, 14)
        self.add_line('back', BASE_L, NAPE)
        self.add_bezier('head', NAPE, ((13, 12), (18, 6), CROWN))
        self.add_line('beak-top', CROWN, HOOK_START)
        self.add_arc('beak-hook', HOOK_START, hook_end, radius_x=HOOK_R, sweep=True)
        self.add_line('beak-tip', hook_end, TIP)
        self.add_line('beak-lower', TIP, GAPE)
        self.add_bezier('chest', GAPE, ((30, 21), (30, 26), (34, 31)), ((38, 36), (36, 42), CHEST_END))
        self.add_contour('outline', 'back', 'head', 'beak-top', 'beak-hook', 'beak-tip', 'beak-lower', 'chest')
        self.add_bezier('wing', NAPE, ((22, 22), (27, 33), WING_END))
        self.add_line('base', WING_END, BASE_L)
        self.add_contour('wing-shape', 'wing', 'base')
        self.relate('connect', 'wing', 'back')
        self.relate('connect', 'wing', 'head')
        self.relate('connect', 'base', 'back')
        self.add_dot('eye', (24, 15))
