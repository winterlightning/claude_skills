"""Stacked Data Tables -- batch-002 r2 generation.

Subject: a data table with a header row and a three-column grid, stacked in
front of a second table whose top and right edges show behind it.

Plan: the front table is a rounded rectangle (radius 4) that owns its grid.
The header rule and the row rule are chords, and two column dividers drop
from the header to the bottom edge. The columns form a 9-unit series and the
rows are 9 and 10 tall. The back table is an open L run (top edge, one
rounded corner and right edge), offset up and right. It keeps 9 from the
front table's rounded contour.
Keyshape SQUARE; centerline box (6,6)-(42,42).
Reduction: none; back sheet, header, row rule and both column dividers are
kept.
Construction reference: Lucide table (rounded frame with header and column
chords), re-derived on the SOLO48 grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_002_r2_shapes import path, polyline, rounded_rect

SOURCE_ICON_ID = '63d1d0fb-c8bf-466e-9407-df40a01495f1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/business/workflow data table stack_63d1d0fb-c8bf-466e-9407-df40a01495f1.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-002/references/workflow data table stack_63d1d0fb-c8bf-466e-9407-df40a01495f1.svg'
AUTHOR = 'claude-opus-5'

LEFT, TOP, RIGHT, BOTTOM, RADIUS = 6, 6, 42, 42, 4
OFFSET = 9
FRONT_TOP, FRONT_RIGHT = TOP + OFFSET, RIGHT - OFFSET
HEADER_Y, ROW_Y = FRONT_TOP + 8, FRONT_TOP + 17
COLUMN_STEP = 9


class StackedDataTablesBatch002R2(Solo48):
    icon_id = 'stacked-data-tables-batch-002-r2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/data'
    aliases = ('table-stack', 'data-tables', 'spreadsheets')
    keywords = ('table', 'data', 'grid', 'spreadsheet', 'stack', 'database', 'rows', 'columns')

    def build(self) -> None:
        columns = [LEFT + COLUMN_STEP * i for i in (1, 2)]
        rounded_rect(self, 'front', LEFT, FRONT_TOP, FRONT_RIGHT, BOTTOM, RADIUS,
                     nodes=[(LEFT, HEADER_Y), (FRONT_RIGHT, HEADER_Y),
                            (LEFT, ROW_Y), (FRONT_RIGHT, ROW_Y),
                            *[(x, BOTTOM) for x in columns]])
        polyline(self, 'header-rule', (LEFT, HEADER_Y), (FRONT_RIGHT, HEADER_Y),
                 nodes=[(x, HEADER_Y) for x in columns])
        polyline(self, 'row-rule', (LEFT, ROW_Y), (FRONT_RIGHT, ROW_Y),
                 nodes=[(x, ROW_Y) for x in columns])
        for i, x in enumerate(columns):
            name = f'column-{i + 1}'
            polyline(self, name, (x, HEADER_Y), (x, BOTTOM), nodes=((x, ROW_Y),))
            self.relate('connect', name, 'header-rule')
            self.relate('connect', name, 'row-rule')
            self.relate('connect', name, 'front')
        self.relate('connect', 'front', 'header-rule')
        self.relate('connect', 'front', 'row-rule')
        path(self, 'back', (LEFT + OFFSET, TOP),
             ('L', (RIGHT - RADIUS, TOP)),
             ('A', (RIGHT, TOP + RADIUS), RADIUS, RADIUS, True),
             ('L', (RIGHT, BOTTOM - OFFSET)))
