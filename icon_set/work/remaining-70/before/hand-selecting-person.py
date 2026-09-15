"""A large hand reaches down toward the central head in a group of three people. Its curved thumb and finger frame the larger middle figure, with smaller busts on either side.
Lucide hand-grab rounded finger construction and user heads. One grasping finger and thumb replace individual fingers; central person and side busts retained. Deliberate asymmetric reaching hand.
SQUARE: centerline extremes (6,6)-(42,42); independently authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5607651d-e737-4878-ba6b-f783c322a934'
SOURCE_PATH = 'pictographic-primitives/work/recruiting employee hand pick_5607651d-e737-4878-ba6b-f783c322a934.svg'
AUTHOR = 'gpt-6'


class HandSelectingPerson(Solo48):
    icon_id = 'hand-selecting-person'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('hand', 'person', 'selection', 'recruiting', 'team', 'employee')

    def build(self) -> None:
        self.add_arc('central-head-top', (21, 34), (27, 34), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('central-head-bottom', (27, 34), (21, 34), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('central-head', 'central-head-top', 'central-head-bottom', closed=True)
        self.add_arc('central-left', (14, 42), (24, 37), radius_x=10, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('central-right', (24, 37), (34, 42), radius_x=10, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('central-bust', 'central-left', 'central-right', closed=False)
        self.relate("connect", 'central-head', 'central-bust')
        self.add_arc('left-head', (10, 30), (10, 34), radius_x=2, radius_y=2, sweep=False, large_arc=False)
        self.add_arc('left-shoulder', (10, 34), (6, 42), radius_x=4, radius_y=8, sweep=False, large_arc=False)
        self.add_line('left-base', (6, 42), (14, 42))
        self.add_contour('left-person', 'left-head', 'left-shoulder', 'left-base', closed=False)
        self.relate("connect", 'left-person', 'central-bust')
        self.add_line('right-base', (34, 42), (42, 42))
        self.add_arc('right-shoulder', (42, 42), (38, 34), radius_x=4, radius_y=8, sweep=False, large_arc=False)
        self.add_arc('right-head', (38, 34), (38, 30), radius_x=2, radius_y=2, sweep=False, large_arc=False)
        self.add_contour('right-person', 'right-base', 'right-shoulder', 'right-head', closed=False)
        self.relate("connect", 'right-person', 'central-bust')
        self.add_polyline('finger', (36, 6), (27, 6), (18, 13), (15, 21), closed=False)
        self.add_arc('fingertip', (15, 21), (19, 23), radius_x=3, radius_y=3, sweep=False, large_arc=False)
        self.add_polyline('finger-inner', (19, 23), (23, 17), (28, 15), closed=False)
        self.add_arc('thumb-tip', (28, 15), (31, 19), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_polyline('thumb', (31, 19), (29, 23), (38, 18), (40, 12), closed=False)
        self.relate("connect", 'finger', 'fingertip')
        self.relate("connect", 'fingertip', 'finger-inner')
        self.relate("connect", 'finger-inner', 'thumb-tip')
        self.relate("connect", 'thumb-tip', 'thumb')
