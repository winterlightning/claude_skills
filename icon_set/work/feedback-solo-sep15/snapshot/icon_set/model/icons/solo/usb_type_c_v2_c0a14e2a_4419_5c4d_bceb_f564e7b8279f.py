'usb-type-c: independent smooth-curve repair.\n\nConstruction: Capsule-like rounded enclosure with equal semicircular ends; centered interior where present.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/rectangle-horizontal.svg and atomic-debug/rectangle-horizontal.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'c0a14e2a-4419-5c4d-bceb-f564e7b8279f'
SOURCE_PATH = 'pictographic-primitives/electronics/usb type c_c0a14e2a-4419-5c4d-bceb-f564e7b8279f.svg'
AUTHOR = 'gpt-6'


class UsbTypeCVariant2(Solo48):
    icon_id = 'usb-type-c-v2'
    variant_of = 'usb-type-c'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('usb', 'type', 'c', 'electronics')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'outline',4,8,44,40,16)
        line(self,"connector",(17,24),(31,24))
        contacts(self)
