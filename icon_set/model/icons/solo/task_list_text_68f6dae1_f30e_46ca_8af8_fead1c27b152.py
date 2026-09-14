'Task list: three straight baselines with even 9-unit spacing and balanced margins.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68f6dae1-f30e-46ca-8af8-fead1c27b152'
SOURCE_PATH = 'icons-json/office/task list text_68f6dae1-f30e-46ca-8af8-fead1c27b152.json'
AUTHOR = 'gpt-6'

class TaskListText(Solo48):
    icon_id = 'task-list-text'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('task', 'list', 'text', 'office')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('page-0', (9, 6), (39, 6))
        self.add_arc('page-1', (39, 6), (42, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('page-2', (42, 9), (42, 39))
        self.add_arc('page-3', (42, 39), (39, 42), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('page-4', (39, 42), (9, 42))
        self.add_arc('page-5', (9, 42), (6, 39), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('page-6', (6, 39), (6, 9))
        self.add_arc('page-7', (6, 9), (9, 6), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('text-15', (15, 15), (33, 15))
        self.add_line('text-24', (15, 24), (33, 24))
        self.add_line('text-33', (15, 33), (27, 33))
        self.add_contour('page', *('page-0', 'page-1', 'page-2', 'page-3', 'page-4', 'page-5', 'page-6', 'page-7'), closed=True)
