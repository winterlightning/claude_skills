from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '787783f6-901a-45ae-a710-84ce8a165876'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/drop bottle_787783f6-901a-45ae-a710-84ce8a165876.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/references/drop bottle_787783f6-901a-45ae-a710-84ce8a165876.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/06-baby-bottle--787783f6-901a-45ae-a710-84ce8a165876.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Nipple shoulder simplified; neck seam remains.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'baby-feeding-bottle-batch-019-06'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    keywords = ('baby', 'bottle', 'feeding', 'nipple', 'teat', 'milk', 'infant', 'nursery')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('nipple', (10, 18), (18, 12), (18, 4), (30, 4), (30, 12), (38, 18), closed=False)
        self.add_polyline('body', (10, 18), (38, 18), (38, 40), (34, 44), (14, 44), (10, 40), closed=True)
        self.relate("connect", 'nipple', 'body')
