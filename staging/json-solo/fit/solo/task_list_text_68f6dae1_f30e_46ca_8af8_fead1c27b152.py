"""Task list text (office), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68f6dae1-f30e-46ca-8af8-fead1c27b152'
SOURCE_PATH = 'icons-json/office/task list text_68f6dae1-f30e-46ca-8af8-fead1c27b152.json'
AUTHOR = 'json_to_solo'

class TaskListTextOffice(Solo48):
    icon_id = 'task-list-text-office'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('task', 'list', 'text', 'office')

    def build(self):
        self.add_line('e0', (13, 15), (35, 15))
        self.add_line('e1', (13, 22), (35, 22))
        self.add_line('e2', (13, 31), (30, 31))
        self.add_line('e3', (40, 42), (8, 42))
        self.add_line('e4', (6, 40), (6, 8))
        self.add_line('e5', (8, 6), (40, 6))
        self.add_line('e6', (42, 8), (42, 40))
        self.add_arc('e7', (8, 42), (6, 40), radius_x=4)
        self.add_line('e8', (6, 8), (8, 6))
        self.add_line('e9', (40, 6), (42, 8))
        self.add_line('e10', (42, 40), (40, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', 'e6', 'e10', closed=True)
