"""A presenter raises one arm toward a wall-mounted chart."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID='c23af45f-822e-420c-bd3d-1882023ab26f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__presenter-at-chart/20260927T153747Z-thuan-mac-1/reference/workflow coaching chart_c23af45f-822e-420c-bd3d-1882023ab26f.svg'
AUTHOR = 'gpt-6'

class PresenterAtChart(Solo48):
    icon_id='presenter-at-chart'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    categories = ("office", "primitives")
    aliases=()
    keywords=('presenter', 'chart', 'screen', 'coaching', 'person', 'office')

    def build(self):
        # Bust at left, raised arm, and an open chart with a directional trend.
        self.add_arc('head-top', (6, 16), (14, 16), radius_x=4)
        self.add_arc('head-bottom', (14, 16), (6, 16), radius_x=4)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('body', (4, 40), (4, 34), (10, 28), (16, 28), (16, 40))
        self.add_line('raised-arm', (16, 28), (24, 20))
        self.add_polyline('screen', (24, 20), (24, 8), (44, 8), (44, 32), (24, 32))
        self.add_polyline('trend', (32, 22), (34, 24), (36, 20))
        self.relate('connect', 'body', 'raised-arm')
        self.relate('connect', 'raised-arm', 'screen')
        self.mark_human_figure('presenter', head='head', torso='body-1', torso_junction='end')
