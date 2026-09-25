"""Electric Slow Cooker Appliance.

SOLO48 visible bounds: (2, 6, 46, 42). Centerline extremes: (4, 8, 44, 40).

Symbol plan: Pot and domed lid share rim nodes; central dial.
Reduction: Simplify feet and lid knob into short external stems.
Construction reference: cooking-pot: shared rim, rounded lower corners
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84ea8179-ecd2-5ac3-8140-a585e67f26c1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/appliances slow cooker_84ea8179-ecd2-5ac3-8140-a585e67f26c1.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/appliances slow cooker_84ea8179-ecd2-5ac3-8140-a585e67f26c1.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-011/references/appliances slow cooker_84ea8179-ecd2-5ac3-8140-a585e67f26c1.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'electric-slow-cooker-batch-011-03'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('slow', 'cooker', 'pot', 'appliance', 'kitchen', 'cooking')

    def build(self):
        self.add_line('pot-1', (4, 18), (8, 34))
        self.add_bezier('pot-2', (8, 34), ((9, 39), (13, 40), (16, 40)))
        self.add_line('pot-3', (16, 40), (32, 40))
        self.add_bezier('pot-4', (32, 40), ((35, 40), (39, 39), (40, 34)))
        self.add_line('pot-5', (40, 34), (44, 18))
        self.add_line('pot-close', (44, 18), (4, 18))
        self.add_contour('pot', 'pot-1', 'pot-2', 'pot-3', 'pot-4', 'pot-5', 'pot-close', closed=True)
        self.add_bezier('lid-1', (4, 18), ((8, 10), (16, 8), (24, 8)))
        self.add_bezier('lid-2', (24, 8), ((32, 8), (40, 10), (44, 18)))
        self.add_contour('lid', 'lid-1', 'lid-2', closed=False)
        self.relate("connect", 'pot', 'lid')
        self.add_arc('dial-1', (24, 27), (26, 29), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('dial-2', (26, 29), (24, 31), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('dial-3', (24, 31), (22, 29), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('dial-4', (22, 29), (24, 27), radius_x=2, radius_y=2, sweep=True)
        self.add_contour('dial', 'dial-1', 'dial-2', 'dial-3', 'dial-4', closed=True)
