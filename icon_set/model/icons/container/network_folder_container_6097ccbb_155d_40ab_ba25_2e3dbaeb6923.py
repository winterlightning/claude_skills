"""Shared Network Folder: independently authored container.

Construction plan: A tabbed folder stands on a centered network stem and foot; preserve the source support.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/folders/folder stand_6097ccbb-155d-40ab-ba25-2e3dbaeb6923.svg. Lucide folder original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '6097ccbb-155d-40ab-ba25-2e3dbaeb6923'
SOURCE_PATH = 'pictographic-primitives/folders/folder stand_6097ccbb-155d-40ab-ba25-2e3dbaeb6923.svg'
AUTHOR = 'gpt-6'


class NetworkFolderContainer(Container64):
    icon_id = 'network-folder-container'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('network', 'folder', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'folder',(6,2),[('L',(24,2)),('L',(34,10)),('L',(58,10)),('A',(62,14),4,4,True),('L',(62,42)),('A',(58,46),4,4,True),('L',(6,46)),('A',(2,42),4,4,True),('L',(2,6)),('A',(6,2),4,4,True)],True)
        line('stem',(32,46),(32,62));line('foot',(18,62),(46,62));join('stem','folder');join('stem','foot')
