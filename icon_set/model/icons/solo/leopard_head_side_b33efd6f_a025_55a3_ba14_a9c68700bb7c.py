"""Right-facing leopard head; pricked ear, angled eye, short muzzle and open neck. Lucide cat informs the coherent skull contour. Whiskers and spots omitted; profile intentionally asymmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b33efd6f-a025-55a3-ba14-a9c68700bb7c'
SOURCE_PATH = 'pictographic-primitives/animals/leopard head side_b33efd6f-a025-55a3-ba14-a9c68700bb7c.svg'
AUTHOR = 'gpt-6'


class LeopardHeadProfile(Solo48):
    icon_id = 'leopard-head-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('leopard', 'head', 'profile', 'animal')

    def build(self) -> None:
        # SQUARE: authored to its exact SOLO48 centerline bounds.
        self.add_line('neck-back', (6, 28), (17, 14))
        self.add_line('ear-back', (17, 14), (20, 6))
        self.add_bezier('ear-tip', (20, 6), *(((21.27525232, 6), (22.72474768, 6), (24, 6)),))
        self.add_arc('ear-front', (24, 6), (26, 11), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('forehead', (26, 11), (38, 20), radius_x=19, radius_y=19, sweep=True)
        self.add_line('snout', (38, 20), (42, 24))
        self.add_line('nose', (42, 24), (42, 30))
        self.add_bezier('muzzle', (42, 30), *(((42, 32.91760715), (40.38747008, 35.71172406), (37, 37)),))
        self.add_arc('jaw', (37, 37), (26, 35), radius_x=16, radius_y=16, sweep=True)
        self.add_arc('chin', (26, 35), (16, 29), radius_x=10, radius_y=6, sweep=True)
        self.add_contour('head', 'neck-back', 'ear-back', 'ear-tip', 'ear-front', 'forehead', 'snout', 'nose', 'muzzle', 'jaw', 'chin', closed=False)
        self.add_arc('neck-front', (26, 35), (18, 42), radius_x=20, radius_y=20, sweep=False)
        self.relate("connect", 'neck-front', 'head')
        self.add_line('eye-1', (28, 23), (31, 24))
        self.add_contour('eye', 'eye-1', closed=False)
