"""A female teacher in a dress stands beside an open classroom whiteboard.

Keyshape SQUARE: visible bounds (0, 0, 64, 64).
Lucide presentation informs rounded board corners; user-round informs the
circular head and smooth shoulder arch. Source supplies dress, swept hair and
open board layout. Centerline extremes (2,2)-(62,62). The figure remains on
the left; simplified hair and garment preserve identity at native size.
Hosting measured with compose.py: plus does not pass, heart does not pass, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class FemaleTeacherWithWhiteboard(Container64):
    icon_id = 'female-teacher-with-whiteboard'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('teacher-whiteboard',)
    keywords = ('teacher', 'woman', 'board', 'education')

    def build(self) -> None:
        self.add_arc('head-top', (6, 12), (26, 12), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('head-bottom', (26, 12), (6, 12), radius_x=10, radius_y=10, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('hair-sweep', (6, 12), (24, 6), radius_x=20, radius_y=20, sweep=False)
        self.relate("connect", 'head', 'hair-sweep')
        self.add_arc('hair-left', (6, 12), (2, 18), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('hair-right', (26, 12), (30, 18), radius_x=6, radius_y=6, sweep=False)
        self.relate("connect", 'head', 'hair-left')
        self.relate("connect", 'head', 'hair-right')
        self.relate("connect", 'hair-sweep', 'hair-left')
        self.add_arc('shoulders', (8, 38), (24, 38), radius_x=8, radius_y=8, sweep=True)
        self.add_line('dress-right', (24, 38), (28, 52))
        self.add_line('hem', (28, 52), (4, 52))
        self.add_line('dress-left', (4, 52), (8, 38))
        self.add_contour('dress', 'shoulders', 'dress-right', 'hem', 'dress-left', closed=True)
        self.add_line('leg-12', (12, 52), (12, 62))
        self.relate("connect", 'dress', 'leg-12')
        self.add_line('leg-20', (20, 52), (20, 62))
        self.relate("connect", 'dress', 'leg-20')
        self.add_line('board-top', (30, 2), (56, 2))
        self.add_arc('board-ne', (56, 2), (62, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_line('board-right', (62, 8), (62, 46))
        self.add_arc('board-se', (62, 46), (56, 52), radius_x=6, radius_y=6, sweep=True)
        self.add_line('board-bottom', (56, 52), (38, 52))
        self.add_contour('board', 'board-top', 'board-ne', 'board-right', 'board-se', 'board-bottom', closed=False)
