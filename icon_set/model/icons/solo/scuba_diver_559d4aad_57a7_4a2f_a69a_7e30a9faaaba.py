"""Scuba Diver. Right-swimming diver with bent legs and an attached back tank; surface reduced to one line and lower waves omitted.
Keyshape HRECT_L, visible extremes (2, 6, 46, 42); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '559d4aad-57a7-4a2f-a69a-7e30a9faaaba'
SOURCE_PATH = 'pictographic-primitives/recreation/diving diver_559d4aad-57a7-4a2f-a69a-7e30a9faaaba.svg'
AUTHOR = 'gpt-6'


class ScubaDiver(Solo48):
    icon_id = 'scuba-diver'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('scuba', 'diver')

    def build(self) -> None:
        self.add_arc('head-top', (35, 21), (43, 21), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('head-bottom', (43, 21), (35, 21), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('body-1', (4, 19), (10, 19))
        self.add_line('body-2', (10, 19), (17, 31))
        self.add_line('body-3', (17, 31), (29, 31))
        self.add_line('body-4', (29, 31), (38, 40))
        self.add_line('body-5', (38, 40), (44, 40))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', closed=False)
        self.add_line('tank-1', (17, 31), (17, 18))
        self.add_line('tank-2', (17, 18), (25, 18))
        self.add_line('tank-3', (25, 18), (25, 31))
        self.add_line('tank-4', (25, 31), (17, 31))
        self.add_contour('tank', 'tank-1', 'tank-2', 'tank-3', 'tank-4', closed=True)
        self.relate("connect", 'tank', 'body')
        self.add_line('surface', (4, 8), (44, 8))
