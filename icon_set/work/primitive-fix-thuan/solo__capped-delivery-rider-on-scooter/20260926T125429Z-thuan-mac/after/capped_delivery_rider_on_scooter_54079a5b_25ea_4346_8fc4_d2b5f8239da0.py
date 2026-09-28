"""Capped delivery rider on a scooter, with a parcel box on the rear seat.

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: two r3 wheels (exempt 6-diameter rings) at (11,39) and (39,39);
the floor line y=36 rests on both wheel tops, and the steering column rises
from the front wheel top to the handlebar (36,18). The seat line y=28 runs
from the rear to the rider's hip; the parcel box (10 x 8) stands on its rear
half. The rider (shared human reference, full_body_ref.png: round outlined
head, round-ended limbs) sits at the hip (24,28): vertical torso to the neck
(24,20), head r3 at (24,9) so the detached head gap is exactly 8 on
centerlines / 4 ink, arm from the chest (24,22) to the handlebar, thigh to
the knee (29,31) and shin down to the floor. A cap brim juts forward from the
head's front point.
Revision: the earlier drawing scattered a head, a parcel and a bent pipe over
a skateboard-like frame; the seated figure with arm on the handlebar, the
steering column and the parcel on the seat now read as a delivery rider.
Omissions: scooter side panels, headlamp and wheel hubs.
Construction: human_ref/full_body_ref.png for the figure; Lucide `bike`
(two wheels, frame between them) for the vehicle.
Deliberate asymmetry: a side-view vehicle.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '54079a5b-25ea-4346-8fc4-d2b5f8239da0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__capped-delivery-rider-on-scooter/20260926T125429Z-thuan-mac/reference/delivery person motorcycle_54079a5b-25ea-4346-8fc4-d2b5f8239da0.svg'
AUTHOR = 'claude-opus-5-5'

WHEEL_R = 3
REAR_C, FRONT_C = (11, 39), (39, 39)
FLOOR_Y = 36            # resting on the wheel tops
SEAT_Y = 28
BOX = (6, 20, 16)          # left, top, right; bottom is the seat
HIP = (24, SEAT_Y)
NECK = (24, 20)
CHEST = (24, 22)
HEAD_C, HEAD_R = (24, 9), 3
KNEE = (29, 31)
FOOT = (29, FLOOR_Y)
BAR = (36, 18)
BRIM = 4


class Drawing(Solo48):
    icon_id = 'capped-delivery-rider-on-scooter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('food delivery', 'courier scooter')
    keywords = ('capped', 'delivery', 'rider', 'on', 'scooter', 'courier', 'parcel', 'motorcycle')

    def ring(self, name, c, r):
        cx, cy = c
        pts = [(cx + r, cy), (cx, cy + r), (cx - r, cy), (cx, cy - r)]
        for i in range(4):
            self.add_arc(f'{name}-{i}', pts[i], pts[(i + 1) % 4], radius_x=r, sweep=True)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)
        return pts

    def build(self):
        rear = self.ring('wheel-rear', REAR_C, WHEEL_R)
        front = self.ring('wheel-front', FRONT_C, WHEEL_R)
        # floor resting on both wheel tops, split where the foot rests
        self.add_line('floor-rear', rear[3], FOOT)
        self.add_line('floor-front', FOOT, front[3])
        self.add_contour('floor', 'floor-rear', 'floor-front')
        self.relate('connect', 'floor-rear', 'wheel-rear-2'); self.relate('connect', 'floor-rear', 'wheel-rear-3')
        self.relate('connect', 'floor-front', 'wheel-front-2'); self.relate('connect', 'floor-front', 'wheel-front-3')
        # steering column from the front wheel top
        self.add_line('column', front[3], BAR)
        self.relate('connect', 'column', 'floor-front')
        self.relate('connect', 'column', 'wheel-front-2'); self.relate('connect', 'column', 'wheel-front-3')
        # seat and parcel box
        l, t, r = BOX
        self.add_line('seat-rear', (r, SEAT_Y), (l, SEAT_Y))
        self.add_line('seat-front', (r, SEAT_Y), HIP)
        self.add_line('box-back', (l, SEAT_Y), (l, t))
        self.add_line('box-top', (l, t), (r, t))
        self.add_line('box-front', (r, t), (r, SEAT_Y))
        self.add_contour('parcel', 'seat-rear', 'box-back', 'box-top', 'box-front', closed=True)
        self.relate('connect', 'seat-front', 'seat-rear')
        self.relate('connect', 'seat-front', 'box-front')
        # rider
        self.add_line('torso-lower', HIP, CHEST)
        self.add_line('torso', CHEST, NECK)
        self.add_contour('body', 'torso-lower', 'torso')
        self.ring('head', HEAD_C, HEAD_R)
        self.mark_human_figure('rider', head='head', torso='torso', torso_junction='end')
        self.add_line('arm', CHEST, BAR)
        self.relate('connect', 'arm', 'torso-lower'); self.relate('connect', 'arm', 'torso')
        self.relate('connect', 'arm', 'column')
        self.add_line('thigh', HIP, KNEE)
        self.add_line('shin', KNEE, FOOT)
        self.add_contour('leg', 'thigh', 'shin')
        self.relate('connect', 'thigh', 'torso-lower')
        self.relate('connect', 'thigh', 'seat-front'); self.relate('connect', 'torso-lower', 'seat-front')
        self.relate('connect', 'shin', 'floor-rear'); self.relate('connect', 'shin', 'floor-front')
        # cap brim from the head's front point
        front = (HEAD_C[0] + HEAD_R, HEAD_C[1])
        self.add_line('cap-brim', front, (front[0] + BRIM, front[1]))
        self.relate('connect', 'cap-brim', 'head-0'); self.relate('connect', 'cap-brim', 'head-3')
