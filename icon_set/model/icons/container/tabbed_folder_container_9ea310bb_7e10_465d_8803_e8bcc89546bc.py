"""Document Storage Folder: independently authored container.

Construction plan: Single rounded folder silhouette with a raised left tab, no lower sleeve.
Keyshape HRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/folders/folder_9ea310bb-7e10-465d-8803-e8bcc89546bc.svg. Lucide folder original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 4, 64, 60).
Hosting measured with compose.py: plus does not clear, heart does not clear, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (tabbed-folder-container HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '9ea310bb-7e10-465d-8803-e8bcc89546bc'
SOURCE_PATH = 'pictographic-primitives/folders/folder_9ea310bb-7e10-465d-8803-e8bcc89546bc.svg'
AUTHOR = 'claude-opus-5-5'


class TabbedFolderContainer(Container64):
    icon_id = 'tabbed-folder-container'
    keyshape = Keyshape.HRECT_L
    category = 'folders'
    categories = ('folders', 'primitives')
    aliases = ()
    keywords = ('tabbed', 'folder', 'container')

    def build(self) -> None:
        self.add_line('folder-0', (8, 10), (24, 10))
        self.add_line('folder-1', (24, 10), (34, 18))
        self.add_line('folder-2', (34, 18), (56, 18))
        self.add_arc('folder-3', (56, 18), (60, 22), radius_x=4)
        self.add_line('folder-4', (60, 22), (60, 50))
        self.add_arc('folder-5', (60, 50), (56, 54), radius_x=4)
        self.add_line('folder-6', (56, 54), (8, 54))
        self.add_arc('folder-7', (8, 54), (4, 50), radius_x=4)
        self.add_line('folder-8', (4, 50), (4, 14))
        self.add_arc('folder-9', (4, 14), (8, 10), radius_x=4)
        self.add_contour('folder', 'folder-0', 'folder-1', 'folder-2', 'folder-3', 'folder-4', 'folder-5', 'folder-6', 'folder-7', 'folder-8', 'folder-9', closed=True)
