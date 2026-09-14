"""Surfer on Board. Crouching surfer extends arms for balance on a right-sloping board; retain upward-curling left tip.
Keyshape HRECT_L, visible extremes (2, 6, 46, 42); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '07b26145-f859-446a-aa54-ec18b20ca4a5'
SOURCE_PATH = 'pictographic-primitives/recreation/nautic sports surfing water_07b26145-f859-446a-aa54-ec18b20ca4a5.svg'
AUTHOR = 'gpt-6'


class SurferOnBoard(Solo48):
    icon_id = 'surfer-on-board'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('surfer', 'on', 'board')

    def build(self) -> None:
        self.add_arc('head-top', (25, 11), (31, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (31, 11), (25, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('arms-1', (10, 14), (16, 20))
        self.add_line('arms-2', (16, 20), (25, 22))
        self.add_line('arms-3', (25, 22), (38, 28))
        self.add_contour('arms', 'arms-1', 'arms-2', 'arms-3', closed=False)
        self.add_line('body-1', (25, 22), (20, 29))
        self.add_line('body-2', (20, 29), (28, 34))
        self.add_line('body-3', (28, 34), (27, 38))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', closed=False)
        self.relate("connect", 'arms', 'body')
        self.add_line('rear-leg-1', (20, 29), (14, 34))
        self.add_line('rear-leg-2', (14, 34), (10, 36))
        self.add_contour('rear-leg', 'rear-leg-1', 'rear-leg-2', closed=False)
        self.relate("connect", 'rear-leg', 'body')
        self.add_arc('board-tip', (4, 29), (10, 36), radius_x=9, radius_y=9, sweep=True)
        self.add_line('board-1', (10, 36), (27, 38))
        self.add_line('board-2', (27, 38), (44, 40))
        self.add_contour('surfboard', 'board-tip', 'board-1', 'board-2', closed=False)
        self.relate("connect", 'surfboard', 'rear-leg')
        self.relate("connect", 'surfboard', 'body')
