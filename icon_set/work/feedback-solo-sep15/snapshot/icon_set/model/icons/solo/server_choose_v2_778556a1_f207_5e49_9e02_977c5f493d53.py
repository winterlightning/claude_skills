'server-choose: independent smooth-curve repair.\n\nConstruction: Three stacked server trays with matching rounded ends and shared horizontal rails.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/server.svg and atomic-debug/server.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '778556a1-f207-5e49-9e02-977c5f493d53'
SOURCE_PATH = 'pictographic-primitives/servers/server choose_778556a1-f207-5e49-9e02-977c5f493d53.svg'
AUTHOR = 'gpt-6'


class ServerChooseVariant2(Solo48):
    icon_id = 'server-choose-v2'
    variant_of = 'server-choose'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'servers'
    aliases = ()
    keywords = ('server', 'choose', 'servers')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'outer',4,8,44,40,6,ys=(18,30))
        line(self,'row-top',(4,18),(44,18));line(self,'row-bottom',(4,30),(44,30))
        contacts(self)
