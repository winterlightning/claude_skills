'material-tile: independent smooth-curve repair.\n\nConstruction: A regular rounded square; its panel structure uses shared centerlines and four equal corners.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'f4d78781-45cc-57cc-9c82-6d29cec0be1d'
SOURCE_PATH = 'pictographic-primitives/construction/material tile_f4d78781-45cc-57cc-9c82-6d29cec0be1d.svg'
AUTHOR = 'gpt-6'


class MaterialTileVariant2(Solo48):
    icon_id = 'material-tile-v2'
    variant_of = 'material-tile'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('material', 'tile', 'construction')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,xs=(24,),ys=(24,))
        line(self,"vertical",(24,6),(24,42))
        line(self,"horizontal",(6,24),(42,24))
        contacts(self)
