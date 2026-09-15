'vectors-anchor-square: independent smooth-curve repair.\n\nConstruction: A regular rounded square; its panel structure uses shared centerlines and four equal corners.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '765d4600-b424-48ac-a39f-4041183aa21d'
SOURCE_PATH = 'pictographic-primitives/design/vectors anchor square_765d4600-b424-48ac-a39f-4041183aa21d.svg'
AUTHOR = 'gpt-6'


class VectorsAnchorSquareVariant2(Solo48):
    icon_id = 'vectors-anchor-square-v2'
    variant_of = 'vectors-anchor-square'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('vectors', 'anchor', 'square', 'design')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,xs=(24,),ys=(24,))
        contacts(self)
