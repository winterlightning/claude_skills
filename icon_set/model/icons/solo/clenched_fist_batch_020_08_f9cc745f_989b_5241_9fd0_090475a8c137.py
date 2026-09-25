from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9cc745f-989b-5241-9fd0-090475a8c137'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/hand fist bump_f9cc745f-989b-5241-9fd0-090475a8c137.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/references/hand fist bump_f9cc745f-989b-5241-9fd0-090475a8c137.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/08-clenched-hand-fist--f9cc745f-989b-5241-9fd0-090475a8c137.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Lower finger seam and palm curve omitted to retain an open fist interior.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'clenched-fist-batch-020-08'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    keywords = ('hand', 'fist', 'clenched', 'gesture', 'knuckles', 'fingers', 'arm', 'bump')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('outline', (4, 16), (12, 16), (20, 8), (36, 8), (44, 12), (44, 20), (44, 30), (44, 36), (40, 40), (18, 40), (10, 34), (4, 34), closed=False)
        self.add_polyline('thumb', (20, 8), (24, 18), (32, 22), (36, 18), closed=False)
        self.add_line('finger3', (30, 30), (44, 30))
        self.relate("connect", 'outline', 'thumb')
        self.relate("connect", 'outline', 'finger3')
