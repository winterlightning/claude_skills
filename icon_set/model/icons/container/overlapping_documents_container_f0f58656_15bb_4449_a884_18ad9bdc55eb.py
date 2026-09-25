"""Two Overlapping File Documents: independently authored container.

Construction plan: Front clipped-corner document with a partially hidden rear sheet; asymmetric overlap retained.
Keyshape VRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/files/duplicate file_f0f58656-15bb-4449-a884-18ad9bdc55eb.svg. Lucide file-stack original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (4, 0, 60, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = 'f0f58656-15bb-4449-a884-18ad9bdc55eb'
SOURCE_PATH = 'pictographic-primitives/files/duplicate file_f0f58656-15bb-4449-a884-18ad9bdc55eb.svg'
AUTHOR = 'gpt-6'


class OverlappingDocumentsContainer(Container64):
    icon_id = 'overlapping-documents-container'
    category = 'files'
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ('overlapping', 'documents', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        poly('front',(18,2),(46,2),(58,14),(58,50),(18,50),closed=True)
        path(self,'rear',(18,14),[('L',(6,14)),('L',(6,62)),('L',(46,62)),('L',(46,50))]);join('front','rear')
