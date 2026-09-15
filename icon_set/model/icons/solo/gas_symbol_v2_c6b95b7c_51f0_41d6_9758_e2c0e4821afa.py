'gas-symbol: distinct review variant.\n\nConstruction: Gas cylinder with a round lower bowl and a broad horizontal belt; separate it from the flat-bottom liquid bottle.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nConstruction reference: bottle-wine from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'c6b95b7c-51f0-41d6-9758-e2c0e4821afa'
SOURCE_PATH = 'pictographic-primitives/symbol/gas_c6b95b7c-51f0-41d6-9758-e2c0e4821afa.svg'
AUTHOR = 'gpt-6'


class GasSymbolVariant2(Solo48):
    icon_id = 'gas-symbol-v2'
    variant_of = 'gas-symbol'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('gas', 'symbol')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'cylinder',(18,4),('L',(30,4)),('L',(30,12)),('C',(30,16),(40,16),(40,24)),('L',(40,30)),('L',(40,34)),('A',16,10,True,(24,44)),('A',16,10,True,(8,34)),('L',(8,30)),('L',(8,24)),('C',(8,16),(18,16),(18,12)),('L',(18,4)),closed=True)
        line(self,'belt',(8,30),(40,30))
        contacts(self)
