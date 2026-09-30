"""Two offset paper documents with a flowing lower edge.

HRECT_L spans (2,10)-(62,54). Front page owns the wavy bottom;
rear page contributes its exposed top and right edges. Occluded rear
edges are omitted, preserving the supplied reference's layered reading.
Lucide files informs the separated exposed rear-page contour; the source
provides the wavy front edge. Deliberate offset, no artificial symmetry.
Hosting via compose.py: plus-sign-state-131 and check-mark validate;
heart-state-63 returns review for contact with the front page.
Legacy probe IDs plus/heart/check are absent from the current registry.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (stacked-wavy-document-frames HRECT_L -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '7d8c35d4-e36c-4769-b5f9-af86d4cc16c2'
SOURCE_PATH = 'pictographic-primitives/diagrams/various document_7d8c35d4-e36c-4769-b5f9-af86d4cc16c2.svg'
AUTHOR = 'claude-opus-5-5'


class Drawing(Container64):
    icon_id = 'stacked-wavy-document-frames'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    categories = ('diagrams', 'primitives')
    aliases = ('stacked wavy document frames',)
    keywords = ('stacked', 'paper', 'documents')

    def build(self) -> None:
        self.add_line('rear-1', (13, 12), (60, 12))
        self.add_line('rear-2', (60, 12), (60, 42))
        self.add_line('front-top', (4, 22), (51, 22))
        self.add_line('front-right', (51, 22), (51, 46))
        self.add_bezier('wave', (51, 46), ((47.2, 42), (43.4, 40.333), (39.6, 40.333)), ((33.9, 40.333), (32, 46), (26.3, 46)), ((20.6, 46), (20.6, 52), (14.9, 52)), ((9.4, 52), (7.6, 50), (4, 46)))
        self.add_line('front-left', (4, 46), (4, 22))
        self.add_contour('rear', 'rear-1', 'rear-2')
        self.add_contour('front', 'front-top', 'front-right', 'wave', 'front-left', closed=True)
