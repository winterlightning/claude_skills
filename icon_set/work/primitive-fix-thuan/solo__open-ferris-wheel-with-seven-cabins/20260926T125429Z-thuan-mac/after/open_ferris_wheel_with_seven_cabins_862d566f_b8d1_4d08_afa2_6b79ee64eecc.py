"""Open Ferris wheel with cabins on an A-frame.

SOLO48 VRECT_L: visible (6, 2)-(42, 46), centerline (8, 4)-(40, 44).

Symbol plan: wheel centre C=(24,20), symmetric about x=24. Three cabins
(r3 rings) sit on the rim at north, east and west, 13 from C; the rim is
drawn as arcs strung between the cabins' cardinal points, so the cabins read
as circles threaded on the wheel like the reference. Spokes run from the hub
to the three cabins; the A-frame legs (slope 1:2) leave the hub, pass the rim
at (18,32)/(30,32) where the lower rim is split, and stand on the base line.
Reduction: seven cabins reduced to the three that stay 8 apart at 48; the
four lower cabins would collide with the A-frame legs.
Construction reference: Lucide `ferris-wheel` (hub, spokes, rim, A-frame
legs to a base line), re-authored on the SOLO48 grid.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '862d566f-b8d1-4d08-afa2-6b79ee64eecc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__open-ferris-wheel-with-seven-cabins/20260926T125429Z-thuan-mac/reference/amusement park ferris wheel_862d566f-b8d1-4d08-afa2-6b79ee64eecc.svg'
AUTHOR = 'claude-opus-5-5'

CX, CY = 24, 20
REACH = 13        # hub to cabin centre
CAB_R = 3
RIM_R = 13
BASE_Y = 44


class Drawing(Solo48):
    icon_id = 'open-ferris-wheel-with-seven-cabins'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('ferris wheel', 'big wheel')
    keywords = ('open', 'ferris', 'wheel', 'with', 'seven', 'cabins', 'amusement', 'park', 'fair', 'ride')

    def ring(self, name, c):
        cx, cy = c
        r = CAB_R
        pts = [(cx + r, cy), (cx, cy + r), (cx - r, cy), (cx, cy - r)]
        ids = []
        for i in range(4):
            self.add_arc(f'{name}-{i}', pts[i], pts[(i + 1) % 4], radius_x=r, sweep=True)
            ids.append(f'{name}-{i}')
        self.add_contour(name, *ids, closed=True)
        # arc ids by the cardinal point they start at: 0=E 1=S 2=W 3=N
        return {'E': (f'{name}-0', f'{name}-3', pts[0]), 'S': (f'{name}-1', f'{name}-0', pts[1]),
                'W': (f'{name}-2', f'{name}-1', pts[2]), 'N': (f'{name}-3', f'{name}-2', pts[3])}

    def join(self, part, *cardinal):
        for arc_id in cardinal[:2]:
            self.relate('connect', part, arc_id)

    def build(self):
        north = self.ring('cabin-top', (CX, CY - REACH))
        east = self.ring('cabin-right', (CX + REACH, CY))
        west = self.ring('cabin-left', (CX - REACH, CY))
        leg_l, leg_r = (18, 32), (30, 32)
        # upper rim
        self.add_arc('rim-upper-right', north['E'][2], east['N'][2], radius_x=RIM_R, sweep=True)
        self.add_arc('rim-upper-left', west['N'][2], north['W'][2], radius_x=RIM_R, sweep=True)
        self.join('rim-upper-right', *north['E']); self.join('rim-upper-right', *east['N'])
        self.join('rim-upper-left', *west['N']); self.join('rim-upper-left', *north['W'])
        # lower rim, split where the legs pass
        self.add_arc('rim-lower-right', east['S'][2], leg_r, radius_x=RIM_R, sweep=True)
        self.add_arc('rim-lower-mid', leg_r, leg_l, radius_x=RIM_R, sweep=True)
        self.add_arc('rim-lower-left', leg_l, west['S'][2], radius_x=RIM_R, sweep=True)
        self.add_contour('rim-lower', 'rim-lower-right', 'rim-lower-mid', 'rim-lower-left')
        self.join('rim-lower-right', *east['S']); self.join('rim-lower-left', *west['S'])
        # spokes
        hub = (CX, CY)
        self.add_line('spoke-top', hub, north['S'][2])
        self.add_line('spoke-right', hub, east['W'][2])
        self.add_line('spoke-left', hub, west['E'][2])
        self.join('spoke-top', *north['S']); self.join('spoke-right', *east['W']); self.join('spoke-left', *west['E'])
        # A-frame legs through the rim to the base
        self.add_line('leg-left-in', hub, leg_l)
        self.add_line('leg-left-out', leg_l, (12, BASE_Y))
        self.add_contour('leg-left', 'leg-left-in', 'leg-left-out')
        self.add_line('leg-right-in', hub, leg_r)
        self.add_line('leg-right-out', leg_r, (36, BASE_Y))
        self.add_contour('leg-right', 'leg-right-in', 'leg-right-out')
        for spoke in ('spoke-top', 'spoke-right', 'spoke-left', 'leg-left-in', 'leg-right-in'):
            for other in ('spoke-top', 'spoke-right', 'spoke-left', 'leg-left-in', 'leg-right-in'):
                if spoke < other:
                    self.relate('connect', spoke, other)
        for leg, side in (('leg-left', 'left'), ('leg-right', 'right')):
            self.relate('connect', f'{leg}-in', 'rim-lower-mid')
            self.relate('connect', f'{leg}-out', 'rim-lower-mid')
            self.relate('connect', f'{leg}-in', f'rim-lower-{side}')
            self.relate('connect', f'{leg}-out', f'rim-lower-{side}')
        # base
        self.add_polyline('base', (8, BASE_Y), (12, BASE_Y), (36, BASE_Y), (40, BASE_Y))
        self.relate('connect', 'leg-left-out', 'base-1'); self.relate('connect', 'leg-left-out', 'base-2')
        self.relate('connect', 'leg-right-out', 'base-2'); self.relate('connect', 'leg-right-out', 'base-3')
