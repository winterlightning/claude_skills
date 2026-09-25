'soap: independent smooth-curve repair.\n\nConstruction: Soap bar with a smooth elliptical top and rounded base; shared exact side attachments.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/cylinder.svg and atomic-debug/cylinder.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '4ee9ecc8-c1c5-4fbd-86bf-4c3aaf9a18f4'
SOURCE_PATH = 'pictographic-primitives/symbol/soap_4ee9ecc8-c1c5-4fbd-86bf-4c3aaf9a18f4.svg'
AUTHOR = 'gpt-6'


class Soap(Solo48):
    icon_id = 'soap'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('soap', 'symbol')
    keyshape = Keyshape.HRECT_L

    def build(self):
        ellipse(self,'top',24,16,20,8)
        path(self,'body',(4,16),('L',(4,32)),('A',20,8,False,(24,40)),('A',20,8,False,(44,32)),('L',(44,16)))
        contacts(self)
