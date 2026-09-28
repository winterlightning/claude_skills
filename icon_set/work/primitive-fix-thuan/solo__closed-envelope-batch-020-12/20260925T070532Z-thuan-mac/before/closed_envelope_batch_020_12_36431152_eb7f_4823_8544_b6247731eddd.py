from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '36431152-eb7f-4823-8544-b6247731eddd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mail_36431152-eb7f-4823-8544-b6247731eddd.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/references/mail_36431152-eb7f-4823-8544-b6247731eddd.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/12-closed-mail-envelope--36431152-eb7f-4823-8544-b6247731eddd.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = []
CONSTRUCTION_REFERENCE = 'mail: attached diagonal flap and broad envelope body.'

class BatchIcon(Solo48):
    icon_id = 'closed-envelope-batch-020-12'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('envelope', 'mail', 'letter', 'message', 'post', 'correspondence', 'stationery', 'closed')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('envelope', (4, 10), (44, 10), (44, 34), (40, 38), (8, 38), (4, 34), closed=True)
        self.add_polyline('flap', (4, 10), (24, 26), (44, 10), closed=False)
        self.relate("connect", 'envelope', 'flap')
