"""Person Reacting to Extreme Spice.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Open circular face emits flame upper-left; detached shoulder arch below.
Reduction: Reduce X eye to one dot; keep flame reaction. Human reference: human_ref/user.svg; head lower edge y=28, shoulders top y=36 gives 4 ink gap.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8b9fd40e-030d-4023-801b-5cc4a7e68ec9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/spicy weakness person very spicy level_8b9fd40e-030d-4023-801b-5cc4a7e68ec9.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/spicy weakness person very spicy level_8b9fd40e-030d-4023-801b-5cc4a7e68ec9.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-012/references/spicy weakness person very spicy level_8b9fd40e-030d-4023-801b-5cc4a7e68ec9.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'person-reacting-to-spicy-food-batch-012-06'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('person', 'spicy', 'flame', 'face', 'food', 'reaction')

    def build(self):
        self.add_bezier('head-1', (27, 8), ((36, 8), (42, 12), (42, 18)))
        self.add_arc('head-2', (42, 18), (32, 28), radius_x=10, radius_y=10, sweep=True)
        self.add_bezier('head-3', (32, 28), ((26, 28), (22, 24), (22, 19)))
        self.add_contour('head', 'head-1', 'head-2', 'head-3', closed=False)
        self.add_bezier('flame-1', (12, 6), ((10, 13), (6, 13), (6, 18)))
        self.add_bezier('flame-2', (6, 18), ((6, 24), (14, 24), (14, 18)))
        self.add_bezier('flame-3', (14, 18), ((14, 14), (14, 13), (12, 6)))
        self.add_contour('flame', 'flame-1', 'flame-2', 'flame-3', closed=True)
        self.add_dot('eye', (32, 17))
        self.add_bezier('shoulders-1', (16, 42), ((16, 38), (23, 36), (29, 36)))
        self.add_bezier('shoulders-2', (29, 36), ((35, 36), (42, 38), (42, 42)))
        self.add_contour('shoulders', 'shoulders-1', 'shoulders-2', closed=False)
