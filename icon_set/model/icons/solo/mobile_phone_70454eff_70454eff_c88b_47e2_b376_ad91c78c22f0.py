'mobile-phone-70454eff: independent smooth-curve repair.\n\nConstruction: Phone with an exact rounded rectangle and lower control band; details centered with legal clearance.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/smartphone.svg and atomic-debug/smartphone.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '70454eff-c88b-47e2-b376-ad91c78c22f0'
SOURCE_PATH = 'pictographic-primitives/phones/mobile phone_70454eff-c88b-47e2-b376-ad91c78c22f0.svg'
AUTHOR = 'gpt-6'


class MobilePhone70454eff(Solo48):
    icon_id = 'mobile-phone-70454eff'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    aliases = ()
    keywords = ('mobile', 'phone', 'phones')
    keyshape = Keyshape.VRECT_L

    def build(self):
        box(self,'phone',8,4,40,44,5,ys=(34,))
        line(self,'band',(8,34),(40,34))
        line(self,"earpiece",(20,14),(28,14))
        contacts(self)
