'Project Management Gantt Chart.\n\nSymbol plan: Six rounded task bars retain the three-two-one staircase pattern. Round-ended strokes replace tiny outlined bar interiors.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: chart-no-axes-gantt.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b62564b-146e-40a6-b154-9dc3b0f68747'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/workflow gantt chart_9b62564b-146e-40a6-b154-9dc3b0f68747.svg'
AUTHOR = 'gpt-6'

class RoundedStaggeredTaskBars(Solo48):
    icon_id = 'rounded-staggered-task-bars'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'diagrams'
    categories = ('diagrams', 'primitives')
    aliases = ()
    keywords = ('rounded', 'staggered', 'task', 'bars')

    def build(self):
        # Six rounded task bars retain the three-two-one staircase pattern. Round-ended strokes replace tiny outlined bar interiors.
        axis_x = 24
        p_4_8 = (4, 8)
        p_4_24 = (4, 24)
        p_4_40 = (4, 40)
        p_14_8 = (14, 8)
        p_14_24 = (14, 24)
        p_14_40 = (14, 40)
        p_19_16 = (19, 16)
        p_19_32 = (19, 32)
        p_29_16 = (2 * axis_x - p_19_16[0], p_19_16[1])
        p_29_32 = (2 * axis_x - p_19_32[0], p_19_32[1])
        p_34_24 = (2 * axis_x - p_14_24[0], p_14_24[1])
        p_44_24 = (2 * axis_x - p_4_24[0], p_4_24[1])
        self.add_line('task0-1', p_4_8, p_14_8)
        self.add_contour('task0', 'task0-1', closed=False)
        self.add_line('task1-1', p_19_16, p_29_16)
        self.add_contour('task1', 'task1-1', closed=False)
        self.add_line('task2-1', p_34_24, p_44_24)
        self.add_contour('task2', 'task2-1', closed=False)
        self.add_line('task3-1', p_4_24, p_14_24)
        self.add_contour('task3', 'task3-1', closed=False)
        self.add_line('task4-1', p_19_32, p_29_32)
        self.add_contour('task4', 'task4-1', closed=False)
        self.add_line('task5-1', p_4_40, p_14_40)
        self.add_contour('task5', 'task5-1', closed=False)
