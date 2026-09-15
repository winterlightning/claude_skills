'keyboard-button: independent smooth-curve repair.\n\nConstruction: A regular rounded square; its panel structure uses shared centerlines and four equal corners.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '2f64ef8b-f8cd-5add-84ab-cb04db2d8ac7'
SOURCE_PATH = 'pictographic-primitives/interface-essential/keyboard button_2f64ef8b-f8cd-5add-84ab-cb04db2d8ac7.svg'
AUTHOR = 'gpt-6'


class KeyboardButtonVariant2(Solo48):
    icon_id = 'keyboard-button-v2'
    variant_of = 'keyboard-button'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'button', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,xs=(24,),ys=(24,))
        contacts(self)
