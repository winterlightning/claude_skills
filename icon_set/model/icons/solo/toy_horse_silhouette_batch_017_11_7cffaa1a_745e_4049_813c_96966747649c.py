from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7cffaa1a-745e-4049-813c-96966747649c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/toys rocking horse 1_7cffaa1a-745e-4049-813c-96966747649c.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/references/toys rocking horse 1_7cffaa1a-745e-4049-813c-96966747649c.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/11-toy-rocking-horse--7cffaa1a-745e-4049-813c-96966747649c.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Short mane and tail omitted; wider neck keeps the horse silhouette open.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'toy-horse-silhouette-batch-017-11'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('horse', 'toy', 'pony', 'animal', 'silhouette', 'tail', 'legs', 'childhood')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('horse', (4, 18), (12, 8), (20, 12), (24, 24), (36, 24), (40, 28), (44, 40), (36, 40), (30, 32), (20, 32), (16, 40), (4, 40), (12, 28), (12, 20), closed=True)
