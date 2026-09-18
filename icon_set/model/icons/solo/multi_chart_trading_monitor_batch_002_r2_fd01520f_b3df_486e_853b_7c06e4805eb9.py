"""Multi Chart Trading Monitor -- batch-002 r2 generation.

Subject: a desktop trading monitor showing a price chart, on a stand.

Plan: symmetric housing about x=24. A rounded screen (radius 4) is split at
the neck node on its bottom edge. The neck drops to a centred base whose
midpoint it shares. The price chart is one open zigzag of 45-degree runs,
held 9 inside the rounded screen, which cannot certify exactly 8.
Keyshape HRECT_L; centerline box (4,8)-(44,40).
Reduction: the reference's 2x2 panel grid with four mini charts cannot hold a
readable chart inside any 20x12 cell with 4-unit clearance at 48. The grid is
reduced to one screen-wide chart. The multi-panel layout is recorded here
rather than drawn as empty cells.
Construction reference: Lucide monitor (rounded screen, centred neck and
base) and chart-line zigzag, re-derived on the SOLO48 grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_002_r2_shapes import polyline, rounded_rect

SOURCE_ICON_ID = 'fd01520f-b3df-486e-853b-7c06e4805eb9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/business/trading monitor_fd01520f-b3df-486e-853b-7c06e4805eb9.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-002/references/trading monitor_fd01520f-b3df-486e-853b-7c06e4805eb9.svg'
AUTHOR = 'claude-opus-5'

AXIS = 24
LEFT, TOP, RIGHT, SCREEN_BOTTOM, BASE_Y, RADIUS = 4, 8, 44, 32, 40, 4
BASE_HALF = 8
CHART = ((13, 23), (18, 18), (22, 22), (27, 17), (35, 17))


class MultiChartTradingMonitorBatch002R2(Solo48):
    icon_id = 'multi-chart-trading-monitor-batch-002-r2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/business'
    aliases = ('trading-monitor', 'stock-monitor', 'trading-screen')
    keywords = ('monitor', 'trading', 'chart', 'stock', 'market', 'finance', 'screen', 'desktop')

    def build(self) -> None:
        neck_top, neck_bottom = (AXIS, SCREEN_BOTTOM), (AXIS, BASE_Y)
        rounded_rect(self, 'screen', LEFT, TOP, RIGHT, SCREEN_BOTTOM, RADIUS, nodes=(neck_top,))
        self.add_line('neck', neck_top, neck_bottom)
        polyline(self, 'base', (AXIS - BASE_HALF, BASE_Y), (AXIS + BASE_HALF, BASE_Y),
                 nodes=(neck_bottom,))
        self.relate('connect', 'screen', 'neck')
        self.relate('connect', 'neck', 'base')
        polyline(self, 'chart', *CHART)
