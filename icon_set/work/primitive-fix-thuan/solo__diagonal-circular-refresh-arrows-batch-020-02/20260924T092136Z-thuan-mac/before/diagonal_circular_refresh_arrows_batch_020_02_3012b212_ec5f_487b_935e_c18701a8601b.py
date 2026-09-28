from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3012b212-ec5f-487b-935e-c18701a8601b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/arrows spin_3012b212-ec5f-487b-935e-c18701a8601b.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/references/arrows spin_3012b212-ec5f-487b-935e-c18701a8601b.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/02-circular-refresh-arrows--3012b212-ec5f-487b-935e-c18701a8601b.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Two opposing arcs preserve rotation; arrowheads remain at diagonal ends.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'diagonal-circular-refresh-arrows-batch-020-02'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('refresh', 'repeat', 'arrows', 'circle', 'clockwise', 'loop', 'rotation', 'sync')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('upper', (4, 24), (36, 8), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_arc('lower', (44, 24), (12, 40), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_polyline('head-upper', (26, 8), (36, 8), (36, 18), closed=False)
        self.add_polyline('head-lower', (22, 40), (12, 40), (12, 30), closed=False)
        self.relate("connect", 'upper', 'head-upper')
        self.relate("connect", 'lower', 'head-lower')
