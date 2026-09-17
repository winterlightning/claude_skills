from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac9f5eb0-9ca6-4ae8-b650-3216bba2d023'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/bird print_ac9f5eb0-9ca6-4ae8-b650-3216bba2d023.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/references/bird print_ac9f5eb0-9ca6-4ae8-b650-3216bba2d023.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/10-bird-footprint-symbol--ac9f5eb0-9ca6-4ae8-b650-3216bba2d023.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = []
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'bird-footprint-batch-019-10'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('bird', 'footprint', 'track', 'toes', 'avian', 'print', 'claw', 'animal')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('stem', (24, 4), (24, 28), (24, 44), closed=False)
        self.add_polyline('toes', (8, 16), (24, 28), (40, 16), closed=False)
        self.relate("connect", 'stem', 'toes')
