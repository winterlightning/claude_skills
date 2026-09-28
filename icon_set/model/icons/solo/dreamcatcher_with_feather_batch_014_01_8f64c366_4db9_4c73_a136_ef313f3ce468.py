"""Traditional Dreamcatcher with Feather.

SOLO48 visible bounds: (8, 2, 40, 46). Centerline extremes: (10, 4, 38, 44).

Symbol plan: Single circular web and long pointed feather beneath it.
Reduction: Omit duplicate ring and outer cords; enlarge feather for recognition.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f64c366-4db9-4c73-a136-ef313f3ce468'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hobbies/dreamcatcher_8f64c366-4db9-4c73-a136-ef313f3ce468.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/dreamcatcher_8f64c366-4db9-4c73-a136-ef313f3ce468.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-014/references/dreamcatcher_8f64c366-4db9-4c73-a136-ef313f3ce468.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'dreamcatcher-with-feather-batch-014-01'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hobbies"
    categories = ("primitives", "hobbies")
    aliases = ()
    keywords = ('dreamcatcher', 'feather', 'ring', 'cord', 'web', 'ornament')

    def build(self):
        self.add_arc('hoop-1', (24, 4), (38, 18), radius_x=14, radius_y=14, sweep=True)
        self.add_arc('hoop-2', (38, 18), (24, 32), radius_x=14, radius_y=14, sweep=True)
        self.add_arc('hoop-3', (24, 32), (10, 18), radius_x=14, radius_y=14, sweep=True)
        self.add_arc('hoop-4', (10, 18), (24, 4), radius_x=14, radius_y=14, sweep=True)
        self.add_contour('hoop', 'hoop-1', 'hoop-2', 'hoop-3', 'hoop-4', closed=True)
        self.add_line('web-h', (10, 18), (38, 18))
        self.add_line('web-v', (24, 4), (24, 32))
        self.relate("connect", 'hoop', 'web-h')
        self.relate("connect", 'hoop', 'web-v')
        self.relate("connect", 'web-h', 'web-v')
        self.add_bezier('feather-1', (24, 32), ((18, 34), (18, 36), (18, 38)))
        self.add_bezier('feather-2', (18, 38), ((18, 40), (22, 42), (24, 44)))
        self.add_bezier('feather-3', (24, 44), ((26, 42), (30, 40), (30, 38)))
        self.add_bezier('feather-4', (30, 38), ((30, 36), (30, 34), (24, 32)))
        self.add_contour('feather', 'feather-1', 'feather-2', 'feather-3', 'feather-4', closed=True)
        self.relate("connect", 'hoop', 'feather')
        self.relate("connect", 'web-v', 'feather')
