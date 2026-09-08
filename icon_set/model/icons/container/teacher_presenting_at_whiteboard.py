"""A teacher stands at the left of an open-sided presentation board.

Keyshape SQUARE: (0, 0, 64, 64); chosen for the reference silhouette.
Construction reference: Lucide presentation: quarter-circle board corners. Original and atomic-debug inspected.
The teacher keeps head, torso, arms and paired legs. The board is intentionally offset right and open behind the figure.
Hosting measured with compose.py: plus does not pass, heart does not pass, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class TeacherPresentingAtWhiteboard(Container64):
    icon_id = 'teacher-presenting-at-whiteboard'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('teacher', 'presenting', 'at', 'whiteboard')

    def build(self) -> None:
        self.add_line('board-top', (28, 2), (56, 2))
        self.add_arc('board-ne', (56, 2), (62, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_line('board-right', (62, 8), (62, 48))
        self.add_arc('board-se', (62, 48), (56, 54), radius_x=6, radius_y=6, sweep=True)
        self.add_line('board-bottom', (56, 54), (38, 54))
        self.add_contour('board', 'board-top', 'board-ne', 'board-right', 'board-se', 'board-bottom', closed=False)
        self.add_arc('head-top', (6, 11), (24, 11), radius_x=9, radius_y=9, sweep=True)
        self.add_arc('head-bottom', (24, 11), (6, 11), radius_x=9, radius_y=9, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('shoulders', (2, 40), (28, 40), radius_x=13, radius_y=13, sweep=True)
        self.add_line('torso-right', (28, 40), (28, 46))
        self.add_line('torso-bottom', (28, 46), (2, 46))
        self.add_line('torso-left', (2, 46), (2, 40))
        self.add_contour('torso', 'shoulders', 'torso-right', 'torso-bottom', 'torso-left', closed=True)
        self.add_polyline('legs', (7, 46), (9, 62), (21, 62), (23, 46), closed=False)
        self.relate("connect", 'legs', 'torso')
        self.add_line('leg-split', (15, 54), (15, 62))
        self.relate("connect", 'leg-split', 'legs')
        self.add_line('arm-left', (7, 38), (7, 46))
        self.add_line('arm-right', (23, 38), (23, 46))
        self.relate("connect", 'arm-left', 'torso')
        self.relate("connect", 'arm-left', 'legs')
        self.relate("connect", 'arm-right', 'torso')
        self.relate("connect", 'arm-right', 'legs')
