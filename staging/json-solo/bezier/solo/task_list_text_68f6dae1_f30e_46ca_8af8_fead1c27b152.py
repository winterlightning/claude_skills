"""Task list text (office), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e7', (8, 42), ((7.804, 41.926), (8.062, 41.951), (7.874, 41.845)), ((7.072, 41.411), (6, 41.015), (6, 40)))
        self.add_bezier('e8', (6, 8), ((6, 6.977), (7.096, 6.556), (7.915, 6.139)), ((8.086, 6.049), (7.82, 6.074), (8, 6)))
        self.add_bezier('e9', (40, 6), ((40.18, 6.065), (39.922, 6.041), (40.11, 6.123)), ((40.904, 6.45), (41.992, 7.293), (41.992, 8.266)), ((41.992, 8.332), (42, 7.935), (42, 8)))
        self.add_bezier('e10', (42, 40), ((41.926, 40.213), (41.951, 39.955), (41.836, 40.151)), ((41.411, 40.953), (41.006, 42), (40, 42)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', 'e6', 'e10', closed=True)
