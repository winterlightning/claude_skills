'trash-can-symbol: independent smooth-curve repair.\n\nConstruction: Tapered wastebasket with rounded heel and a centered loop handle on the lid.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/trash-2.svg and atomic-debug/trash-2.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'f0702c6a-8d52-4871-82ba-3206aeb5703e'
SOURCE_PATH = 'pictographic-primitives/symbol/trash can_f0702c6a-8d52-4871-82ba-3206aeb5703e.svg'
AUTHOR = 'gpt-6'


class TrashCan(Solo48):
    icon_id = 'trash-can-symbol'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('trash', 'can', 'symbol')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'bin',(10,20),('L',(13,38)),('C',(13,42),(16,44),(20,44)),('L',(28,44)),('C',(32,44),(35,42),(35,38)),('L',(38,20)))
        path(self,'lid',(8,20),('L',(8,12)),('L',(18,12)),('L',(18,7)),('A',3,3,True,(21,4)),('L',(27,4)),('A',3,3,True,(30,7)),('L',(30,12)),('L',(40,12)),('L',(40,20)),('L',(8,20)),closed=True)
        contacts(self)
