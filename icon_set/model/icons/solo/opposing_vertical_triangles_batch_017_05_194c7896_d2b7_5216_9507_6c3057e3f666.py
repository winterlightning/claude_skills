from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '194c7896-d2b7-5216-9507-6c3057e3f666'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/scroll vertical_194c7896-d2b7-5216-9507-6c3057e3f666.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/references/scroll vertical_194c7896-d2b7-5216-9507-6c3057e3f666.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/05-vertical-up-and-down-arrows--194c7896-d2b7-5216-9507-6c3057e3f666.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = []
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'opposing-vertical-triangles-batch-017-05'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('arrows', 'up', 'down', 'vertical', 'scroll', 'triangles')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('up', (24, 4), (40, 18), (8, 18), closed=True)
        self.add_polyline('down', (8, 30), (40, 30), (24, 44), closed=True)
