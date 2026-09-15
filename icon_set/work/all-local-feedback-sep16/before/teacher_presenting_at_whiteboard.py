'Teacher presenting at whiteboard: independent spacing revision.\n\nRemove narrow leg split and arm seams; open the two legs and add a clear presenting arm.\nNative container family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'

class TeacherPresentingAtWhiteboard(Container64):
    icon_id = 'teacher-presenting-at-whiteboard'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'containers'
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
        self.add_line('leg-left', (7, 46), (7, 62))
        self.add_line('leg-right', (23, 46), (23, 62))
        self.add_line('presenting-arm', (28, 40), (38, 30))
        self.relate('connect', 'torso', 'leg-left')
        self.relate('connect', 'torso', 'leg-right')
        self.relate('connect', 'torso', 'presenting-arm')
SOURCE_ICON_ID = None
SOURCE_PATH = None
