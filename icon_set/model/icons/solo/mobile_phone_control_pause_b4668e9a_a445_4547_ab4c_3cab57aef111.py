'mobile-phone-control-pause: independent smooth-curve repair.\n\nConstruction: Phone with an exact rounded rectangle and lower control band; details centered with legal clearance.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/smartphone.svg and atomic-debug/smartphone.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'b4668e9a-a445-4547-ab4c-3cab57aef111'
SOURCE_PATH = 'pictographic-primitives/state/mobile phone control pause_b4668e9a-a445-4547-ab4c-3cab57aef111.svg'
AUTHOR = 'gpt-6'


class MobilePhoneControlPause(Solo48):
    icon_id = 'mobile-phone-control-pause'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('mobile', 'phone', 'control', 'pause', 'state')
    keyshape = Keyshape.VRECT_L

    def build(self):
        box(self,'phone',8,4,40,44,5,ys=(34,))
        line(self,'band',(8,34),(40,34))
        line(self,"pause-left",(19,14),(19,24))
        line(self,"pause-right",(29,14),(29,24))
        contacts(self)
