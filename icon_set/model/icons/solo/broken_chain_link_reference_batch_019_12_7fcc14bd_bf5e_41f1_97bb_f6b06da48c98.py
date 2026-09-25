from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7fcc14bd-bf5e-41f1-97bb-f6b06da48c98'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/disconnect_7fcc14bd-bf5e-41f1-97bb-f6b06da48c98.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/references/disconnect_7fcc14bd-bf5e-41f1-97bb-f6b06da48c98.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/12-broken-chain-link--7fcc14bd-bf5e-41f1-97bb-f6b06da48c98.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Two break rays retained; third ray removed for spacing.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'broken-chain-link-reference-batch-019-12'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("symbol", "state", "other", "primitives-generate")
    keywords = ('chain', 'link', 'broken', 'disconnect', 'unlink', 'gap', 'break', 'connection')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('lower-hook', (16, 24), (6, 34), (6, 38), (10, 42), (16, 42), (26, 32), closed=False)
        self.add_polyline('upper-hook', (24, 16), (34, 6), (38, 6), (42, 10), (42, 16), (32, 26), closed=False)
        self.add_line('ray1', (6, 16), (10, 16))
        self.add_line('ray2', (16, 6), (16, 10))
