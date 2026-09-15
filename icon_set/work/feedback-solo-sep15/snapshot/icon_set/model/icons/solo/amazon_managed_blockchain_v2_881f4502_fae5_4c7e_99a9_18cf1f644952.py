'amazon-managed-blockchain: independent smooth-curve repair.\n\nConstruction: Two identical rounded ledger blocks joined by one central link; shared dimensions.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/rectangle-horizontal.svg and atomic-debug/rectangle-horizontal.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '881f4502-fae5-4c7e-99a9-18cf1f644952'
SOURCE_PATH = 'pictographic-primitives/programing/amazon managed blockchain_881f4502-fae5-4c7e-99a9-18cf1f644952.svg'
AUTHOR = 'gpt-6'


class AmazonManagedBlockchainVariant2(Solo48):
    icon_id = 'amazon-managed-blockchain-v2'
    variant_of = 'amazon-managed-blockchain'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('amazon', 'managed', 'blockchain', 'programing')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'left',6,6,20,42,3,ys=(24,))
        box(self,'right',28,6,42,42,3,ys=(24,))
        line(self,'link',(20,24),(28,24))
        contacts(self)
