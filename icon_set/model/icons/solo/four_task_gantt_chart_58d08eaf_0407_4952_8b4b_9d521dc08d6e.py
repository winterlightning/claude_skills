'Project Management Gantt Chart.\n\nSymbol plan: Four task bars at equal row spacing beside a timeline. Outlined bars reduce to round-ended strokes.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: chart-no-axes-gantt.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '58d08eaf-0407-4952-8b4b-9d521dc08d6e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/workflow gantt chart 4_58d08eaf-0407-4952-8b4b-9d521dc08d6e.svg'
AUTHOR = 'gpt-6'

class FourTaskGanttChart(Solo48):
    icon_id = 'four-task-gantt-chart'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('four', 'task', 'gantt', 'chart')

    def build(self):
        # Four task bars at equal row spacing beside a timeline. Outlined bars reduce to round-ended strokes.
        axis_x = 24
        p_4_8 = (4, 8)
        p_4_40 = (4, 40)
        p_12_8 = (12, 8)
        p_12_38 = (12, 38)
        p_20_18 = (20, 18)
        p_28_8 = (28, 8)
        p_28_28 = (28, 28)
        p_28_38 = (28, 38)
        p_36_18 = (36, 18)
        p_44_28 = (44, 28)
        self.add_line('axis-1', p_4_8, p_4_40)
        self.add_contour('axis', 'axis-1', closed=False)
        self.add_line('task0-1', p_12_8, p_28_8)
        self.add_contour('task0', 'task0-1', closed=False)
        self.add_line('task1-1', p_20_18, p_36_18)
        self.add_contour('task1', 'task1-1', closed=False)
        self.add_line('task2-1', p_28_28, p_44_28)
        self.add_contour('task2', 'task2-1', closed=False)
        self.add_line('task3-1', p_12_38, p_28_38)
        self.add_contour('task3', 'task3-1', closed=False)
