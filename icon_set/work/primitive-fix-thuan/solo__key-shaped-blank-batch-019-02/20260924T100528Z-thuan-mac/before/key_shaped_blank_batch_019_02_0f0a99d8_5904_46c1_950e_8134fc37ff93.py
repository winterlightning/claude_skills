from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f0a99d8-5904-46c1-950e-8134fc37ff93'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/key 2_0f0a99d8-5904-46c1-950e-8134fc37ff93.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/references/key 2_0f0a99d8-5904-46c1-950e-8134fc37ff93.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/02-angled-pointer-indicator--0f0a99d8-5904-46c1-950e-8134fc37ff93.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Key blank remains toothless; tiny source dot omitted.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'key-shaped-blank-batch-019-02'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('key', 'blank', 'bow', 'shaft', 'diagonal', 'tool', 'lock', 'silhouette')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('bow-bottom', (34, 28), (6, 28), radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('bow-top', (6, 28), (20, 14), radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_line('shaft-part-0', (20, 14), (26, 16))
        self.add_line('shaft-part-1', (26, 16), (36, 6))
        self.add_line('shaft-part-2', (36, 6), (42, 6))
        self.add_line('shaft-part-3', (42, 6), (42, 16))
        self.add_line('shaft-part-4', (42, 16), (34, 28))
        self.add_contour('key', 'bow-bottom', 'bow-top', 'shaft-part-0', 'shaft-part-1', 'shaft-part-2', 'shaft-part-3', 'shaft-part-4', closed=True)
