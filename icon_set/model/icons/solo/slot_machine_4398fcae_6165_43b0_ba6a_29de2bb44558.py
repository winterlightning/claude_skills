'slot-machine: independent smooth-curve repair.\n\nConstruction: Rounded panel grid; all dividers share exact edge nodes and evenly spaced repeated columns.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/layout-grid.svg and atomic-debug/layout-grid.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '4398fcae-6165-43b0-ba6a-29de2bb44558'
SOURCE_PATH = 'pictographic-primitives/state/slot machine_4398fcae-6165-43b0-ba6a-29de2bb44558.svg'
AUTHOR = 'gpt-6'


class SlotMachine(Solo48):
    icon_id = 'slot-machine'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('slot', 'machine', 'state')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,4,xs=(18,24,30),ys=(18,24,30))
        line(self,"header",(6,18),(42,18))
        line(self,"column",(24,18),(24,42))
        contacts(self)
