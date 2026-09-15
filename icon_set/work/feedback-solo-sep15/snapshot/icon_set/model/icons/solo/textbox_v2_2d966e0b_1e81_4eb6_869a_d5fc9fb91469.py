'textbox: independent smooth-curve repair.\n\nConstruction: Rounded text field with a centered T; spacious margins around the letter.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/type.svg and atomic-debug/type.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '2d966e0b-1e81-4eb6-869a-d5fc9fb91469'
SOURCE_PATH = 'pictographic-primitives/interface-essential/textbox_2d966e0b-1e81-4eb6-869a-d5fc9fb91469.svg'
AUTHOR = 'gpt-6'


class TextboxVariant2(Solo48):
    icon_id = 'textbox-v2'
    variant_of = 'textbox'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('textbox', 'interface-essential')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'field',4,8,44,40,5)
        line(self,'top',(16,18),(32,18));line(self,'stem',(24,18),(24,30))
        contacts(self)
