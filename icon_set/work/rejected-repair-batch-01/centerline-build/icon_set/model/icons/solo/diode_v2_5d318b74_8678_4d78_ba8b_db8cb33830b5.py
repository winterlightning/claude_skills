'diode: independent smooth-curve repair.\n\nConstruction: Diode triangle, cathode and leads with exact horizontal symmetry and real endpoint attachments.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/chevrons-right.svg and atomic-debug/chevrons-right.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '5d318b74-8678-4d78-ba8b-db8cb33830b5'
SOURCE_PATH = 'pictographic-primitives/electronics/diode_5d318b74-8678-4d78-ba8b-db8cb33830b5.svg'
AUTHOR = 'gpt-6'


class DiodeVariant2(Solo48):
    icon_id = 'diode-v2'
    variant_of = 'diode'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('diode', 'electronics')
    keyshape = Keyshape.HRECT_L

    def build(self):
        poly(self,'triangle',(14,8),(34,24),(14,40),(14,24),(14,8),closed=True)
        line(self,'cathode-top',(34,8),(34,24))
        line(self,'cathode-bottom',(34,24),(34,40))
        line(self,'lead-left',(4,24),(14,24))
        line(self,'lead-right',(34,24),(44,24))
        contacts(self)
