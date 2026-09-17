"""Congregational Group with Rising Sun.

SOLO48 visible bounds: (2, 6, 46, 42). Centerline extremes: (4, 8, 44, 40).

Symbol plan: Three equal detached heads below a rising semicircular sun.
Reduction: Omit small sun rays; retain three-person congregation. Human_ref/user.svg; each head bottom y=28, shoulder apex y=36: exact 4 ink gap.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f7860911-157a-4fff-a6a5-f904dc8d19e7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/jumu ah_f7860911-157a-4fff-a6a5-f904dc8d19e7.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/jumu ah_f7860911-157a-4fff-a6a5-f904dc8d19e7.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-014/references/jumu ah_f7860911-157a-4fff-a6a5-f904dc8d19e7.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'congregation-beneath-rising-sun-batch-014-04'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('congregation', 'people', 'group', 'sun', 'rays', 'gathering')

    def build(self):
        self.add_arc('sun-1', (14, 12), (34, 12), radius_x=10, radius_y=4, sweep=True)
        self.add_contour('sun', 'sun-1', closed=False)
        self.add_arc('head-0-1', (10, 22), (13, 25), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-0-2', (13, 25), (10, 28), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-0-3', (10, 28), (7, 25), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-0-4', (7, 25), (10, 22), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head-0', 'head-0-1', 'head-0-2', 'head-0-3', 'head-0-4', closed=True)
        self.add_arc('head-1-1', (24, 22), (27, 25), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-1-2', (27, 25), (24, 28), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-1-3', (24, 28), (21, 25), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-1-4', (21, 25), (24, 22), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head-1', 'head-1-1', 'head-1-2', 'head-1-3', 'head-1-4', closed=True)
        self.add_arc('head-2-1', (38, 22), (41, 25), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-2-2', (41, 25), (38, 28), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-2-3', (38, 28), (35, 25), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-2-4', (35, 25), (38, 22), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head-2', 'head-2-1', 'head-2-2', 'head-2-3', 'head-2-4', closed=True)
        self.add_bezier('shoulders-1', (4, 40), ((4, 36), (7, 36), (10, 36)))
        self.add_bezier('shoulders-2', (10, 36), ((13, 36), (15, 36), (17, 40)))
        self.add_bezier('shoulders-3', (17, 40), ((19, 36), (21, 36), (24, 36)))
        self.add_bezier('shoulders-4', (24, 36), ((27, 36), (29, 36), (31, 40)))
        self.add_bezier('shoulders-5', (31, 40), ((33, 36), (35, 36), (38, 36)))
        self.add_bezier('shoulders-6', (38, 36), ((41, 36), (44, 36), (44, 40)))
        self.add_contour('shoulders', 'shoulders-1', 'shoulders-2', 'shoulders-3', 'shoulders-4', 'shoulders-5', 'shoulders-6', closed=False)
