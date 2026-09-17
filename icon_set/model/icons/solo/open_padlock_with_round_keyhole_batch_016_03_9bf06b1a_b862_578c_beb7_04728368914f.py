from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9bf06b1a-b862-578c-beb7-04728368914f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/lock unlock_9bf06b1a-b862-578c-beb7-04728368914f.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/references/lock unlock_9bf06b1a-b862-578c-beb7-04728368914f.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/03-open-security-padlock--9bf06b1a-b862-578c-beb7-04728368914f.md'
DESIGN_PLAN = 'Rounded lock body with split upper edge for shackle attachment; shared arch radius.'
DESIGN_NOTES = ['Keyhole simplified to a round-ended slot to keep clearance.']
CONSTRUCTION_REFERENCE = 'lock / lock-open: round body corners and arch.'

class BatchIcon(Solo48):
    icon_id = 'open-padlock-with-round-keyhole-batch-016-03'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('padlock', 'unlock', 'open', 'keyhole', 'security', 'shackle')

    def build(self):
        # Rounded lock body with split upper edge for shackle attachment; shared arch radius.
        self.add_arc('corner-tr', (36, 22), (40, 26), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('right', (40, 26), (40, 40))
        self.add_arc('corner-br', (40, 40), (36, 44), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('bottom', (36, 44), (12, 44))
        self.add_arc('corner-bl', (12, 44), (8, 40), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('left', (8, 40), (8, 26))
        self.add_arc('corner-tl', (8, 26), (12, 22), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('top-part-0', (12, 22), (16, 22))
        self.add_line('top-part-1', (16, 22), (32, 22))
        self.add_line('top-part-2', (32, 22), (36, 22))
        self.add_contour('body', 'top-part-0', 'top-part-1', 'top-part-2', 'corner-tr', 'right', 'corner-br', 'bottom', 'corner-bl', 'left', 'corner-tl', closed=True)
        self.add_line('shackle-left', (16, 22), (16, 12))
        self.add_arc('shackle-arch', (16, 12), (32, 12), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_line('keyhole', (24, 31), (24, 35))
        self.relate("connect", 'body', 'shackle-left')
        self.relate("connect", 'shackle-left', 'shackle-arch')
