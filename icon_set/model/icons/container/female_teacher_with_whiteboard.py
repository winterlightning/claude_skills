"""A female teacher in a dress stands beside an open classroom whiteboard.

Keyshape SQUARE: visible bounds (0, 0, 64, 64).
Lucide presentation informs rounded board corners; user-round informs the
circular head and smooth shoulder arch. Source supplies dress, swept hair and
open board layout. Centerline extremes (2,2)-(62,62). The figure remains on
the left; simplified hair and garment preserve identity at native size.
Hosting measured with compose.py: plus does not pass, heart does not pass, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (female-teacher-with-whiteboard SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4. Hand-repaired after the fit: legs 8 apart.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): the shape caps it below 24, now it takes a 20 symbol with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

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
        # A narrower teacher (head r6 about (16,13), dress 8..24) leaves the board 30..58 clear of her hair, so the
        # board holds a symbol of 20 with a 4 px gap (was 19). Head-to-shoulder ink gap 4 (head bottom 19,
        # shoulders top 27).
        self.add_arc('head-top', (10, 13), (22, 13), radius_x=6)
        self.add_arc('head-bottom', (22, 13), (10, 13), radius_x=6)
        self.add_arc('hair-left', (10, 13), (6, 17), radius_x=4)
        self.add_arc('hair-right', (22, 13), (25, 17), radius_x=4, sweep=False)
        self.add_arc('shoulders', (10, 33), (22, 33), radius_x=6)
        self.add_line('dress-right', (22, 33), (24, 48))
        self.add_line('hem', (24, 48), (8, 48))
        self.add_line('dress-left', (8, 48), (10, 33))
        self.add_line('leg-12', (12, 48), (12, 58))
        self.add_line('leg-20', (20, 48), (20, 58))
        self.add_line('board-top', (30, 6), (52, 6))
        self.add_arc('board-ne', (52, 6), (58, 12), radius_x=6)
        self.add_line('board-right', (58, 12), (58, 44))
        self.add_arc('board-se', (58, 44), (52, 50), radius_x=6)
        self.add_line('board-bottom', (52, 50), (34, 50))
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_contour('dress', 'shoulders', 'dress-right', 'hem', 'dress-left', closed=True)
        self.add_contour('board', 'board-top', 'board-ne', 'board-right', 'board-se', 'board-bottom')
        self.relate('connect', 'head', 'hair-left')
        self.relate('connect', 'head', 'hair-right')
        self.relate('connect', 'dress', 'leg-12')
        self.relate('connect', 'dress', 'leg-20')
