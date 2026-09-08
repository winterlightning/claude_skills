"""Standing howling wolf, raised muzzle and dropped tail. Near legs replace overlapping far legs; directional pose is deliberately asymmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '02bbed8d-19bf-42c9-9539-d93fbda86791'
SOURCE_PATH = 'pictographic-primitives/animals/wolf body howl_02bbed8d-19bf-42c9-9539-d93fbda86791.svg'
AUTHOR = 'gpt-6'


class HowlingWolf(Solo48):
    icon_id = 'howling-wolf'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('wolf', 'howl', 'standing', 'moon', 'wild', 'canine', 'night', 'wilderness')

    def build(self) -> None:
        self.add_line('raised-head-1', (29, 16), (33, 9))
        self.add_line('raised-head-2', (33, 9), (37, 8))
        self.add_line('raised-head-3', (37, 8), (46, 2))
        self.add_line('neck', (46, 2), (46, 24))
        self.add_arc('chest', (46, 24), (39, 32), radius_x=7, radius_y=8, sweep=True)
        self.add_line('front-leg-1', (39, 32), (39, 46))
        self.add_line('front-leg-2', (39, 46), (33, 46))
        self.add_line('front-leg-3', (33, 46), (32, 33))
        self.add_arc('belly', (32, 33), (22, 37), radius_x=15, radius_y=15, sweep=True)
        self.add_line('hindleg-1', (22, 37), (18, 41))
        self.add_line('hindleg-2', (18, 41), (18, 46))
        self.add_line('hindleg-3', (18, 46), (12, 46))
        self.add_line('hindleg-4', (12, 46), (12, 34))
        self.add_arc('back', (12, 34), (21, 25), radius_x=9, radius_y=9, sweep=True)
        self.add_arc('shoulders', (21, 25), (32, 16), radius_x=14, radius_y=14, sweep=False)
        self.add_line('muzzle', (32, 16), (29, 16))
        self.add_contour('outline', 'raised-head-1', 'raised-head-2', 'raised-head-3', 'neck', 'chest', 'front-leg-1', 'front-leg-2', 'front-leg-3', 'belly', 'hindleg-1', 'hindleg-2', 'hindleg-3', 'hindleg-4', 'back', 'shoulders', 'muzzle', closed=True)
        self.add_arc('tail-outer', (12, 34), (2, 44), radius_x=10, radius_y=10, sweep=False)
        self.relate("connect", 'outline', 'tail-outer')
