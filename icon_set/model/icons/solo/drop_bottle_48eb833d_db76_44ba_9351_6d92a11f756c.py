'drop-bottle: independent smooth-curve repair.\n\nConstruction: Bottle with a short neck, equal shoulder transitions and rounded heel.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/bottle-wine.svg and atomic-debug/bottle-wine.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '48eb833d-db76-44ba-9351-6d92a11f756c'
SOURCE_PATH = 'pictographic-primitives/symbol/drop bottle_48eb833d-db76-44ba-9351-6d92a11f756c.svg'
AUTHOR = 'gpt-6'


class DropBottle(Solo48):
    icon_id = 'drop-bottle'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('drop', 'bottle', 'symbol')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'bottle',(19,4),('L',(29,4)),('L',(29,12)),('C',(29,17),(40,17),(40,24)),('L',(40,39)),('A',5,5,True,(35,44)),('L',(13,44)),('A',5,5,True,(8,39)),('L',(8,24)),('C',(8,17),(19,17),(19,12)),('L',(19,4)),closed=True)
        contacts(self)
