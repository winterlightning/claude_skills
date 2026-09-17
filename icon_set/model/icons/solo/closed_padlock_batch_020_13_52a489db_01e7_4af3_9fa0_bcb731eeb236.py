from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '52a489db-01e7-4af3-9fa0-bcb731eeb236'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/lock_52a489db-01e7-4af3-9fa0-bcb731eeb236.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/references/lock_52a489db-01e7-4af3-9fa0-bcb731eeb236.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-020/13-closed-padlock-with-center-dot--52a489db-01e7-4af3-9fa0-bcb731eeb236.md'
DESIGN_PLAN = 'Rounded lock body with split upper edge for shackle attachment; shared arch radius.'
DESIGN_NOTES = []
CONSTRUCTION_REFERENCE = 'lock / lock-open: round body corners and arch.'

class BatchIcon(Solo48):
    icon_id = 'closed-padlock-batch-020-13'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('padlock', 'lock', 'closed', 'security', 'shackle', 'protection', 'safe', 'access')

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
        self.add_line('shackle-right', (32, 12), (32, 22))
        self.add_dot('center-dot',(24,33))
        self.relate("connect", 'body', 'shackle-left')
        self.relate("connect", 'body', 'shackle-right')
        self.relate("connect", 'shackle-left', 'shackle-arch')
        self.relate("connect", 'shackle-arch', 'shackle-right')
