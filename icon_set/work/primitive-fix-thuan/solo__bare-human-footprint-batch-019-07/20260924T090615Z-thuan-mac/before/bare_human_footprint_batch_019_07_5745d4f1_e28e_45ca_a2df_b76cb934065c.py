from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5745d4f1-e28e-45ca-a2df-b76cb934065c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/foot_5745d4f1-e28e-45ca-a2df-b76cb934065c.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/references/foot_5745d4f1-e28e-45ca-a2df-b76cb934065c.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/07-bare-human-footprint--5745d4f1-e28e-45ca-a2df-b76cb934065c.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Four toe lobes preserve big-toe hierarchy; smallest toe omitted.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'bare-human-footprint-batch-019-07'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('foot', 'footprint', 'sole', 'toes', 'heel', 'barefoot', 'human', 'track')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('heel', (30, 34), (10, 34), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('big-toe', (10, 9), (20, 9), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('toe2', (20, 9), (28, 9), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('toe3', (28, 13), (36, 13), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('toe-step', (28, 9), (28, 13))
        self.add_arc('little-toe', (36, 13), (38, 15), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_line('outer-toe', (38, 15), (38, 19))
        self.add_line('arch-part-0', (10, 34), (14, 24))
        self.add_line('arch-part-1', (14, 24), (10, 14))
        self.add_line('arch-part-2', (10, 14), (10, 9))
        self.add_line('outer-part-0', (38, 19), (34, 28))
        self.add_line('outer-part-1', (34, 28), (30, 34))
        self.add_contour('foot', 'heel', 'arch-part-0', 'arch-part-1', 'arch-part-2', 'big-toe', 'toe2', 'toe-step', 'toe3', 'little-toe', 'outer-toe', 'outer-part-0', 'outer-part-1', closed=True)
