from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '31a89d48-62e9-4297-8d54-47541920c9cc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__opposing-bent-transfer-arrows-batch-017-01/20260927T153322Z-thuan-mac-1/reference/refresh_31a89d48-62e9-4297-8d54-47541920c9cc.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/references/refresh_31a89d48-62e9-4297-8d54-47541920c9cc.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/01-up-and-down-data-transfer-arrows--31a89d48-62e9-4297-8d54-47541920c9cc.md'
DESIGN_PLAN = 'Two opposing arrows share vertical travel and mirror their turns.'
DESIGN_NOTES = []
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'opposing-bent-transfer-arrows-batch-017-01'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    keywords = ('arrows', 'transfer', 'up', 'down', 'refresh', 'exchange')

    def build(self):
        # Long straight shafts and squared opposing bends match the source more closely.
        self.add_polyline('up-head', (6,16), (16,6), (24,16))
        self.add_polyline('up-shaft', (16,6), (16,34), (8,34))
        self.add_polyline('down-head', (24,32), (32,42), (42,32))
        self.add_polyline('down-shaft', (32,42), (32,14), (40,14))
        self.relate('connect','up-head','up-shaft')
        self.relate('connect','down-head','down-shaft')
