from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f6e5bd8a-5088-4e44-940d-be3c568ff2da'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/sunbed_f6e5bd8a-5088-4e44-940d-be3c568ff2da.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/references/sunbed_f6e5bd8a-5088-4e44-940d-be3c568ff2da.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/08-beach-sun-lounger--f6e5bd8a-5088-4e44-940d-be3c568ff2da.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Intentional side-view asymmetry; back rises to the right.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'reclining-sun-lounger-batch-019-08'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    keywords = ('lounger', 'chair', 'sunbed', 'beach', 'recliner', 'seat', 'furniture', 'leisure')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('seat', (4, 28), (12, 28), (32, 28), (44, 8), closed=False)
        self.add_line('front-leg', (12, 28), (6, 40))
        self.add_line('rear-leg', (32, 28), (40, 40))
        self.relate("connect", 'seat', 'front-leg')
        self.relate("connect", 'seat', 'rear-leg')
