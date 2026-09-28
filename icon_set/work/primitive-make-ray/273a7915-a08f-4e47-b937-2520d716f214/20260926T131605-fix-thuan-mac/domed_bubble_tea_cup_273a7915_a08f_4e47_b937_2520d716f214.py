"""Domed bubble tea cup.

SOLO48 VRECT_L: visible (6, 2)-(42, 46), centerline (8, 4)-(40, 44).

Symbol plan: symmetric about x=24. A tall cup tapers from the lid rim (y=21)
to a flat base (y=44); the rim line overhangs the cup walls by 2 on each side
like the reference's lid lip; a semicircular dome (r10) sits on the rim, and
a slanted straw leaves the dome's right shoulder. Three tapioca pearls are solid dots
in a triangle at the bottom of the cup (8 apart from each other, the walls,
the base and the rim).
Revision: the earlier cup was squat with one ringed pearl and read as a
muffin/bin; the taller cup, overhanging lid lip, straw and pearl cluster now
carry the bubble-tea meaning.
Construction reference: Lucide `cup-soda` (tapered cup, lid band, straw), re-authored.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '273a7915-a08f-4e47-b937-2520d716f214'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__domed-bubble-tea-cup/20260926T125429Z-thuan-mac/reference/bubble tea shake_273a7915-a08f-4e47-b937-2520d716f214.svg'
AUTHOR = 'claude-opus-5-5'

AXIS = 24
RIM_Y = 18
RIM_HALF = 16      # lid lip x 8..40
WALL_TOP = 14      # cup top half-width (x 10..38)
WALL_BOT = 12      # cup base half-width (x 12..36)
BASE_Y = 44
DOME_R = 10


class Drawing(Solo48):
    icon_id = 'domed-bubble-tea-cup'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('boba tea', 'bubble tea')
    keywords = ('domed', 'bubble', 'tea', 'cup', 'boba', 'pearls', 'straw', 'drink')

    def build(self):
        a = AXIS
        # lid lip, split where the dome and the cup walls meet it
        xs = [a - RIM_HALF, a - WALL_TOP, a - DOME_R, a + DOME_R, a + WALL_TOP, a + RIM_HALF]
        for i in range(len(xs) - 1):
            self.add_line(f'rim-{i}', (xs[i], RIM_Y), (xs[i + 1], RIM_Y))
        self.add_contour('rim', *(f'rim-{i}' for i in range(len(xs) - 1)))
        # dome split where the straw leaves it (6-8-10 point right of the crown)
        crown = (a + 6, RIM_Y - 8)
        self.add_arc('dome-left', (a - DOME_R, RIM_Y), crown, radius_x=DOME_R, sweep=True)
        self.add_arc('dome-right', crown, (a + DOME_R, RIM_Y), radius_x=DOME_R, sweep=True)
        self.add_contour('dome', 'dome-left', 'dome-right')
        for arc, seg in (('dome-left', ('rim-1', 'rim-2')), ('dome-right', ('rim-2', 'rim-3'))):
            for s in seg:
                self.relate('connect', arc, s)
        # cup
        self.add_polyline('cup', (a - WALL_TOP, RIM_Y), (a - WALL_BOT, BASE_Y),
                          (a + WALL_BOT, BASE_Y), (a + WALL_TOP, RIM_Y))
        for wall, seg in (('cup-1', ('rim-0', 'rim-1')), ('cup-3', ('rim-3', 'rim-4'))):
            for s in seg:
                self.relate('connect', wall, s)
        # straw
        self.add_line('straw', crown, (a + 10, 4))
        self.relate('connect', 'straw', 'dome-left')
        self.relate('connect', 'straw', 'dome-right')
        # tapioca pearls
        for name, p in (('pearl-left', (a - 4, 36)), ('pearl-right', (a + 4, 36)), ('pearl-top', (a, 28))):
            self.add_dot(name, p)
