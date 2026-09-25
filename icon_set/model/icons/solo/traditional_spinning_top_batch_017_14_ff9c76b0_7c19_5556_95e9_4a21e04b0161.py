from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ff9c76b0-7c19-5556-95e9-4a21e04b0161'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/spinning top_ff9c76b0-7c19-5556-95e9-4a21e04b0161.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/references/spinning top_ff9c76b0-7c19-5556-95e9-4a21e04b0161.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/14-traditional-spinning-top-toy--ff9c76b0-7c19-5556-95e9-4a21e04b0161.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = []
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'traditional-spinning-top-batch-017-14'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "kids"
    keywords = ('top', 'spinning', 'toy', 'spindle', 'grip', 'symmetrical', 'play', 'traditional')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('top', (8, 22), (24, 12), (40, 22), (40, 30), (24, 40), (8, 30), closed=True)
        self.add_line('handle', (24, 4), (24, 12))
        self.add_line('spindle', (24, 40), (24, 44))
        self.add_line('band-top', (8, 22), (40, 22))
        self.add_line('band-bottom', (8, 30), (40, 30))
        self.relate("connect", 'top', 'handle')
        self.relate("connect", 'top', 'spindle')
        self.relate("connect", 'top', 'band-top')
        self.relate("connect", 'top', 'band-bottom')
