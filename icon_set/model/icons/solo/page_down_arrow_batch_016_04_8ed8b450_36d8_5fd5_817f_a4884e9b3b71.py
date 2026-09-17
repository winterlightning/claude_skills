from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ed8b450-36d8-5fd5-817f-a4884e9b3b71'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/keyboard page down_8ed8b450-36d8-5fd5-817f-a4884e9b3b71.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/references/keyboard page down_8ed8b450-36d8-5fd5-817f-a4884e9b3b71.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/04-page-down-navigation-arrow--8ed8b450-36d8-5fd5-817f-a4884e9b3b71.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = []
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'page-down-arrow-batch-016-04'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('page', 'down', 'arrow', 'keyboard', 'navigation', 'crossbars')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('shaft', (24, 4), (24, 16), (24, 24), (24, 44), closed=False)
        self.add_polyline('bar-16', (14, 16), (24, 16), (34, 16), closed=False)
        self.add_polyline('bar-24', (14, 24), (24, 24), (34, 24), closed=False)
        self.add_polyline('head', (8, 28), (24, 44), (40, 28), closed=False)
        self.relate("connect", 'shaft', 'bar-16')
        self.relate("connect", 'shaft', 'bar-24')
        self.relate("connect", 'shaft', 'head')
