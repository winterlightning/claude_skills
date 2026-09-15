'water-glass-half-full: independent smooth-curve repair.\n\nConstruction: Water glass with mirrored taper, soft base corners and a level waterline.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/glass-water.svg and atomic-debug/glass-water.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '28cdadb8-cf88-5932-b499-688e483db85e'
SOURCE_PATH = 'pictographic-primitives/drinks/water glass half full_28cdadb8-cf88-5932-b499-688e483db85e.svg'
AUTHOR = 'gpt-6'


class WaterGlassHalfFullVariant2(Solo48):
    icon_id = 'water-glass-half-full-v2'
    variant_of = 'water-glass-half-full'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('water', 'glass', 'half', 'full', 'drinks')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'glass',(8,4),('L',(40,4)),('L',(38,18)),('L',(35,39)),('C',(34.5,42),(32,44),(29,44)),('L',(19,44)),('C',(16,44),(13.5,42),(13,39)),('L',(10,18)),('L',(8,4)),closed=True)
        line(self,'water',(10,18),(38,18))
        contacts(self)
