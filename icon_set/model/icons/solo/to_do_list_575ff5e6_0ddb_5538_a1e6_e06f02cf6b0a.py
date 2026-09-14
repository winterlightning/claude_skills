"""Three horizontal rows pair left-hand checkboxes with text lines. The upper two boxes are empty, while the bottom box opens around a large check mark extending toward its corresponding line.
Lucide list-todo construction. Two empty square boxes and a check retain the three-row list; the completed box outline is omitted to leave a clear check.
SQUARE: centerline extremes (6,6)-(42,42); independently authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '575ff5e6-0ddb-5538-a1e6-e06f02cf6b0a'
SOURCE_PATH = 'pictographic-primitives/work/list to do_575ff5e6-0ddb-5538-a1e6-e06f02cf6b0a.svg'
AUTHOR = 'gpt-6'


class ToDoList(Solo48):
    icon_id = 'to-do-list'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('list', 'todo', 'checkbox', 'check', 'task', 'completion')

    def build(self) -> None:
        self.add_polyline('box-0', (6, 6), (14, 6), (14, 14), (6, 14), closed=True)
        self.add_line('text-0', (23, 10), (42, 10))
        self.add_polyline('box-1', (6, 22), (14, 22), (14, 30), (6, 30), closed=True)
        self.add_line('text-1', (23, 26), (42, 26))
        self.add_polyline('check', (6, 39), (10, 42), (16, 38), closed=False)
        self.add_line('text-2', (25, 40), (42, 40))
