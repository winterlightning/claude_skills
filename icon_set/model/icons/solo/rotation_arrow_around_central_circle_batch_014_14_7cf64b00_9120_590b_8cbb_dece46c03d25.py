"""Circular Refresh Arrow.

Symbol plan: Open counterclockwise rotation arc with central pivot and a clear corner arrowhead.
Reduction: Smaller pivot creates clearance for a full-width arrowhead.
Construction reference: rotate-ccw: open lower-left quadrant and diagonal approach to corner arrowhead
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7cf64b00-9120-590b-8cbb-dece46c03d25'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/synchronize arrow 2_7cf64b00-9120-590b-8cbb-dece46c03d25.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/synchronize arrow 2_7cf64b00-9120-590b-8cbb-dece46c03d25.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-014/references/synchronize arrow 2_7cf64b00-9120-590b-8cbb-dece46c03d25.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'rotation-arrow-around-central-circle-batch-014-14'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('rotation', 'arrow', 'circle', 'refresh', 'pivot', 'interface')

    def build(self):
        self.add_arc('rotation-1', (6, 24), (24, 42), radius_x=18, radius_y=18, sweep=False)
        self.add_arc('rotation-2', (24, 42), (42, 24), radius_x=18, radius_y=18, sweep=False)
        self.add_arc('rotation-3', (42, 24), (24, 6), radius_x=18, radius_y=18, sweep=False)
        self.add_bezier('rotation-4', (24, 6), ((16, 6), (12, 10), (6, 16)))
        self.add_contour('rotation', 'rotation-1', 'rotation-2', 'rotation-3', 'rotation-4', closed=False)
        self.add_polyline('arrowhead', (6, 6), (6, 16), (16, 16), closed=False)
        self.relate("connect", 'rotation', 'arrowhead')
        self.add_arc('pivot-1', (24, 21), (27, 24), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('pivot-2', (27, 24), (24, 27), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('pivot-3', (24, 27), (21, 24), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('pivot-4', (21, 24), (24, 21), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('pivot', 'pivot-1', 'pivot-2', 'pivot-3', 'pivot-4', closed=True)
