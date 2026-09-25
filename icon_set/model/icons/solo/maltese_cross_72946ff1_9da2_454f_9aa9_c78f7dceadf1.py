'maltese-cross: independent smooth-curve repair.\n\nConstruction: Maltese cross with a shared waist and matching curved sides; purposeful arm-end corners.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/plus.svg and atomic-debug/plus.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '72946ff1-9da2-454f-9aa9-c78f7dceadf1'
SOURCE_PATH = 'pictographic-primitives/symbol/maltese cross_72946ff1-9da2-454f-9aa9-c78f7dceadf1.svg'
AUTHOR = 'gpt-6'


class MalteseCross(Solo48):
    icon_id = 'maltese-cross'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('maltese', 'cross', 'symbol')
    keyshape = Keyshape.SQUARE

    def build(self):
        path(self,'cross',(16,6),('L',(32,6)),('C',(30,11),(27,15),(30,18)),('C',(33,21),(37,18),(42,16)),('L',(42,32)),('C',(37,30),(33,27),(30,30)),('C',(27,33),(30,37),(32,42)),('L',(16,42)),('C',(18,37),(21,33),(18,30)),('C',(15,27),(11,30),(6,32)),('L',(6,16)),('C',(11,18),(15,21),(18,18)),('C',(21,15),(18,11),(16,6)),closed=True)
        contacts(self)
