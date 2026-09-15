'text-bar: independent smooth-curve repair.\n\nConstruction: Text caret with matched concave terminal curves and a central crossbar.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/text-cursor.svg and atomic-debug/text-cursor.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'a6fdd803-e318-450c-9350-15e3faf7e238'
SOURCE_PATH = 'pictographic-primitives/interface-essential/text bar_a6fdd803-e318-450c-9350-15e3faf7e238.svg'
AUTHOR = 'gpt-6'


class TextBar(Solo48):
    icon_id = 'text-bar'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'bar', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        path(self,'top',(6,6),('C',(14,6),(19,9),(24,14)),('C',(29,9),(34,6),(42,6)))
        path(self,'bottom',(6,42),('C',(14,42),(19,39),(24,34)),('C',(29,39),(34,42),(42,42)))
        line(self,'stem',(24,14),(24,34));line(self,'crossbar',(16,27),(32,27))
        contacts(self)
