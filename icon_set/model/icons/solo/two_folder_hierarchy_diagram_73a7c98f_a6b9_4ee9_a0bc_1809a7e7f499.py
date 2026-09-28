"""Folder Hierarchy Structure."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '73a7c98f-a6b9-4ee9-a0bc-1809a7e7f499'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/folders/folder connect_73a7c98f-a6b9-4ee9-a0bc-1809a7e7f499.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-folder-hierarchy-diagram'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'folders'
    categories = ('folders', 'primitives')
    aliases = ()
    keywords = ('folder', 'hierarchy', 'tree', 'diagram', 'connection', 'organization', 'files')

    def build(self):
        # Plan: Two instances of one small tabbed folder; constant row pitch 22. Left spine and branches meet split folder walls. Lucide folder-tree. Bounds (6,6)-(42,42).
        for i,y in enumerate((6,28)):
            self.add_polyline(f'folder-{i}',(20,y+7),(20,y),(28,y),(31,y+3),(42,y+3),(42,y+14),(20,y+14),closed=True)
            self.add_line(f'branch-{i}',(6,y+7),(20,y+7))
            self.relate('connect',f'branch-{i}',f'folder-{i}')
        self.add_polyline('spine',(6,6),(6,13),(6,35))
        for i in range(2):self.relate('connect','spine',f'branch-{i}')
