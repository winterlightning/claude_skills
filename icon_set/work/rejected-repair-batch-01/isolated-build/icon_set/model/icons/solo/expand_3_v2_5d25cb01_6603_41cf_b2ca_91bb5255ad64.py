'expand-3: independent smooth-curve repair.\n\nConstruction: Four outward arrow tips share two crossing diagonal shafts; paired coordinates.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/expand.svg and atomic-debug/expand.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '5d25cb01-6603-41cf-b2ca-91bb5255ad64'
SOURCE_PATH = 'pictographic-primitives/interface-essential/expand 3_5d25cb01-6603-41cf-b2ca-91bb5255ad64.svg'
AUTHOR = 'gpt-6'


class Expand3Variant2(Solo48):
    icon_id = 'expand-3-v2'
    variant_of = 'expand-3'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('expand', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        line(self,'diagonal-a',(6,6),(42,42));line(self,'diagonal-b',(6,42),(42,6))
        poly(self,'tl',(6,16),(6,6),(16,6));poly(self,'tr',(32,6),(42,6),(42,16))
        poly(self,'bl',(6,32),(6,42),(16,42));poly(self,'br',(32,42),(42,42),(42,32))
        contacts(self)
