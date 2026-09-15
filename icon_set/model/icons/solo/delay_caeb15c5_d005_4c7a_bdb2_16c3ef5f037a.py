'delay: independent smooth-curve repair.\n\nConstruction: Delay symbol: one true half ellipse joins the two horizontal rails tangentially.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/rectangle-horizontal.svg and atomic-debug/rectangle-horizontal.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'caeb15c5-d005-4c7a-bdb2-16c3ef5f037a'
SOURCE_PATH = 'pictographic-primitives/diagrams/delay_caeb15c5-d005-4c7a-bdb2-16c3ef5f037a.svg'
AUTHOR = 'gpt-6'


class Delay(Solo48):
    icon_id = 'delay'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('delay', 'diagrams')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'delay',(4,8),('L',(24,8)),('A',20,16,True,(44,24)),('A',20,16,True,(24,40)),('L',(4,40)),('L',(4,8)),closed=True)
        contacts(self)
