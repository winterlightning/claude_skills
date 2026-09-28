from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9d3425c4-0090-4fdf-b40b-9f93695f8ca8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/adjustable_9d3425c4-0090-4fdf-b40b-9f93695f8ca8.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/references/adjustable_9d3425c4-0090-4fdf-b40b-9f93695f8ca8.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/15-adjustable-curved-indicator--9d3425c4-0090-4fdf-b40b-9f93695f8ca8.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Open arch and angled right-hand indicator; no numeric scale.', 'Pointer joins the right-hand end of the gauge, avoiding an ambiguous crossing.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'curved-gauge-indicator-batch-018-15'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('gauge', 'arc', 'indicator', 'adjustable', 'dial', 'measure', 'curve', 'pointer')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('gauge-left', (4, 40), (24, 8), radius_x=20, radius_y=32, sweep=True, large_arc=False)
        self.add_arc('gauge-right', (24, 8), (44, 40), radius_x=20, radius_y=32, sweep=True, large_arc=False)
        self.add_polyline('pointer', (32, 40), (44, 40), (44, 26), closed=False)
        self.relate("connect", 'gauge-left', 'gauge-right')
        self.relate("connect", 'gauge-right', 'pointer')
