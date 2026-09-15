'phone-box: independent smooth-curve repair.\n\nConstruction: Domed phone kiosk with a circular crown and centered lower divider.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/door-open.svg and atomic-debug/door-open.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '2b7a921e-0a41-4b3f-b6dd-57df1cbed0b2'
SOURCE_PATH = 'pictographic-primitives/symbol/phone box_2b7a921e-0a41-4b3f-b6dd-57df1cbed0b2.svg'
AUTHOR = 'gpt-6'


class PhoneBox(Solo48):
    icon_id = 'phone-box'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('phone', 'box', 'symbol')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'dome',(8,20),('A',16,16,True,(24,4)),('A',16,16,True,(40,20)))
        poly(self,'frame',(8,44),(8,20),(40,20),(40,44))
        line(self,'door',(24,29),(24,44))
        contacts(self)
