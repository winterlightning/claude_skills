"""High Temperature Thermometer.

SOLO48 visible bounds: (6, 2, 42, 46). Centerline extremes: (8, 4, 40, 44).

Symbol plan: Thermometer tube and circular bulb, three equal scale marks.
Reduction: Omit inner mercury stem and circle because the tube cannot contain another stroke with legal clearance.
Construction reference: thermometer: round bulb and parallel tube
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1fa52957-1342-499f-9403-f3293476b96f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/temperature thermometer high_1fa52957-1342-499f-9403-f3293476b96f.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/temperature thermometer high_1fa52957-1342-499f-9403-f3293476b96f.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-011/references/temperature thermometer high_1fa52957-1342-499f-9403-f3293476b96f.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'high-temperature-thermometer-reference-batch-011-13'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('thermometer', 'temperature', 'heat', 'scale', 'measurement', 'bulb')

    def build(self):
        self.add_line('outline-1', (12, 28), (12, 10))
        self.add_arc('outline-2', (12, 10), (24, 10), radius_x=6, radius_y=6, sweep=True)
        self.add_line('outline-3', (24, 10), (24, 28))
        self.add_bezier('outline-4', (24, 28), ((28, 30), (28, 34), (28, 36)))
        self.add_arc('outline-5', (28, 36), (8, 36), radius_x=10, radius_y=8, sweep=True)
        self.add_bezier('outline-6', (8, 36), ((8, 32), (8, 30), (12, 28)))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', closed=True)
        self.add_line('tick-0', (36, 8), (40, 8))
        self.add_line('tick-1', (36, 18), (40, 18))
        self.add_line('tick-2', (36, 28), (40, 28))
