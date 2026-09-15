'square-symbol: independent smooth-curve repair.\n\nConstruction: A regular rounded square; its panel structure uses shared centerlines and four equal corners.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '2a45045f-3140-4253-8ad6-d194ab424293'
SOURCE_PATH = 'pictographic-primitives/symbol/square_2a45045f-3140-4253-8ad6-d194ab424293.svg'
AUTHOR = 'gpt-6'


class SquareVariant2(Solo48):
    icon_id = 'square-symbol-v2'
    variant_of = 'square-symbol'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('square', 'symbol')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,xs=(24,),ys=(24,))
        contacts(self)
