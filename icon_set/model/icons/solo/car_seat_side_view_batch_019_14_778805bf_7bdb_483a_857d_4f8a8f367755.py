from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '778805bf-7bdb-483a-857d-4f8a8f367755'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/seat car_778805bf-7bdb-483a-857d-4f8a8f367755.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/references/seat car_778805bf-7bdb-483a-857d-4f8a8f367755.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/14-car-seat-side-view--778805bf-7bdb-483a-857d-4f8a8f367755.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['One padded side profile; deliberate asymmetric back and cushion.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'car-seat-side-view-batch-019-14'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('seat', 'car', 'chair', 'cushion', 'backrest', 'vehicle', 'interior', 'seating')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('seat', (6, 6), (6, 28), (10, 38), (18, 42), (38, 42), (42, 38), (42, 34), (38, 30), (24, 30), (18, 24), (14, 6), closed=True)
