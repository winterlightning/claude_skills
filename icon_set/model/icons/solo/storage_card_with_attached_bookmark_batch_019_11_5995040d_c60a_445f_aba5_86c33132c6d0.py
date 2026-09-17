from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5995040d-c60a-445f-aba5-86c33132c6d0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/data tag_5995040d-c60a-445f-aba5-86c33132c6d0.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/references/data tag_5995040d-c60a-445f-aba5-86c33132c6d0.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/11-bookmarked-storage-card--5995040d-c60a-445f-aba5-86c33132c6d0.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Lower contact marks removed because the remaining strip is only 12 centerline units tall.', 'Two contact marks and attached ribbon preserved.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'storage-card-with-attached-bookmark-batch-019-11'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('card', 'storage', 'bookmark', 'ribbon', 'data', 'memory', 'tag', 'marked')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('card', (8, 4), (16, 4), (28, 4), (32, 4), (40, 12), (40, 32), (40, 44), (8, 44), (8, 32), closed=True)
        self.add_polyline('ribbon', (16, 4), (16, 20), (22, 16), (28, 20), (28, 4), closed=False)
        self.add_line('divider', (8, 32), (40, 32))
        self.relate("connect", 'card', 'ribbon')
        self.relate("connect", 'card', 'divider')
