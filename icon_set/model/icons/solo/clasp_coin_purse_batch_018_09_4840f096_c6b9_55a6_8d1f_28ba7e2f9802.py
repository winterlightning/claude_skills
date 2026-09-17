from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4840f096-c6b9-55a6-8d1f-28ba7e2f9802'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/money/coin purse_4840f096-c6b9-55a6-8d1f-28ba7e2f9802.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/references/coin purse_4840f096-c6b9-55a6-8d1f-28ba7e2f9802.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/09-classic-small-coin-purse--4840f096-c6b9-55a6-8d1f-28ba7e2f9802.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Double rim reduced to one structural seam; paired clasp retained.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'clasp-coin-purse-batch-018-09'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('purse', 'coin', 'clasp', 'wallet', 'pouch', 'money', 'accessory', 'bag')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('purse', (12, 18), (36, 18), (44, 32), (44, 36), (40, 40), (8, 40), (4, 36), (4, 32), closed=True)
        self.add_polyline('clasp-left', (16, 18), (16, 8), (24, 8), (24, 18), closed=False)
        self.add_polyline('clasp-right', (24, 18), (24, 8), (32, 8), (32, 18), closed=False)
        self.relate("connect", 'clasp-left', 'clasp-right')
