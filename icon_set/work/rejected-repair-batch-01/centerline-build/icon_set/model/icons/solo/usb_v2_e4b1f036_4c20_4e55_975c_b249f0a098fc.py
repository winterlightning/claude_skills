'usb: independent smooth-curve repair.\n\nConstruction: USB plug with a joined rectangular connector and rounded lower housing.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/usb.svg and atomic-debug/usb.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'e4b1f036-4c20-4e55-975c-b249f0a098fc'
SOURCE_PATH = 'pictographic-primitives/state/usb_e4b1f036-4c20-4e55-975c-b249f0a098fc.svg'
AUTHOR = 'gpt-6'


class UsbVariant2(Solo48):
    icon_id = 'usb-v2'
    variant_of = 'usb'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('usb', 'state')
    keyshape = Keyshape.VRECT_L

    def build(self):
        poly(self,'connector',(14,18),(14,4),(34,4),(34,18))
        box(self,'body',8,18,40,44,6,xs=(14,34))
        contacts(self)
