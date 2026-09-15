'keyboard-button: distinct review variant.\n\nConstruction: Keyboard keycap with a lower bevel line, making the key depth visible.\nKeyshape: SQUARE; exact SOLO48 envelope.\nConstruction reference: layout-grid from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '2f64ef8b-f8cd-5add-84ab-cb04db2d8ac7'
SOURCE_PATH = 'pictographic-primitives/interface-essential/keyboard button_2f64ef8b-f8cd-5add-84ab-cb04db2d8ac7.svg'
AUTHOR = 'gpt-6'


class KeyboardButtonVariant2(Solo48):
    icon_id = 'keyboard-button-v2'
    variant_of = 'keyboard-button'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'button', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'keycap',6,6,42,42,4,ys=(30,))
        line(self,'bevel',(6,30),(42,30))
        contacts(self)
