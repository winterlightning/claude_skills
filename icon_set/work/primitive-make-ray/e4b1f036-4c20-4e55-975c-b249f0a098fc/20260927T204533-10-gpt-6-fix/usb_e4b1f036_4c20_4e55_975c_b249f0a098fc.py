'usb: independent smooth-curve repair.\n\nConstruction: USB plug with a joined rectangular connector and rounded lower housing.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/usb.svg and atomic-debug/usb.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'e4b1f036-4c20-4e55-975c-b249f0a098fc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__usb/20260927T133645Z-thuan-mac-1/reference/usb_e4b1f036-4c20-4e55-975c-b249f0a098fc.svg'
AUTHOR = "gpt-6"


class Usb(Solo48):
    icon_id = 'usb'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('usb', 'state')
    keyshape = Keyshape.VRECT_L

    def build(self):
        poly(self,'connector',(15,18),(15,4),(33,4),(33,18))
        box(self,'body',8,18,40,44,6,xs=(15,33))
        contacts(self)
