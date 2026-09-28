"""A magnifying glass examining a two-tone capsule pill.

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: the lens is a r15 ring about (21,21) reaching the left and top
edges, split at the 3-4-5 node (30,33) where the handle leaves it for the
bottom-right corner (42,42) along (4,3). Inside, a capsule centred on the
lens: two r4 cap arcs about (19,21) and (23,21) joined by straight sides,
with a divider line across its middle so it reads as a two-part pill; its
farthest point is 6 from the lens centre, 9 clear of the rim.
Revision: the rejected drawing's tiny rounded square did not read as a pill;
the capsule is now long with a centre divider.
Construction reference: Lucide `search` (lens and handle) and `pill`.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '15fc1905-26f1-420c-9167-f58df5f29604'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__magnifying-glass-pill/20260926T160211Z-thuan-mac-1/reference/magnifying glass pill_15fc1905-26f1-420c-9167-f58df5f29604.svg'
AUTHOR = 'claude-opus-5-5'

LENS, LENS_R = (21, 21), 15
HANDLE_ROOT, HANDLE_END = (30, 33), (42, 42)   # LENS + (9, 12); handle along (4, 3)
CAP_L, CAP_R, CAP_RAD = (19, 21), (23, 21), 4


class Drawing(Solo48):
    icon_id = 'magnifying-glass-pill'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('drug search', 'medicine lookup')
    keywords = ('magnifying glass', 'pill', 'capsule', 'medicine', 'drug', 'search', 'pharmacy')

    def build(self):
        cx, cy = LENS
        east, south, west, north = (cx + LENS_R, cy), (cx, cy + LENS_R), (cx - LENS_R, cy), (cx, cy - LENS_R)
        self.add_arc('lens-a', east, HANDLE_ROOT, radius_x=LENS_R, sweep=True)
        self.add_arc('lens-b', HANDLE_ROOT, south, radius_x=LENS_R, sweep=True)
        self.add_arc('lens-c', south, west, radius_x=LENS_R, sweep=True)
        self.add_arc('lens-d', west, north, radius_x=LENS_R, sweep=True)
        self.add_arc('lens-e', north, east, radius_x=LENS_R, sweep=True)
        self.add_contour('lens', 'lens-a', 'lens-b', 'lens-c', 'lens-d', 'lens-e', closed=True)
        self.add_line('handle', HANDLE_ROOT, HANDLE_END)
        self.relate('connect', 'handle', 'lens')
        (lx, ly), (rx, ry), r = CAP_L, CAP_R, CAP_RAD
        top_l, top_r, bot_r, bot_l = (lx, ly - r), (rx, ry - r), (rx, ry + r), (lx, ly + r)
        mid_top, mid_bot = ((lx + rx) // 2, ly - r), ((lx + rx) // 2, ly + r)
        self.add_line('pill-top-l', top_l, mid_top)
        self.add_line('pill-top-r', mid_top, top_r)
        self.add_arc('pill-cap-r', top_r, bot_r, radius_x=r, sweep=True)
        self.add_line('pill-bottom-r', bot_r, mid_bot)
        self.add_line('pill-bottom-l', mid_bot, bot_l)
        self.add_arc('pill-cap-l', bot_l, top_l, radius_x=r, sweep=True)
        self.add_contour('pill', 'pill-top-l', 'pill-top-r', 'pill-cap-r', 'pill-bottom-r', 'pill-bottom-l', 'pill-cap-l', closed=True)
        self.add_line('pill-divider', mid_top, mid_bot)
        self.relate('connect', 'pill-divider', 'pill')
