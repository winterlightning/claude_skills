"""Person and Business Growth Chart -- batch-002 r2 generation.

Subject: a presenter bust standing beside a presentation board whose chart
is a rising arrow; the board stands on a post and foot.

Plan: two symbols under one root. The person is a detached bust built from
the shared human reference (icon_set/references/human_ref/user.svg): a
circular head (radius 4) above a dome of two quarter-ellipse shoulders
(rx 8, ry 6). The head outline sits exactly 8 centerline units / 4 ink units
above the shoulder apex, which is the neck junction. The board is an open
run: a short left stub, the top, the right side and a bottom edge that stops
short of the head. The board is left open on the person's side, as in the
reference. The rising arrow keeps exactly 8 from the straight board edges and
more than 9 from the head. The stand post shares a node on the board bottom
and the centre of its foot.
Keyshape SQUARE; centerline box (6,6)-(42,42).
Reduction: the two data dots on the chart line are dropped (they close up at
48); the rising arrow carries the growth meaning.
Construction reference: Lucide presentation (board with centred post) for
the board; shared human_ref/user.svg for the bust proportions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_002_r2_shapes import circle, path, polyline

SOURCE_ICON_ID = 'aca4af14-d513-5480-b973-52f14722c981'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/business/customer relationship management performance metrics_aca4af14-d513-5480-b973-52f14722c981.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-002/references/customer relationship management performance metrics_aca4af14-d513-5480-b973-52f14722c981.svg'
AUTHOR = 'claude-opus-5'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'

# Person: head outline bottom 28, shoulder apex 36 -> 8 centerline / 4 ink.
HEAD_CX, HEAD_CY, HEAD_R = 14, 24, 4
SHOULDER_RX, SHOULDER_RY, GROUND = 8, 6, 42
SHOULDER_APEX_Y = HEAD_CY + HEAD_R + 8
# Board.
BOARD_LEFT, BOARD_TOP, BOARD_RIGHT, BOARD_BOTTOM = 14, 6, 42, 30
STUB_BOTTOM, BOARD_BOTTOM_LEFT = 11, 26
POST_X, FOOT_HALF = 34, 3
# Arrow: head corner 8 below the top and 8 left of the right side.
TIP = (BOARD_RIGHT - 8, BOARD_TOP + 8)
TAIL, BARB = (27, 21), 6


class PersonAndBusinessGrowthChartBatch002R2(Solo48):
    icon_id = 'person-and-business-growth-chart-batch-002-r2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/business'
    aliases = ('presenter-growth-chart', 'business-presentation')
    keywords = ('person', 'presentation', 'growth', 'chart', 'board', 'business',
                'performance', 'metrics', 'crm', 'arrow')

    def build(self) -> None:
        circle(self, 'head', HEAD_CX, HEAD_CY, HEAD_R)
        apex = (HEAD_CX, SHOULDER_APEX_Y)
        self.add_arc('shoulder-left', (HEAD_CX - SHOULDER_RX, GROUND), apex,
                     radius_x=SHOULDER_RX, radius_y=SHOULDER_RY)
        self.add_arc('shoulder-right', apex, (HEAD_CX + SHOULDER_RX, GROUND),
                     radius_x=SHOULDER_RX, radius_y=SHOULDER_RY)
        self.add_contour('shoulders', 'shoulder-left', 'shoulder-right')
        self.mark_human_figure('person', head='head', torso='shoulder-left',
                               torso_junction='end')

        post_top, post_foot = (POST_X, BOARD_BOTTOM), (POST_X, GROUND)
        path(self, 'board', (BOARD_LEFT, STUB_BOTTOM),
             ('L', (BOARD_LEFT, BOARD_TOP)), ('L', (BOARD_RIGHT, BOARD_TOP)),
             ('L', (BOARD_RIGHT, BOARD_BOTTOM)), ('L', post_top),
             ('L', (BOARD_BOTTOM_LEFT, BOARD_BOTTOM)))
        self.add_line('post', post_top, post_foot)
        polyline(self, 'foot', (POST_X - FOOT_HALF, GROUND), (POST_X + FOOT_HALF, GROUND),
                 nodes=(post_foot,))
        self.relate('connect', 'board', 'post')
        self.relate('connect', 'post', 'foot')

        self.add_line('arrow-shaft', TAIL, TIP)
        polyline(self, 'arrow-head', (TIP[0] - BARB, TIP[1]), TIP, (TIP[0], TIP[1] + BARB))
        self.relate('connect', 'arrow-shaft', 'arrow-head')
