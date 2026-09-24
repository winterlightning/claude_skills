from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a11ecc5-12d2-479f-ad50-bf72f2730e09'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/repeat_0a11ecc5-12d2-479f-ad50-bf72f2730e09.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/references/repeat_0a11ecc5-12d2-479f-ad50-bf72f2730e09.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/03-circular-refresh-arrows--0a11ecc5-12d2-479f-ad50-bf72f2730e09.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Two opposing arcs preserve rotation; arrowheads remain at diagonal ends.', 'Counterclockwise direction requires mirrored arrow traversal.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'counterclockwise-circular-refresh-arrows-batch-020-03'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('refresh', 'repeat', 'arrows', 'counterclockwise', 'circle', 'loop', 'rotation', 'sync')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('upper', (40, 12), (8, 36), radius_x=20, radius_y=20, sweep=False, large_arc=False)
        self.add_arc('lower', (8, 36), (40, 12), radius_x=20, radius_y=20, sweep=False, large_arc=False)
        self.add_polyline('head-left', (8, 24), (8, 36), (20, 36), closed=False)
        self.add_polyline('head-right', (28, 12), (40, 12), (40, 24), closed=False)
        self.relate("connect", 'upper', 'lower')
        self.relate("connect", 'upper', 'head-left')
        self.relate("connect", 'upper', 'head-right')
        self.relate("connect", 'lower', 'head-left')
        self.relate("connect", 'lower', 'head-right')
