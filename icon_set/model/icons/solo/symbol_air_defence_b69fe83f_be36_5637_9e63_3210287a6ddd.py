'symbol-air-defence: independent smooth-curve repair.\n\nConstruction: Air-defense symbol in a tall frame with a broad smooth arch at its base.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/rectangle-horizontal.svg and atomic-debug/rectangle-horizontal.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'b69fe83f-be36-5637-9e63-3210287a6ddd'
SOURCE_PATH = 'pictographic-primitives/war/symbol air defence_b69fe83f-be36-5637-9e63-3210287a6ddd.svg'
AUTHOR = 'gpt-6'


class SymbolAirDefence(Solo48):
    icon_id = 'symbol-air-defence'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('symbol', 'air', 'defence', 'war')
    keyshape = Keyshape.HRECT_L

    def build(self):
        poly(self,'frame',(4,40),(4,8),(44,8),(44,40),(4,40),closed=True)
        path(self,'arch',(4,40),('C',(16,25),(32,25),(44,40)))
        contacts(self)
