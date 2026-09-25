'dice-empty: independent smooth-curve repair.\n\nConstruction: Regular die outline with equal radius corners; retain the central pip where present.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/dice-1.svg and atomic-debug/dice-1.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '82ba9e82-eb9d-5ce8-8e11-dbd76429d353'
SOURCE_PATH = 'pictographic-primitives/video-games/dice empty_82ba9e82-eb9d-5ce8-8e11-dbd76429d353.svg'
AUTHOR = 'gpt-6'


class DiceEmpty(Solo48):
    icon_id = 'dice-empty'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('dice', 'empty', 'video-games')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'die',6,6,42,42,7)
        contacts(self)
