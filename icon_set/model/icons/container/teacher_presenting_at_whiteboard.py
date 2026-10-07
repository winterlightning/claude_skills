"""Teacher presenting at whiteboard: independent spacing revision.

Remove narrow leg split and arm seams; open the two legs and add a clear presenting arm.
Native container family, SQUARE keyshape. The original model is preserved.
Directional and natural asymmetry follows the supplied subject.
Final construction review: Original subject render; no exact Lucide match selected.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (teacher-presenting-at-whiteboard SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): closed board and a slimmer teacher pointing at its edge, so the symbol centres in the board (container-combination64).
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class TeacherPresentingAtWhiteboard(Container64):
    icon_id = 'teacher-presenting-at-whiteboard'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('teacher', 'presenting', 'at', 'whiteboard')

    def build(self) -> None:
        # A whiteboard open on the teacher's side, as the original: top edge 24..53, rounded right side 58, bottom
        # edge back to 30, no left edge; a slim stick-figure teacher on the left:
        # head r5 at (12,12), torso 25..42 (4 units of ink below the head), legs to the floor at 58, one arm down
        # and the pointing arm reaching to the board's open side at (24,20). The board holds a
        # symbol of 20 (24 when its ink keeps 2 px) centred near (41,25).
        self.add_line('board-0', (24, 6), (53, 6))
        self.add_arc('board-1', (53, 6), (58, 11), radius_x=5)
        self.add_line('board-2', (58, 11), (58, 39))
        self.add_arc('board-3', (58, 39), (53, 44), radius_x=5)
        self.add_line('board-4', (53, 44), (30, 44))
        self.add_arc('head-0', (7, 12), (17, 12), radius_x=5)
        self.add_arc('head-1', (17, 12), (7, 12), radius_x=5)
        self.add_line('torso', (12, 25), (12, 42))
        self.add_line('legs-1', (6, 58), (12, 42))
        self.add_line('legs-2', (12, 42), (18, 58))
        self.add_line('arms-1', (6, 33), (12, 25))
        self.add_line('arms-2', (12, 25), (24, 20))
        self.add_contour('board', 'board-0', 'board-1', 'board-2', 'board-3', 'board-4')
        self.add_contour('head', 'head-0', 'head-1', closed=True)
        self.add_contour('legs', 'legs-1', 'legs-2')
        self.add_contour('arms', 'arms-1', 'arms-2')
        self.relate('connect', 'torso', 'legs')
        self.relate('connect', 'torso', 'arms')
        self.mark_human_figure('teacher', head='head', torso='torso', torso_junction='start')
