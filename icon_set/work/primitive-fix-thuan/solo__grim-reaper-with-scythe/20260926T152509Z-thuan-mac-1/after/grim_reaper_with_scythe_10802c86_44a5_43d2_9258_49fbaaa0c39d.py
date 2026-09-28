"""The grim reaper: a hooded, cloaked figure holding a long scythe.

SOLO48 VRECT_L: visible (6, 2)-(42, 46), centerline (8, 4)-(40, 44).

Symbol plan: the scythe dominates: a straight handle at x=40 and a long
blade that is one r20 arc about (28,24), from the handle top (40,8) over
its apex (28,4) down to the tip (12,12) (12-16-20 offsets, so every node is
an integer). The figure stands under the blade tip: a round hood (r8 arc)
over a cloak that flares to a flat hem, with one arm reaching straight out
to grip the handle.
Revision: the rejected drawing gave a house outline with a ring and read as
a building; the reaper is now a hooded cloak with the scythe blade sweeping
over it.
Construction reference: no useful Lucide match (`ghost` checked for the
hood-and-cloak silhouette).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '10802c86-44a5-43d2-9258-49fbaaa0c39d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__grim-reaper-with-scythe/20260926T152509Z-thuan-mac-1/reference/grim reaper_10802c86-44a5-43d2-9258-49fbaaa0c39d.svg'
AUTHOR = 'claude-opus-5-5'

HANDLE_X, HANDLE_TOP, GROUND = 40, 8, 44
BLADE_APEX, BLADE_TIP, BLADE_R = (28, 4), (12, 12), 20
HOOD_L, HOOD_R, HOOD_RAD = (10, 30), (26, 30), 8
HEM_L, HEM_R = (8, 44), (28, 44)
SHOULDER = (27, 34)       # on the right cloak edge; the arm leaves here
GRIP = (HANDLE_X, SHOULDER[1])


class Drawing(Solo48):
    icon_id = 'grim-reaper-with-scythe'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('grim reaper', 'death')
    keywords = ('grim reaper', 'death', 'scythe', 'halloween', 'hood', 'cloak', 'spooky')

    def build(self):
        self.add_line('handle', (HANDLE_X, GROUND), GRIP)
        self.add_line('handle-upper', GRIP, (HANDLE_X, HANDLE_TOP))
        self.add_arc('blade-right', (HANDLE_X, HANDLE_TOP), BLADE_APEX, radius_x=BLADE_R, sweep=False)
        self.add_arc('blade-left', BLADE_APEX, BLADE_TIP, radius_x=BLADE_R, sweep=False)
        self.add_contour('scythe', 'handle', 'handle-upper', 'blade-right', 'blade-left')
        self.add_arc('hood', HOOD_L, HOOD_R, radius_x=HOOD_RAD, sweep=True)
        self.add_line('cloak-right-a', HOOD_R, SHOULDER)
        self.add_line('cloak-right-b', SHOULDER, HEM_R)
        self.add_line('hem', HEM_R, HEM_L)
        self.add_line('cloak-left', HEM_L, HOOD_L)
        self.add_contour('cloak', 'hood', 'cloak-right-a', 'cloak-right-b', 'hem', 'cloak-left', closed=True)
        self.add_line('arm', SHOULDER, GRIP)
        self.relate('connect', 'arm', 'cloak')
        self.relate('connect', 'arm', 'scythe')
