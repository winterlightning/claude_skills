"""Teacher presenting at whiteboard: independent spacing revision.

Remove narrow leg split and arm seams; open the two legs and add a clear presenting arm.
Native container family, SQUARE keyshape. The original model is preserved.
Directional and natural asymmetry follows the supplied subject.
Final construction review: Original subject render; no exact Lucide match selected.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (teacher-presenting-at-whiteboard SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
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
        self.add_line('board-0', (29, 6), (52, 6))
        self.add_arc('board-1', (52, 6), (58, 11), radius_x=6, radius_y=5)
        self.add_line('board-2', (58, 11), (58, 46))
        self.add_arc('board-3', (58, 46), (52, 51), radius_x=6, radius_y=5)
        self.add_line('board-4', (52, 51), (37, 51))
        self.add_arc('head-0', (10, 14), (18, 6), radius_x=8)
        self.add_arc('head-1', (18, 6), (25, 14), radius_x=7, radius_y=8)
        self.add_arc('head-2', (25, 14), (18, 22), radius_x=7, radius_y=8)
        self.add_arc('head-3', (18, 22), (10, 14), radius_x=8)
        self.add_line('torso', (18, 28), (18, 44))
        self.add_line('legs-1', (6, 58), (18, 44))
        self.add_line('legs-2', (18, 44), (29, 58))
        self.add_line('arms-1', (6, 39), (18, 28))
        self.add_line('arms-2', (18, 28), (29, 39))
        self.add_line('arms-3', (29, 39), (37, 30))
        self.add_contour('board', 'board-0', 'board-1', 'board-2', 'board-3', 'board-4')
        self.add_contour('head', 'head-0', 'head-1', 'head-2', 'head-3', closed=True)
        self.add_contour('legs', 'legs-1', 'legs-2')
        self.add_contour('arms', 'arms-1', 'arms-2', 'arms-3')
        self.relate('connect', 'legs', 'torso')
        self.relate('connect', 'arms', 'torso')
        self.mark_human_figure('teacher', head='head', torso='torso', torso_junction='start')
