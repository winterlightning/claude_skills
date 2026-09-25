"""Japanese Dango Rice Dumplings Skewer.

Symbol plan: Three equal dumplings on one diagonal skewer; shafts end at shared 3-4-5 circle points.
Reduction: Space dumplings along an exposed skewer instead of letting their outlines crowd.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c1f111a2-448d-5b0c-a1a7-7f8feffca82b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/japanese sweets dango on stick_c1f111a2-448d-5b0c-a1a7-7f8feffca82b.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/japanese sweets dango on stick_c1f111a2-448d-5b0c-a1a7-7f8feffca82b.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-012/references/japanese sweets dango on stick_c1f111a2-448d-5b0c-a1a7-7f8feffca82b.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'dango-skewer-batch-012-02'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('dango', 'skewer', 'dumpling', 'sweet', 'japanese', 'food')

    def build(self):
        self.add_arc('dumpling-0-1', (16, 35), (17, 42), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('dumpling-0-2', (17, 42), (10, 43), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('dumpling-0-3', (10, 43), (9, 36), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('dumpling-0-4', (9, 36), (16, 35), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('dumpling-0', 'dumpling-0-1', 'dumpling-0-2', 'dumpling-0-3', 'dumpling-0-4', closed=True)
        self.add_arc('dumpling-1-1', (25, 23), (26, 30), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('dumpling-1-2', (26, 30), (19, 31), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('dumpling-1-3', (19, 31), (18, 24), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('dumpling-1-4', (18, 24), (25, 23), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('dumpling-1', 'dumpling-1-1', 'dumpling-1-2', 'dumpling-1-3', 'dumpling-1-4', closed=True)
        self.add_arc('dumpling-2-1', (34, 11), (35, 18), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('dumpling-2-2', (35, 18), (28, 19), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('dumpling-2-3', (28, 19), (27, 12), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('dumpling-2-4', (27, 12), (34, 11), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('dumpling-2', 'dumpling-2-1', 'dumpling-2-2', 'dumpling-2-3', 'dumpling-2-4', closed=True)
        self.add_line('stick-0', (16, 35), (19, 31))
        self.add_line('stick-1', (25, 23), (28, 19))
        self.add_line('tip', (34, 11), (40, 4))
        self.relate("connect", 'dumpling-0', 'stick-0')
        self.relate("connect", 'dumpling-1', 'stick-0')
        self.relate("connect", 'dumpling-1', 'stick-1')
        self.relate("connect", 'dumpling-2', 'stick-1')
        self.relate("connect", 'dumpling-2', 'tip')
