'rectangle-dots-symbol: independent smooth-curve repair.\n\nConstruction: Four matching scan corners with true quarter arcs; content remains centered.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/scan.svg and atomic-debug/scan.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '79a79b08-2adb-4aab-bbe9-6affe885b5dd'
SOURCE_PATH = 'pictographic-primitives/symbol/rectangle dots_79a79b08-2adb-4aab-bbe9-6affe885b5dd.svg'
AUTHOR = 'gpt-6'


class RectangleDotsSymbol(Solo48):
    icon_id = 'rectangle-dots-symbol'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('rectangle', 'dots', 'symbol')
    keyshape = Keyshape.SQUARE

    def build(self):
        path(self,'tl',(6,16),('L',(6,10)),('A',4,4,True,(10,6)),('L',(16,6)))
        path(self,'tr',(32,6),('L',(38,6)),('A',4,4,True,(42,10)),('L',(42,16)))
        path(self,'br',(42,32),('L',(42,38)),('A',4,4,True,(38,42)),('L',(32,42)))
        path(self,'bl',(16,42),('L',(10,42)),('A',4,4,True,(6,38)),('L',(6,32)))
        self.add_dot("dot-top",(24,16))
        self.add_dot("dot-bottom",(24,32))
        contacts(self)
