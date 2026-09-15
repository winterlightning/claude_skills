'dice: independent smooth-curve repair.\n\nConstruction: Regular die outline with equal radius corners; retain the central pip where present.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/dice-1.svg and atomic-debug/dice-1.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '2a9164c0-da9e-5daf-ab67-2a9588ba7d68'
SOURCE_PATH = 'pictographic-primitives/entertainment/dice_2a9164c0-da9e-5daf-ab67-2a9588ba7d68.svg'
AUTHOR = 'gpt-6'


class Dice(Solo48):
    icon_id = 'dice'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ()
    keywords = ('dice', 'entertainment')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'die',6,6,42,42,7)
        ellipse(self,"pip",24,24,3)
        contacts(self)
