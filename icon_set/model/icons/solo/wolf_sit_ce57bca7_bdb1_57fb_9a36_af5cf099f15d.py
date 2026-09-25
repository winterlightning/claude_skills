"""Sitting wolf with upright foreleg and curled tail. One ear and near foreleg replace overlapping detail; asymmetric profile follows the source."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce57bca7-bdb1-57fb-9a36-af5cf099f15d'
SOURCE_PATH = 'pictographic-primitives/animals/wolf sit_ce57bca7-bdb1-57fb-9a36-af5cf099f15d.svg'
AUTHOR = 'gpt-6'


class SittingWolf(Solo48):
    icon_id = 'sitting-wolf'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('wolf', 'sitting', 'tail', 'profile', 'canine', 'dog', 'wild', 'guard')

    def build(self) -> None:
        self.add_line('head-1', (6, 6), (13, 8))
        self.add_line('head-2', (13, 8), (21, 9))
        self.add_line('head-3', (21, 9), (29, 13))
        self.add_arc('nose', (29, 13), (22, 19), radius_x=7, radius_y=7, sweep=True)
        self.add_line('jaw', (22, 19), (18, 20))
        self.add_arc('chest', (18, 20), (30, 32), radius_x=25, radius_y=25, sweep=False)
        self.add_arc('haunch', (30, 32), (29, 42), radius_x=10, radius_y=10, sweep=True)
        self.add_line('ground', (29, 42), (10, 42))
        self.add_line('foreleg', (10, 42), (10, 35))
        self.add_bezier('back', (10, 35), *(((7.30664765, 28.67898379), (6, 21.87068894), (6, 15)),))
        self.add_line('ear-back', (6, 15), (6, 6))
        self.add_contour('outline', 'head-1', 'head-2', 'head-3', 'nose', 'jaw', 'chest', 'haunch', 'ground', 'foreleg', 'back', 'ear-back', closed=True)
        self.add_bezier('tail-top',(30,32),((34,28),(34,23),(34,20)))
        self.add_bezier('tail-tip',(34,20),((39,20),(42,25),(42,31)))
        self.add_arc('tail-bottom', (42, 31), (29, 42), radius_x=14, radius_y=15, sweep=True)
        self.add_contour('tail', 'tail-top', 'tail-tip', 'tail-bottom', closed=False)
        self.relate("connect", 'outline', 'tail')
