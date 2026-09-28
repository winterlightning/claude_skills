"""A brass bugle: mouthpiece, straight lead pipe, flared bell and a coil of tubing.

SOLO48 HRECT_L: visible (2, 6)-(46, 42), centerline (4, 8)-(44, 40).

Symbol plan: the lead pipe runs along y=14 from the mouthpiece cup (a short
upright at x=4) to the bell's throat at (26,14). The bell is a cone from the
throat to a rim at x=44 spanning y=8..24 (inradius about 5). The coiled
tubing is a stadium loop (r8 caps about (16,32) and (22,32)) hanging under
the pipe on a short drop from (16,14), its top 10 below the pipe.
Revision: the rejected drawing's blocky bell and loop read as a hair dryer;
the mouthpiece, straight lead pipe, open bell with rim and a separate coil
now read as a bugle.
Construction reference: no useful Lucide match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1c3b1dee-2c1a-4e89-91de-95172d2201db'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__looped-brass-bugle/20260926T160211Z-thuan-mac-1/reference/brass_1c3b1dee-2c1a-4e89-91de-95172d2201db.svg'
AUTHOR = 'claude-opus-5-5'

PIPE_Y, CUP_X, CUP_HALF, THROAT_X = 16, 4, 4, 26
RIM_X, RIM_TOP, RIM_BOTTOM = 44, 8, 24
FLARE_R = 20
DROP_X = 16
COIL_L, COIL_R, COIL_RAD = (16, 32), (22, 32), 8


class Drawing(Solo48):
    icon_id = 'looped-brass-bugle'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('brass', 'bugle')
    keywords = ('bugle', 'brass', 'horn', 'trumpet', 'music', 'instrument', 'military', 'fanfare')

    def build(self):
        self.add_line('cup-top', (CUP_X, PIPE_Y - CUP_HALF), (CUP_X, PIPE_Y))
        self.add_line('cup-bottom', (CUP_X, PIPE_Y), (CUP_X, PIPE_Y + CUP_HALF))
        self.add_line('pipe-a', (CUP_X, PIPE_Y), (DROP_X, PIPE_Y))
        self.add_line('pipe-b', (DROP_X, PIPE_Y), (THROAT_X, PIPE_Y))
        self.add_contour('pipe', 'pipe-a', 'pipe-b')
        self.relate('connect', 'pipe', 'cup-top')
        self.relate('connect', 'pipe', 'cup-bottom')
        self.relate('connect', 'cup-top', 'cup-bottom')
        throat = (THROAT_X, PIPE_Y)
        self.add_arc('bell-top', throat, (RIM_X, RIM_TOP), radius_x=FLARE_R, sweep=False)
        self.add_line('bell-rim', (RIM_X, RIM_TOP), (RIM_X, RIM_BOTTOM))
        self.add_arc('bell-bottom', (RIM_X, RIM_BOTTOM), throat, radius_x=FLARE_R, sweep=True)
        self.add_contour('bell', 'bell-top', 'bell-rim', 'bell-bottom', closed=True)
        self.relate('connect', 'bell', 'pipe')
        (lx, ly), (rx, ry), r = COIL_L, COIL_R, COIL_RAD
        self.add_line('coil-top', (rx, ry - r), (lx, ly - r))
        self.add_arc('coil-left', (lx, ly - r), (lx, ly + r), radius_x=r, sweep=False)
        self.add_line('coil-bottom', (lx, ly + r), (rx, ry + r))
        self.add_arc('coil-right', (rx, ry + r), (rx, ry - r), radius_x=r, sweep=False)
        self.add_contour('coil', 'coil-top', 'coil-left', 'coil-bottom', 'coil-right', closed=True)
        self.add_line('drop', (DROP_X, PIPE_Y), (lx, ly - r))
        self.relate('connect', 'drop', 'pipe')
        self.relate('connect', 'drop', 'coil')
