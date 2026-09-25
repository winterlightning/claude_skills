"""Document compressed by mirrored inward chevrons. Page has upper and lower interrupted outlines; three centered writing rows share eight-unit pitch. Lucide files informed the clipped page silhouette.
Whole subject explicitly authorized by user; preserve saved family.
Keyshape: SQUARE; fine source details simplified only for native readability.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'a2280dd3-0b51-4414-8735-7bd943577c11'
SOURCE_PATH = 'pictographic-primitives/files/compress pdf_a2280dd3-0b51-4414-8735-7bd943577c11.svg'
AUTHOR = "gpt-6"

class Icon(Solo48):
    icon_id = 'document-compression-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'files'
    categories = ('files', 'primitives')
    aliases = ('Document Compression Symbol',)
    keywords = ('document', 'compression', 'symbol')
    def build(self):
        self.add_polyline("page-top",(14,14),(14,6),(28,6),(34,12),(34,14))
        self.add_polyline("page-bottom",(14,34),(14,42),(34,42),(34,34))
        for side in (-1,1):
            self.add_polyline("chevron-"+str(side),(24+side*18,18),(24+side*12,24),(24+side*18,30))
        for index,y in enumerate((16,24,32)):
            self.add_line("text-"+str(index),(22,y),(26,y))
