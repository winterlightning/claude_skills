"""Two Overlapping File Documents: independently authored container.

Construction plan: Front clipped-corner document with a partially hidden rear sheet; asymmetric overlap retained.
Keyshape VRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/files/duplicate file_f0f58656-15bb-4449-a884-18ad9bdc55eb.svg. Lucide file-stack original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (4, 0, 60, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (overlapping-documents-container VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = 'f0f58656-15bb-4449-a884-18ad9bdc55eb'
SOURCE_PATH = 'pictographic-primitives/files/duplicate file_f0f58656-15bb-4449-a884-18ad9bdc55eb.svg'
AUTHOR = 'claude-opus-5-5'


class OverlappingDocumentsContainer(Container64):
    icon_id = 'overlapping-documents-container'
    keyshape = Keyshape.VRECT_L
    category = 'files'
    categories = ('files', 'primitives')
    aliases = ()
    keywords = ('overlapping', 'documents', 'container')

    def build(self) -> None:
        self.add_line('front-1', (20, 4), (44, 4))
        self.add_line('front-2', (44, 4), (54, 15))
        self.add_line('front-3', (54, 15), (54, 49))
        self.add_line('front-4', (54, 49), (20, 49))
        self.add_line('front-5', (20, 49), (20, 4))
        self.add_line('rear-0', (20, 15), (10, 15))
        self.add_line('rear-1', (10, 15), (10, 60))
        self.add_line('rear-2', (10, 60), (44, 60))
        self.add_line('rear-3', (44, 60), (44, 49))
        self.add_contour('front', 'front-1', 'front-2', 'front-3', 'front-4', 'front-5', closed=True)
        self.add_contour('rear', 'rear-0', 'rear-1', 'rear-2', 'rear-3')
        self.relate('connect', 'front', 'rear')
