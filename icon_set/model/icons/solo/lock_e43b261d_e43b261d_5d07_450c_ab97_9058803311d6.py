'lock-e43b261d: independent smooth-curve repair.\n\nConstruction: Padlock with a circular shackle and four equal body corners; shackle meets exact top-edge nodes.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/lock.svg and atomic-debug/lock.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'e43b261d-5d07-450c-ab97-9058803311d6'
SOURCE_PATH = 'pictographic-primitives/interface-essential/lock_e43b261d-5d07-450c-ab97-9058803311d6.svg'
AUTHOR = 'gpt-6'


class LockE43b261d(Solo48):
    icon_id = 'lock-e43b261d'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'lock-e43b261d')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'shackle',(14,22),('L',(14,14)),('A',10,10,True,(24,4)),('A',10,10,True,(34,14)),('L',(34,22)))
        box(self,'body',8,22,40,44,4,xs=(14,34))
        line(self,"keyhole",(24,31),(24,34))
        contacts(self)
