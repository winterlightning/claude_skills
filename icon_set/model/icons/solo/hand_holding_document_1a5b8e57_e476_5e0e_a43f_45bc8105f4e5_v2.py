# Variant of hand-holding-document; parent file remains unchanged.
"""Hand Holding a Document. Authored from the supplied visual brief."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1a5b8e57-e476-5e0e-a43f-45bc8105f4e5'
SOURCE_PATH = 'pictographic-primitives/websites/digital policies data breach_1a5b8e57-e476-5e0e-a43f-45bc8105f4e5.svg'
AUTHOR = 'gpt-6'

class HandHoldingDocumentVariant2(Solo48):
    icon_id = 'hand-holding-document-v2'
    variant_of = 'hand-holding-document'
    variant_label = 'Clear document grip and spacing'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('hand', 'document', 'paper', 'grip', 'policy', 'file', 'holding')

    def build(self) -> None:
        self.add_polyline('paper',(30,23),(30,6),(8,6),(8,28),(22,28))
        self.add_line('text',(17,12),(21,12))
        self.add_line('finger-left',(22,32),(22,28))
        self.add_line('finger-upper',(22,28),(22,23))
        self.add_arc('fingertip',(22,23),(30,23),radius_x=4)
        self.add_polyline('hand-right',(30,23),(30,32),(40,26),(40,36))
        self.add_arc('palm-heel',(40,36),(32,42),radius_x=8)
        self.add_polyline('wrist',(32,42),(24,42),(16,36))
        self.add_contour('hand','finger-left','finger-upper','fingertip')
        self.relate('connect','hand','paper')
        self.relate('connect','hand','hand-right')
        self.relate('connect','paper','hand-right')
        self.relate('connect','hand-right','palm-heel')
        self.relate('connect','palm-heel','wrist')
