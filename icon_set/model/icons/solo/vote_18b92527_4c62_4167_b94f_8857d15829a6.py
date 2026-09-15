'vote: independent smooth-curve repair.\n\nConstruction: Ballot box below a centered diamond paper; rounded box corners.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/vote.svg and atomic-debug/vote.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '18b92527-4c62-4167-b94f-8857d15829a6'
SOURCE_PATH = 'pictographic-primitives/symbol/vote_18b92527-4c62-4167-b94f-8857d15829a6.svg'
AUTHOR = 'gpt-6'


class Vote(Solo48):
    icon_id = 'vote'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('vote', 'symbol')
    keyshape = Keyshape.VRECT_L

    def build(self):
        poly(self,'paper',(24,4),(34,14),(24,24),(14,14),closed=True)
        box(self,'box',8,24,40,44,4,xs=(24,))
        contacts(self)
