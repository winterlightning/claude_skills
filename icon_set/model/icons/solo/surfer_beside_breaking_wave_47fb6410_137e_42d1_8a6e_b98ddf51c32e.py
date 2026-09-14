"""Surfer Beside Breaking Wave. Surfer balances on a sloping board beside a tall breaking wave; retain one bent leg and simplify the smaller waves to one joined baseline.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47fb6410-137e-42d1-8a6e-b98ddf51c32e'
SOURCE_PATH = 'pictographic-primitives/recreation/surfing_47fb6410-137e-42d1-8a6e-b98ddf51c32e.svg'
AUTHOR = 'gpt-6'


class SurferBesideBreakingWave(Solo48):
    icon_id = 'surfer-beside-breaking-wave'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('surfer', 'beside', 'breaking', 'wave')

    def build(self) -> None:
        self.add_arc('head-top', (14, 9), (20, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (20, 9), (14, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('arms-1', (6, 20), (17, 22))
        self.add_line('arms-2', (17, 22), (27, 25))
        self.add_contour('arms', 'arms-1', 'arms-2', closed=False)
        self.add_line('body-1', (17, 22), (13, 27))
        self.add_line('body-2', (13, 27), (20, 31))
        self.add_contour('body', 'body-1', 'body-2', closed=False)
        self.relate("connect", 'arms', 'body')
        self.add_line('board-1', (6, 29), (20, 31))
        self.add_line('board-2', (20, 31), (29, 33))
        self.add_contour('board', 'board-1', 'board-2', closed=False)
        self.relate("connect", 'board', 'body')
        self.add_arc('wave-crest', (32, 6), (40, 20), radius_x=8, radius_y=14, sweep=True)
        self.add_line('wave-wall', (40, 20), (40, 34))
        self.add_arc('wave-foot', (40, 34), (42, 42), radius_x=2, radius_y=8, sweep=False)
        self.add_contour('breaking-wave', 'wave-crest', 'wave-wall', 'wave-foot', closed=False)
        self.add_line('water', (6, 42), (42, 42))
        self.relate("connect", 'water', 'breaking-wave')
