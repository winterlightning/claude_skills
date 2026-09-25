"""Traditional Honensai Harvest Festival.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Roofed ceremonial stand above three procession heads.
Reduction: Simplify fertility projection to a horizontal ceremonial beam; human_ref/user.svg, heads end y=30 and shoulders start y=38 give exact 4 ink gap.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'abee9503-fe72-4b3a-913c-0fd8883e1517'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/honensai with persons_abee9503-fe72-4b3a-913c-0fd8883e1517.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/honensai with persons_abee9503-fe72-4b3a-913c-0fd8883e1517.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-014/references/honensai with persons_abee9503-fe72-4b3a-913c-0fd8883e1517.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'roofed-festival-sculpture-with-procession-batch-014-11'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('honensai', 'festival', 'sculpture', 'roof', 'procession', 'people')

    def build(self):
        self.add_polyline('roof', (12, 16), (24, 6), (36, 16), closed=True)
        self.add_line('beam-left', (6, 16), (12, 16))
        self.add_line('beam-right', (36, 16), (42, 16))
        self.relate("connect", 'roof', 'beam-left')
        self.relate("connect", 'roof', 'beam-right')
        self.add_arc('head-0-1', (10, 24), (13, 27), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-0-2', (13, 27), (10, 30), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-0-3', (10, 30), (7, 27), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-0-4', (7, 27), (10, 24), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head-0', 'head-0-1', 'head-0-2', 'head-0-3', 'head-0-4', closed=True)
        self.add_arc('head-1-1', (24, 24), (27, 27), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-1-2', (27, 27), (24, 30), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-1-3', (24, 30), (21, 27), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-1-4', (21, 27), (24, 24), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head-1', 'head-1-1', 'head-1-2', 'head-1-3', 'head-1-4', closed=True)
        self.add_arc('head-2-1', (38, 24), (41, 27), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-2-2', (41, 27), (38, 30), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-2-3', (38, 30), (35, 27), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-2-4', (35, 27), (38, 24), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head-2', 'head-2-1', 'head-2-2', 'head-2-3', 'head-2-4', closed=True)
        self.add_bezier('shoulders-1', (6, 42), ((6, 38), (7, 38), (10, 38)))
        self.add_bezier('shoulders-2', (10, 38), ((13, 38), (15, 38), (17, 42)))
        self.add_bezier('shoulders-3', (17, 42), ((19, 38), (21, 38), (24, 38)))
        self.add_bezier('shoulders-4', (24, 38), ((27, 38), (29, 38), (31, 42)))
        self.add_bezier('shoulders-5', (31, 42), ((33, 38), (35, 38), (38, 38)))
        self.add_bezier('shoulders-6', (38, 38), ((41, 38), (42, 38), (42, 42)))
        self.add_contour('shoulders', 'shoulders-1', 'shoulders-2', 'shoulders-3', 'shoulders-4', 'shoulders-5', 'shoulders-6', closed=False)
