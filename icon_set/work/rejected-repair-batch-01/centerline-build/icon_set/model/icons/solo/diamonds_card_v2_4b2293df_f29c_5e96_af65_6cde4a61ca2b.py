'diamonds-card: independent smooth-curve repair.\n\nConstruction: A clean centered diamond; intentional directional vertices remain crisp and equal.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/diamond.svg and atomic-debug/diamond.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '4b2293df-f29c-5e96-af65-6cde4a61ca2b'
SOURCE_PATH = 'pictographic-primitives/entertainment/diamonds card_4b2293df-f29c-5e96-af65-6cde4a61ca2b.svg'
AUTHOR = 'gpt-6'


class DiamondsCardVariant2(Solo48):
    icon_id = 'diamonds-card-v2'
    variant_of = 'diamonds-card'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ()
    keywords = ('diamonds', 'card', 'entertainment')
    keyshape = Keyshape.VRECT_L

    def build(self):
        poly(self,'diamond',(24,4),(40,24),(24,44),(8,24),closed=True)
        contacts(self)
