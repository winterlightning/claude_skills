"""Person Beside Surfboard. Front-facing person beside a tall pointed surfboard with a flat tail; omit diagonal board stripe for a clear silhouette.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4394c3a4-148d-4234-842b-4dbdd29ad331'
SOURCE_PATH = 'pictographic-primitives/recreation/nautic sports surfing_4394c3a4-148d-4234-842b-4dbdd29ad331.svg'
AUTHOR = 'gpt-6'


class PersonBesideSurfboard(Solo48):
    icon_id = 'person-beside-surfboard'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation"
    aliases = ()
    keywords = ('person', 'beside', 'surfboard')

    def build(self) -> None:
        self.add_arc('head-top', (11, 9), (17, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (17, 9), (11, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('person-1', (6, 30), (6, 24))
        self.add_line('person-2', (6, 24), (14, 22))
        self.add_line('person-3', (14, 22), (22, 24))
        self.add_line('person-4', (22, 24), (22, 30))
        self.add_contour('person', 'person-1', 'person-2', 'person-3', 'person-4', closed=False)
        self.add_line('legs-1', (10, 42), (14, 31))
        self.add_line('legs-2', (14, 31), (18, 42))
        self.add_contour('legs', 'legs-1', 'legs-2', closed=False)
        self.add_line('torso', (14, 22), (14, 31))
        self.relate("connect", 'person', 'torso')
        self.relate("connect", 'legs', 'torso')
        self.add_arc('board-left', (37, 6), (32, 27), radius_x=5, radius_y=21, sweep=False)
        self.add_line('tail-1', (32, 27), (33, 42))
        self.add_line('tail-2', (33, 42), (41, 42))
        self.add_line('tail-3', (41, 42), (42, 27))
        self.add_arc('board-right', (42, 27), (37, 6), radius_x=5, radius_y=21, sweep=False)
        self.add_contour('surfboard', 'board-left', 'tail-1', 'tail-2', 'tail-3', 'board-right', closed=True)
