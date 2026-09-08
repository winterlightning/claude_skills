"""Sitting wolf with upright foreleg and curled tail. One ear and near foreleg replace overlapping detail; asymmetric profile follows the source."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce57bca7-bdb1-57fb-9a36-af5cf099f15d'
SOURCE_PATH = 'pictographic-primitives/animals/wolf sit_ce57bca7-bdb1-57fb-9a36-af5cf099f15d.svg'
AUTHOR = 'gpt-6'


class SittingWolf(Solo48):
    icon_id = 'sitting-wolf'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('wolf', 'sitting', 'tail', 'profile', 'canine', 'dog', 'wild', 'guard')

    def build(self) -> None:
        self.add_line('head-1', (5, 2), (13, 8))
        self.add_line('head-2', (13, 8), (21, 9))
        self.add_line('head-3', (21, 9), (29, 13))
        self.add_arc('nose', (29, 13), (22, 19), radius_x=7, radius_y=7, sweep=True)
        self.add_line('jaw', (22, 19), (18, 20))
        self.add_arc('chest', (18, 20), (30, 32), radius_x=25, radius_y=25, sweep=False)
        self.add_arc('haunch', (30, 32), (29, 46), radius_x=10, radius_y=10, sweep=True)
        self.add_line('ground', (29, 46), (10, 46))
        self.add_line('foreleg', (10, 46), (10, 35))
        self.add_arc('back', (10, 35), (5, 15), radius_x=50, radius_y=50, sweep=True)
        self.add_line('ear-back', (5, 15), (5, 2))
        self.add_contour('outline', 'head-1', 'head-2', 'head-3', 'nose', 'jaw', 'chest', 'haunch', 'ground', 'foreleg', 'back', 'ear-back', closed=True)
        self.add_arc('tail-top', (30, 32), (39, 20), radius_x=13, radius_y=13, sweep=False)
        self.add_arc('tail-tip', (39, 20), (43, 31), radius_x=4, radius_y=11, sweep=True)
        self.add_arc('tail-bottom', (43, 31), (29, 46), radius_x=14, radius_y=15, sweep=True)
        self.add_contour('tail', 'tail-top', 'tail-tip', 'tail-bottom', closed=False)
        self.relate("connect", 'outline', 'tail')
