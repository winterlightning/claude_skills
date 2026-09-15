'gas-symbol: independent smooth-curve repair.\n\nConstruction: Bottle with a short neck, equal shoulder transitions and rounded heel.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/bottle-wine.svg and atomic-debug/bottle-wine.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'c6b95b7c-51f0-41d6-9758-e2c0e4821afa'
SOURCE_PATH = 'pictographic-primitives/symbol/gas_c6b95b7c-51f0-41d6-9758-e2c0e4821afa.svg'
AUTHOR = 'gpt-6'


class GasSymbolVariant2(Solo48):
    icon_id = 'gas-symbol-v2'
    variant_of = 'gas-symbol'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('gas', 'symbol')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'bottle',(19,4),('L',(29,4)),('L',(29,12)),('C',(29,17),(40,17),(40,24)),('L',(40,39)),('A',5,5,True,(35,44)),('L',(13,44)),('A',5,5,True,(8,39)),('L',(8,24)),('C',(8,17),(19,17),(19,12)),('L',(19,4)),closed=True)
        contacts(self)
