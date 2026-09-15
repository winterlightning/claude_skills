'vectors-anchor-square: distinct review variant.\n\nConstruction: Vector anchor square with four attached diagonal handles and endpoint nodes; all handles meet the inner square at real vertices.\nKeyshape: SQUARE; exact SOLO48 envelope.\nConstruction reference: layout-grid from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '765d4600-b424-48ac-a39f-4041183aa21d'
SOURCE_PATH = 'pictographic-primitives/design/vectors anchor square_765d4600-b424-48ac-a39f-4041183aa21d.svg'
AUTHOR = 'gpt-6'


class VectorsAnchorSquareVariant2(Solo48):
    icon_id = 'vectors-anchor-square-v2'
    variant_of = 'vectors-anchor-square'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('vectors', 'anchor', 'square', 'design')
    keyshape = Keyshape.SQUARE

    def build(self):
        poly(self,'square',(14,14),(34,14),(34,34),(14,34),closed=True)
        for i,(a,b) in enumerate((((6,6),(14,14)),((42,6),(34,14)),((42,42),(34,34)),((6,42),(14,34)))):
         line(self,f'handle-{i}',a,b);self.add_dot(f'anchor-{i}',a)
        contacts(self)
