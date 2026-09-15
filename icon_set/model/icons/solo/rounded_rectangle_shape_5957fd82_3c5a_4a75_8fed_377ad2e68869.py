'rounded-rectangle-shape: independent smooth-curve repair.\n\nConstruction: Capsule-like rounded enclosure with equal semicircular ends; centered interior where present.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/rectangle-horizontal.svg and atomic-debug/rectangle-horizontal.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '5957fd82-3c5a-4a75-8fed-377ad2e68869'
SOURCE_PATH = 'pictographic-primitives/design/rounded rectangle shape_5957fd82-3c5a-4a75-8fed-377ad2e68869.svg'
AUTHOR = 'gpt-6'


class RoundedRectangleShape(Solo48):
    icon_id = 'rounded-rectangle-shape'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('rounded', 'rectangle', 'shape', 'design')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'outline',4,8,44,40,16)
        contacts(self)
