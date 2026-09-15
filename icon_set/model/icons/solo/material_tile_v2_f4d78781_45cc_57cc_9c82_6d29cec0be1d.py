'material-tile: distinct review variant.\n\nConstruction: Four separate material tiles arranged on a shared grid with eight-unit centerline gaps.\nKeyshape: SQUARE; exact SOLO48 envelope.\nConstruction reference: layout-grid from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'f4d78781-45cc-57cc-9c82-6d29cec0be1d'
SOURCE_PATH = 'pictographic-primitives/construction/material tile_f4d78781-45cc-57cc-9c82-6d29cec0be1d.svg'
AUTHOR = 'gpt-6'


class MaterialTileVariant2(Solo48):
    icon_id = 'material-tile-v2'
    variant_of = 'material-tile'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('material', 'tile', 'construction')
    keyshape = Keyshape.SQUARE

    def build(self):
        for x in (6,28):
         for y in (6,28): box(self,f'tile-{x}-{y}',x,y,x+14,y+14,2)
        contacts(self)
