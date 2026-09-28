from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dfb60b37-8f2a-452c-872d-06287e677376'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/expand vertical 2_dfb60b37-8f2a-452c-872d-06287e677376.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/references/expand vertical 2_dfb60b37-8f2a-452c-872d-06287e677376.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/03-vertical-expansion-and-resize--dfb60b37-8f2a-452c-872d-06287e677376.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Shafts attached to their arrowheads to preserve legibility at 48px.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'outward-arrows-from-horizontal-divider-batch-017-03'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    keywords = ('arrows', 'expand', 'vertical', 'divider', 'outward', 'resize')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('top-head', (8, 16), (24, 4), (40, 16), closed=False)
        self.add_line('top-shaft', (24, 4), (24, 16))
        self.add_line('divider', (8, 24), (40, 24))
        self.add_polyline('bottom-head', (8, 32), (24, 44), (40, 32), closed=False)
        self.add_line('bottom-shaft', (24, 32), (24, 44))
        self.relate("connect", 'top-head', 'top-shaft')
        self.relate("connect", 'bottom-head', 'bottom-shaft')
