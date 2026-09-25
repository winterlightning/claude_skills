from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35b2e33d-7f76-56bf-a387-22ca75647071'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/money/piggy_35b2e33d-7f76-56bf-a387-22ca75647071.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/references/piggy_35b2e33d-7f76-56bf-a387-22ca75647071.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/10-piggy-bank-with-coin--35b2e33d-7f76-56bf-a387-22ca75647071.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Coin separated above the bank instead of overlapping its slot. Tail and denomination omitted.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'piggy-bank-receiving-coin-batch-018-10'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "money"
    keywords = ('piggy', 'bank', 'coin', 'saving', 'money', 'deposit', 'pig', 'finance')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('coin-0', (23, 11), (28, 6), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('coin-1', (28, 6), (33, 11), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('coin-2', (33, 11), (28, 16), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('coin-3', (28, 16), (23, 11), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('coin', 'coin-0', 'coin-1', 'coin-2', 'coin-3', closed=True)
        self.add_polyline('pig', (6, 26), (12, 26), (12, 18), (20, 26), (34, 26), (42, 30), (42, 38), (38, 38), (38, 42), (30, 42), (30, 38), (20, 38), (20, 42), (12, 42), (12, 34), (6, 34), closed=True)
