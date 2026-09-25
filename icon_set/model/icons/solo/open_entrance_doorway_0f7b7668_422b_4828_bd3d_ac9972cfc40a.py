'Open Entrance Doorway.\n\nSymbol plan: Open angled door within frame, handle and short ground extensions.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: door-open.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f7b7668-422b-4828-bd3d-ac9972cfc40a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/door open_0f7b7668-422b-4828-bd3d-ac9972cfc40a.svg'
AUTHOR = 'gpt-6'

class OpenEntranceDoorway(Solo48):
    icon_id = 'open-entrance-doorway'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('open', 'entrance', 'doorway')

    def build(self):
        # Open angled door within frame, handle and short ground extensions.
        axis_x = 24
        p_8_40 = (8, 40)
        p_12_4 = (12, 4)
        p_12_40 = (12, 40)
        p_20_12 = (20, 12)
        p_20_44 = (20, 44)
        p_28_23 = (28, 23)
        p_28_27 = (28, 27)
        p_36_4 = (2 * axis_x - p_12_4[0], p_12_4[1])
        p_36_36 = (36, 36)
        p_36_40 = (2 * axis_x - p_12_40[0], p_12_40[1])
        p_40_40 = (2 * axis_x - p_8_40[0], p_8_40[1])
        self.add_line('frame-1', p_8_40, p_12_40)
        self.add_line('frame-2', p_12_40, p_12_4)
        self.add_line('frame-3', p_12_4, p_36_4)
        self.add_line('frame-4', p_36_4, p_36_40)
        self.add_line('frame-5', p_36_40, p_40_40)
        self.add_contour('frame', 'frame-1', 'frame-2', 'frame-3', 'frame-4', 'frame-5', closed=False)
        self.add_line('door-1', p_20_44, p_20_12)
        self.add_line('door-2', p_20_12, p_36_4)
        self.add_line('door-3', p_36_4, p_36_36)
        self.add_line('door-4', p_36_36, p_20_44)
        self.add_contour('door', 'door-1', 'door-2', 'door-3', 'door-4', closed=False)
        self.relate("connect", 'door', 'frame')
        self.add_line('handle-1', p_28_23, p_28_27)
        self.add_contour('handle', 'handle-1', closed=False)
