"""Horse Rider. Upright rider on a right-facing horse; retain long muzzle, ear, tail and two visible legs, omit reins and doubled limbs.
Keyshape VRECT_L, visible extremes (6, 2, 42, 46); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bebbb6da-7e2b-58de-b56f-770e3a08a34d'
SOURCE_PATH = 'pictographic-primitives/recreation/outdoors horse_bebbb6da-7e2b-58de-b56f-770e3a08a34d.svg'
AUTHOR = 'gpt-6'


class HorsebackRider(Solo48):
    icon_id = 'horseback-rider'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('horseback', 'rider')

    def build(self) -> None:
        self.add_arc('rider-head-top', (15, 7), (21, 7), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('rider-head-bottom', (21, 7), (15, 7), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('rider-head', 'rider-head-top', 'rider-head-bottom', closed=True)
        self.add_line('rider-1', (18, 19), (18, 28))
        self.add_line('rider-2', (18, 28), (27, 28))
        self.add_contour('rider', 'rider-1', 'rider-2', closed=False)
        self.add_line('arm-1', (18, 19), (26, 22))
        self.add_line('arm-2', (26, 22), (32, 17))
        self.add_contour('arm', 'arm-1', 'arm-2', closed=False)
        self.relate("connect", 'rider', 'arm')
        self.add_line('horse-1', (9, 44), (9, 36))
        self.add_line('horse-2', (9, 36), (9, 30))
        self.add_line('horse-3', (9, 30), (15, 28))
        self.add_line('horse-4', (15, 28), (27, 28))
        self.add_line('horse-5', (27, 28), (32, 17))
        self.add_line('horse-6', (32, 17), (33, 12))
        self.add_line('horse-7', (33, 12), (40, 20))
        self.add_line('horse-8', (40, 20), (40, 25))
        self.add_line('horse-9', (40, 25), (34, 24))
        self.add_line('horse-10', (34, 24), (33, 33))
        self.add_line('horse-11', (33, 33), (33, 36))
        self.add_line('horse-12', (33, 36), (33, 44))
        self.add_contour('horse', 'horse-1', 'horse-2', 'horse-3', 'horse-4', 'horse-5', 'horse-6', 'horse-7', 'horse-8', 'horse-9', 'horse-10', 'horse-11', 'horse-12', closed=False)
        self.relate("connect", 'rider', 'horse')
        self.relate("connect", 'arm', 'horse')
        self.add_line('tail-1', (9, 30), (8, 37))
        self.add_contour('tail', 'tail-1', closed=False)
        self.relate("connect", 'tail', 'horse')
        self.add_line('belly', (9, 36), (33, 36))
        self.relate("connect", 'belly', 'horse')
