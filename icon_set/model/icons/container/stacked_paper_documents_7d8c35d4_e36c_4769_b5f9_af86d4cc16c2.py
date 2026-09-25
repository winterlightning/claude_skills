"""Two offset paper documents with a flowing lower edge.

HRECT_L spans (2,10)-(62,54). Front page owns the wavy bottom;
rear page contributes its exposed top and right edges. Occluded rear
edges are omitted, preserving the supplied reference's layered reading.
Lucide files informs the separated exposed rear-page contour; the source
provides the wavy front edge. Deliberate offset, no artificial symmetry.
Hosting via compose.py: plus-sign-state-131 and check-mark validate;
heart-state-63 returns review for contact with the front page.
Legacy probe IDs plus/heart/check are absent from the current registry.
"""
from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '7d8c35d4-e36c-4769-b5f9-af86d4cc16c2'
SOURCE_PATH = 'pictographic-primitives/diagrams/various document_7d8c35d4-e36c-4769-b5f9-af86d4cc16c2.svg'
AUTHOR = 'gpt-6'

class Drawing(Container64):
    icon_id = 'stacked-wavy-document-frames'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    categories = ('diagrams', 'primitives')
    aliases = ('stacked wavy document frames',)
    keywords = ('stacked','paper','documents')

    def build(self):
        self.add_polyline('rear', (12,10), (62,10), (62,44))
        self.add_line('front-top',(2,20),(52,20))
        self.add_line('front-right',(52,20),(52,48))
        self.add_bezier('wave',(52,48),((48,44),(44,42),(40,42)),
                         ((34,42),(32,48),(26,48)),
                         ((20,48),(20,54),(14,54)),
                         ((8,54),(6,52),(2,48)))
        self.add_line('front-left',(2,48),(2,20))
        self.add_contour('front','front-top','front-right','wave','front-left',closed=True)
