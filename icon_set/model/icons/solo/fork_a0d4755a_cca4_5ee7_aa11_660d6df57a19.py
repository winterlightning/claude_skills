'fork: independent smooth-curve repair.\n\nConstruction: Fork-like trident with a coherent rounded bowl and central stem; equal arm extents.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/utensils.svg and atomic-debug/utensils.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'a0d4755a-cca4-5ee7-aa11-660d6df57a19'
SOURCE_PATH = 'pictographic-primitives/food/fork_a0d4755a-cca4-5ee7-aa11-660d6df57a19.svg'
AUTHOR = 'gpt-6'


class Fork(Solo48):
    icon_id = 'fork'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('fork', 'food')
    keyshape = Keyshape.SQUARE

    def build(self):
        path(self,'bowl',(6,6),('L',(6,16)),('C',(6,22),(12,24),(24,24)),('C',(36,24),(42,22),(42,16)),('L',(42,6)))
        line(self,'stem',(24,6),(24,24));line(self,'handle',(24,24),(24,42))
        contacts(self)
