"""Lattice oil pump jack (nodding donkey).

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: an A-frame tower (feet (14,42) and (38,42), apex (26,18)) with a
crossbar brace carries the walking beam at its apex. The beam (slope 2:5)
runs from the horsehead's back at (16,14) down to the right end (41,24). The
horsehead is a quarter-ellipse (10 x 14 about (16,20)) facing left, and the polished
rod hangs from its lower tip straight down to the ground line.
Revision: the earlier drawing boxed everything into one closed frame and lost
the horsehead, the rod and the see-saw beam; these now carry the meaning.
Reduction: the tower lattice is reduced to one crossbar (an X brace leaves
holes below the 6-unit floor); the counterweight box and pitman arm are
omitted because they cannot stay 8 from the tower's right leg.
Construction reference: no useful local Lucide match; supplied reference governs.
Deliberate asymmetry: the beam tilts and the horsehead sits on the left.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4216f978-fc24-48e8-8c36-261313bcdf26'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__lattice-oil-pump-jack/20260926T125429Z-thuan-mac/reference/oil well_4216f978-fc24-48e8-8c36-261313bcdf26.svg'
AUTHOR = "claude-opus-5-5"

GROUND = 42
APEX = (26, 18)
FOOT_L, FOOT_R = (14, GROUND), (38, GROUND)
BAR_Y = 30
HEAD_C, HEAD_RX, HEAD_RY = (16, 20), 10, 14
BEAM_BACK = (16, 14)
BEAM_END = (41, 24)


class Drawing(Solo48):
    icon_id = 'lattice-oil-pump-jack'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("Industrial Oil Pump Jack", "nodding donkey")
    keywords = ("oil", "pump", "jack", "industry", "beam", "energy", "well", "horsehead")

    def build(self):
        hx, hy = HEAD_C
        head_top, head_tip = (hx, hy - HEAD_RY), (hx - HEAD_RX, hy)
        # horsehead: quarter ellipse, back edge split where the beam leaves it
        self.add_arc('head-face', head_tip, head_top, radius_x=HEAD_RX, radius_y=HEAD_RY, sweep=True)
        self.add_line('head-back-upper', head_top, BEAM_BACK)
        self.add_line('head-back-lower', BEAM_BACK, HEAD_C)
        self.add_line('head-bottom', HEAD_C, head_tip)
        self.add_contour('horsehead', 'head-face', 'head-back-upper', 'head-back-lower', 'head-bottom', closed=True)
        # walking beam, split at the pivot
        self.add_line('beam-left', BEAM_BACK, APEX)
        self.add_line('beam-right', APEX, BEAM_END)
        self.add_contour('beam', 'beam-left', 'beam-right')
        self.relate('connect', 'beam-left', 'head-back-upper')
        self.relate('connect', 'beam-left', 'head-back-lower')
        # tower: legs split at the crossbar
        bl = (FOOT_L[0] + (APEX[0] - FOOT_L[0]) * (GROUND - BAR_Y) // (GROUND - APEX[1]), BAR_Y)   # (20, 30)
        br = (2 * APEX[0] - bl[0], BAR_Y)                                                       # (32, 30)
        self.add_polyline('leg-left', FOOT_L, bl, APEX)
        self.add_polyline('leg-right', FOOT_R, br, APEX)
        self.add_line('crossbar', bl, br)
        for leg in ('leg-left', 'leg-right'):
            self.relate('connect', f'{leg}-2', 'beam-left')
            self.relate('connect', f'{leg}-2', 'beam-right')
            self.relate('connect', 'crossbar', f'{leg}-1')
            self.relate('connect', 'crossbar', f'{leg}-2')
        self.relate('connect', 'leg-left-2', 'leg-right-2')
        # polished rod and ground
        self.add_line('rod', head_tip, (head_tip[0], GROUND))
        self.relate('connect', 'rod', 'head-face')
        self.relate('connect', 'rod', 'head-bottom')
        self.add_polyline('ground', (head_tip[0], GROUND), FOOT_L, FOOT_R, (42, GROUND))
        self.relate('connect', 'ground-1', 'rod')
        self.relate('connect', 'ground-1', 'leg-left-1'); self.relate('connect', 'ground-2', 'leg-left-1')
        self.relate('connect', 'ground-2', 'leg-right-1'); self.relate('connect', 'ground-3', 'leg-right-1')
