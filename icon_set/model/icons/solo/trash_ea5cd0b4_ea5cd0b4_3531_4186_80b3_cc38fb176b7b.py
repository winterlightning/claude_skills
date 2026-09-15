'trash-ea5cd0b4: independent smooth-curve repair.\n\nConstruction: Wastebasket with a broad lid and matched rounded lower corners.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/trash-2.svg and atomic-debug/trash-2.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'ea5cd0b4-3531-4186-80b3-cc38fb176b7b'
SOURCE_PATH = 'pictographic-primitives/symbol/trash_ea5cd0b4-3531-4186-80b3-cc38fb176b7b.svg'
AUTHOR = 'gpt-6'


class TrashEa5cd0b4(Solo48):
    icon_id = 'trash-ea5cd0b4'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('trash', 'symbol')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'bin',(10,14),('L',(10,39)),('A',5,5,False,(15,44)),('L',(33,44)),('A',5,5,False,(38,39)),('L',(38,14)))
        line(self,'lid',(8,14),(40,14));line(self,'knob',(24,4),(24,14))
        contacts(self)
