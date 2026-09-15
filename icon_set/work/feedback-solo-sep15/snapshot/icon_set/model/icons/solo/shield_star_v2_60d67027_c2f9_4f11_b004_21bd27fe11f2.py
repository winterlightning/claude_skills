'shield-star: independent smooth-curve repair.\n\nConstruction: Shield with a smooth domed top and a coherent curved lower bowl; centered detail kept spacious.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/shield.svg and atomic-debug/shield.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '60d67027-c2f9-4f11-b004-21bd27fe11f2'
SOURCE_PATH = 'pictographic-primitives/protection/shield star_60d67027-c2f9-4f11-b004-21bd27fe11f2.svg'
AUTHOR = 'gpt-6'


class ShieldStarVariant2(Solo48):
    icon_id = 'shield-star-v2'
    variant_of = 'shield-star'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('shield', 'star', 'protection')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'shield',(8,9),('C',(17,2.333333333),(31,2.333333333),(40,9)),('L',(40,27)),('C',(40,35),(32,41),(24,44)),('C',(16,41),(8,35),(8,27)),('L',(8,9)),closed=True)
        poly(self,"star",(24,14),(27,20),(31,21),(28,25),(29,30),(24,28),(19,30),(20,25),(17,21),(21,20),closed=True)
        contacts(self)
