'expand: independent smooth-curve repair.\n\nConstruction: Four matching scan corners with true quarter arcs; content remains centered.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/scan.svg and atomic-debug/scan.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'fcf922f1-c091-4a41-9a2c-3b6016b7cf68'
SOURCE_PATH = 'pictographic-primitives/interface-essential/expand_fcf922f1-c091-4a41-9a2c-3b6016b7cf68.svg'
AUTHOR = 'gpt-6'


class ExpandVariant2(Solo48):
    icon_id = 'expand-v2'
    variant_of = 'expand'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('expand', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        path(self,'tl',(6,16),('L',(6,10)),('A',4,4,True,(10,6)),('L',(16,6)))
        path(self,'tr',(32,6),('L',(38,6)),('A',4,4,True,(42,10)),('L',(42,16)))
        path(self,'br',(42,32),('L',(42,38)),('A',4,4,True,(38,42)),('L',(32,42)))
        path(self,'bl',(16,42),('L',(10,42)),('A',4,4,True,(6,38)),('L',(6,32)))
        box(self,"content",16,18,32,30,2)
        contacts(self)
