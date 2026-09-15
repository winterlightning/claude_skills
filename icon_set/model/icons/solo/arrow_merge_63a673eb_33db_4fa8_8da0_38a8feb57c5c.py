'arrow-merge: independent smooth-curve repair.\n\nConstruction: Two flowing branches diverge from one stem with matching tangents; directional arrow tips retain purposeful corners.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/split.svg and atomic-debug/split.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '63a673eb-33db-4fa8-8da0-38a8feb57c5c'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow merge_63a673eb-33db-4fa8-8da0-38a8feb57c5c.svg'
AUTHOR = 'gpt-6'


class ArrowMerge(Solo48):
    icon_id = 'arrow-merge'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'merge', 'symbol')
    keyshape = Keyshape.SQUARE

    def build(self):
        line(self,'stem',(24,42),(24,34))
        path(self,'branch-left',(24,34),('C',(24,24),(14,12),(6,6)))
        path(self,'branch-right',(24,34),('C',(24,24),(34,12),(42,6)))
        poly(self,'left-head',(6,18),(6,6),(18,6))
        poly(self,'right-head',(30,6),(42,6),(42,18))
        contacts(self)
