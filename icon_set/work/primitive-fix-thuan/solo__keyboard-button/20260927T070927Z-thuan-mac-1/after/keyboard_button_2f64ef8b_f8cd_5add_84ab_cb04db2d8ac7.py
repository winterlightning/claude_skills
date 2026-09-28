"""keyboard-button: approved original model.

Construction: Keyboard keycap with a lower bevel line, making the key depth visible.
Keyshape: SQUARE; exact SOLO48 envelope.
Construction reference: layout-grid from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '2f64ef8b-f8cd-5add-84ab-cb04db2d8ac7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__keyboard-button/20260927T070927Z-thuan-mac-1/reference/keyboard button_2f64ef8b-f8cd-5add-84ab-cb04db2d8ac7.svg'
AUTHOR = 'gpt-6'

class KeyboardButton(Solo48):
    icon_id = 'keyboard-button'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('keyboard', 'button', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        # The reference is a single softly rounded key face, without a bevel.
        box(self, 'keycap', 6, 6, 42, 42, 6)
