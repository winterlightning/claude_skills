"""A female teacher in a dress stands beside an open classroom whiteboard.

Keyshape SQUARE: visible bounds (0, 0, 64, 64).
Lucide presentation informs rounded board corners; user-round informs the
circular head and smooth shoulder arch. Source supplies dress, swept hair and
open board layout. Centerline extremes (2,2)-(62,62). The figure remains on
the left; simplified hair and garment preserve identity at native size.
Hosting measured with compose.py: plus does not pass, heart does not pass, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (female-teacher-with-whiteboard SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4. Hand-repaired after the fit: legs 8 apart.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class FemaleTeacherWithWhiteboard(Container64):
    icon_id = 'female-teacher-with-whiteboard'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('teacher-whiteboard',)
    keywords = ('teacher', 'woman', 'board', 'education')

    def build(self) -> None:
        self.add_arc('head-top', (10, 14), (26, 14), radius_x=8)
        self.add_arc('head-bottom', (26, 14), (10, 14), radius_x=8)
        self.add_arc('hair-sweep', (10, 14), (24, 9), radius_x=22, sweep=False)
        self.add_arc('hair-left', (10, 14), (6, 19), radius_x=5)
        self.add_arc('hair-right', (26, 14), (30, 19), radius_x=5, sweep=False)
        self.add_arc('shoulders', (11, 38), (25, 38), radius_x=7)
        self.add_line('dress-right', (25, 38), (28, 50))
        self.add_line('hem', (28, 50), (8, 50))
        self.add_line('dress-left', (8, 50), (11, 38))
        self.add_line('leg-12', (14, 50), (14, 58))
        self.add_line('leg-20', (22, 50), (22, 58))
        self.add_line('board-top', (30, 6), (52, 6))
        self.add_arc('board-ne', (52, 6), (58, 11), radius_x=6, radius_y=5)
        self.add_line('board-right', (58, 11), (58, 45))
        self.add_arc('board-se', (58, 45), (52, 50), radius_x=6, radius_y=5)
        self.add_line('board-bottom', (52, 50), (38, 50))
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_contour('dress', 'shoulders', 'dress-right', 'hem', 'dress-left', closed=True)
        self.add_contour('board', 'board-top', 'board-ne', 'board-right', 'board-se', 'board-bottom')
        self.relate('connect', 'head', 'hair-sweep')
        self.relate('connect', 'head', 'hair-left')
        self.relate('connect', 'head', 'hair-right')
        self.relate('connect', 'hair-sweep', 'hair-left')
        self.relate('connect', 'dress', 'leg-12')
        self.relate('connect', 'dress', 'leg-20')
