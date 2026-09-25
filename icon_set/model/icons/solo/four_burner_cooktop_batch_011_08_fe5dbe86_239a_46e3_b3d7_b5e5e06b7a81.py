"""Four Burner Stove Top.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Rounded cooktop with a two-by-two series of equal burner circles.
Reduction: Equalize burners to retain all four with certified clearance.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fe5dbe86-239a-46e3-b3d7-b5e5e06b7a81'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/cooktop_fe5dbe86-239a-46e3-b3d7-b5e5e06b7a81.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/cooktop_fe5dbe86-239a-46e3-b3d7-b5e5e06b7a81.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-011/references/cooktop_fe5dbe86-239a-46e3-b3d7-b5e5e06b7a81.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'four-burner-cooktop-batch-011-08'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('cooktop', 'stove', 'burners', 'kitchen', 'cooking', 'appliance')

    def build(self):
        self.add_line('cooktop-1', (10, 6), (38, 6))
        self.add_arc('cooktop-2', (38, 6), (42, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_line('cooktop-3', (42, 10), (42, 38))
        self.add_arc('cooktop-4', (42, 38), (38, 42), radius_x=4, radius_y=4, sweep=True)
        self.add_line('cooktop-5', (38, 42), (10, 42))
        self.add_arc('cooktop-6', (10, 42), (6, 38), radius_x=4, radius_y=4, sweep=True)
        self.add_line('cooktop-7', (6, 38), (6, 10))
        self.add_arc('cooktop-8', (6, 10), (10, 6), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('cooktop', 'cooktop-1', 'cooktop-2', 'cooktop-3', 'cooktop-4', 'cooktop-5', 'cooktop-6', 'cooktop-7', 'cooktop-8', closed=True)
        self.add_arc('burner-0-1', (17, 15), (19, 17), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('burner-0-2', (19, 17), (17, 19), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('burner-0-3', (17, 19), (15, 17), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('burner-0-4', (15, 17), (17, 15), radius_x=2, radius_y=2, sweep=True)
        self.add_contour('burner-0', 'burner-0-1', 'burner-0-2', 'burner-0-3', 'burner-0-4', closed=True)
        self.add_arc('burner-1-1', (31, 15), (33, 17), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('burner-1-2', (33, 17), (31, 19), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('burner-1-3', (31, 19), (29, 17), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('burner-1-4', (29, 17), (31, 15), radius_x=2, radius_y=2, sweep=True)
        self.add_contour('burner-1', 'burner-1-1', 'burner-1-2', 'burner-1-3', 'burner-1-4', closed=True)
        self.add_arc('burner-2-1', (17, 29), (19, 31), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('burner-2-2', (19, 31), (17, 33), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('burner-2-3', (17, 33), (15, 31), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('burner-2-4', (15, 31), (17, 29), radius_x=2, radius_y=2, sweep=True)
        self.add_contour('burner-2', 'burner-2-1', 'burner-2-2', 'burner-2-3', 'burner-2-4', closed=True)
        self.add_arc('burner-3-1', (31, 29), (33, 31), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('burner-3-2', (33, 31), (31, 33), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('burner-3-3', (31, 33), (29, 31), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('burner-3-4', (29, 31), (31, 29), radius_x=2, radius_y=2, sweep=True)
        self.add_contour('burner-3', 'burner-3-1', 'burner-3-2', 'burner-3-3', 'burner-3-4', closed=True)
