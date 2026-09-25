from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc9c205a-fa2d-425c-ad9c-0ff1e334f886'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/wallet_fc9c205a-fa2d-425c-ad9c-0ff1e334f886.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/references/wallet_fc9c205a-fa2d-425c-ad9c-0ff1e334f886.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/06-classic-personal-money-wallet--fc9c205a-fa2d-425c-ad9c-0ff1e334f886.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Fastener dot omitted because tab interior is too small.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'wallet-batch-020-06'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    keywords = ('wallet', 'money', 'pocket', 'cash', 'accessory', 'leather', 'purse', 'payment')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('wallet', (12, 4), (36, 4), (40, 8), (40, 22), (40, 34), (40, 40), (36, 44), (12, 44), (8, 40), (8, 8), closed=True)
        self.add_polyline('tab', (40, 22), (26, 22), (22, 26), (22, 30), (26, 34), (40, 34), closed=False)
        self.add_line('pocket', (16, 13), (31, 13))
        self.relate("connect", 'wallet', 'tab')
