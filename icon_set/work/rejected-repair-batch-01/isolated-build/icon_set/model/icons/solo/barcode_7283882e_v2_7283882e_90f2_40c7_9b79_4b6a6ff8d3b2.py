'barcode-7283882e: independent smooth-curve repair.\n\nConstruction: Four equally long barcode bars on shared top and bottom baselines.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/barcode.svg and atomic-debug/barcode.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '7283882e-90f2-40c7-9b79-4b6a6ff8d3b2'
SOURCE_PATH = 'pictographic-primitives/shopping/barcode_7283882e-90f2-40c7-9b79-4b6a6ff8d3b2.svg'
AUTHOR = 'gpt-6'


class Barcode7283882eVariant2(Solo48):
    icon_id = 'barcode-7283882e-v2'
    variant_of = 'barcode-7283882e'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('barcode', 'shopping')
    keyshape = Keyshape.HRECT_L

    def build(self):
        for i,x in enumerate((4,17,31,44)):
            line(self,f'bar-{i}',(x,8),(x,40))
        contacts(self)
