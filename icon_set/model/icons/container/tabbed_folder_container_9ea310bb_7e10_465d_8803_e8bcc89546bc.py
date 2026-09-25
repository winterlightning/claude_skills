"""Document Storage Folder: independently authored container.

Construction plan: Single rounded folder silhouette with a raised left tab, no lower sleeve.
Keyshape HRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/folders/folder_9ea310bb-7e10-465d-8803-e8bcc89546bc.svg. Lucide folder original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 4, 64, 60).
Hosting measured with compose.py: plus does not clear, heart does not clear, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '9ea310bb-7e10-465d-8803-e8bcc89546bc'
SOURCE_PATH = 'pictographic-primitives/folders/folder_9ea310bb-7e10-465d-8803-e8bcc89546bc.svg'
AUTHOR = 'gpt-6'


class TabbedFolderContainer(Container64):
    icon_id = 'tabbed-folder-container'
    category = 'folders'
    keyshape = Keyshape.HRECT_XL
    aliases = ()
    keywords = ('tabbed', 'folder', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'folder',(6,6),[('L',(24,6)),('L',(34,14)),('L',(58,14)),('A',(62,18),4,4,True),('L',(62,54)),('A',(58,58),4,4,True),('L',(6,58)),('A',(2,54),4,4,True),('L',(2,10)),('A',(6,6),4,4,True)],True)
