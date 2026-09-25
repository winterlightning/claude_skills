from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b142e96-a7ca-4d29-b690-c751a7da7802'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/cursor left 2_1b142e96-a7ca-4d29-b690-c751a7da7802.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/references/cursor left 2_1b142e96-a7ca-4d29-b690-c751a7da7802.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/15-computer-mouse-arrow-cursor--1b142e96-a7ca-4d29-b690-c751a7da7802.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = []
CONSTRUCTION_REFERENCE = 'mouse-pointer-2: deliberate angular silhouette and two notches.'

class BatchIcon(Solo48):
    icon_id = 'arrow-cursor-batch-020-15'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    keywords = ('cursor', 'pointer', 'arrow', 'mouse', 'computer', 'select', 'diagonal', 'interface')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('pointer', (6, 6), (42, 18), (30, 24), (42, 36), (36, 42), (24, 30), (18, 42), closed=True)
