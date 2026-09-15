'add-circle-1: independent smooth-curve repair.\n\nConstruction: Concentric circular frame; equal cross arms end ten units inside its centerline.\nKeyshape: CIRCLE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/circle-plus.svg and atomic-debug/circle-plus.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '39599cbe-59cb-4e0a-a987-fdb1399c7551'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/add circle 1_39599cbe-59cb-4e0a-a987-fdb1399c7551.svg'
AUTHOR = 'gpt-6'


class AddCircle1Variant2(Solo48):
    icon_id = 'add-circle-1-v2'
    variant_of = 'add-circle-1'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('add', 'circle', '_uncategorized_01')
    keyshape = Keyshape.CIRCLE

    def build(self):
        ellipse(self,'ring',24,24,20)
        line(self,'cross-h',(14,24),(34,24))
        line(self,'cross-v',(24,14),(24,34))
        contacts(self)
