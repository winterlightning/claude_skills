from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1e26ac1b-672a-5b59-a650-b299e22cc422'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/check_1e26ac1b-672a-5b59-a650-b299e22cc422.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/references/check_1e26ac1b-672a-5b59-a650-b299e22cc422.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/02-verification-check-mark-symbol--1e26ac1b-672a-5b59-a650-b299e22cc422.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = []
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'outlined-check-mark-batch-017-02'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    keywords = ('check', 'tick', 'verify', 'confirm', 'success', 'mark')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('outline', (4, 24), (12, 16), (20, 24), (36, 8), (44, 16), (20, 40), closed=True)
