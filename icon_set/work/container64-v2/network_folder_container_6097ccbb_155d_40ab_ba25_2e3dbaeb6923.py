"""Shared Network Folder: independently authored container.

Construction plan: A tabbed folder stands on a centered network stem and foot; preserve the source support.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/folders/folder stand_6097ccbb-155d-40ab-ba25-2e3dbaeb6923.svg. Lucide folder original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (network-folder-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '6097ccbb-155d-40ab-ba25-2e3dbaeb6923'
SOURCE_PATH = 'pictographic-primitives/folders/folder stand_6097ccbb-155d-40ab-ba25-2e3dbaeb6923.svg'
AUTHOR = 'claude-opus-5-5'


class NetworkFolderContainer(Container64):
    icon_id = 'network-folder-container'
    keyshape = Keyshape.SQUARE
    category = 'folders'
    categories = ('folders', 'primitives')
    aliases = ()
    keywords = ('network', 'folder', 'container')

    def build(self) -> None:
        self.add_line('folder-0', (10, 6), (24, 6))
        self.add_line('folder-1', (24, 6), (34, 14))
        self.add_line('folder-2', (34, 14), (54, 14))
        self.add_arc('folder-3', (54, 14), (58, 18), radius_x=4)
        self.add_line('folder-4', (58, 18), (58, 38))
        self.add_arc('folder-5', (58, 38), (54, 42), radius_x=4)
        self.add_line('folder-6', (54, 42), (10, 42))
        self.add_arc('folder-7', (10, 42), (6, 38), radius_x=4)
        self.add_line('folder-8', (6, 38), (6, 10))
        self.add_arc('folder-9', (6, 10), (10, 6), radius_x=4)
        self.add_line('stem', (32, 42), (32, 58))
        self.add_line('foot', (18, 58), (46, 58))
        self.add_contour('folder', 'folder-0', 'folder-1', 'folder-2', 'folder-3', 'folder-4', 'folder-5', 'folder-6', 'folder-7', 'folder-8', 'folder-9', closed=True)
        self.relate('connect', 'stem', 'folder')
        self.relate('connect', 'stem', 'foot')
