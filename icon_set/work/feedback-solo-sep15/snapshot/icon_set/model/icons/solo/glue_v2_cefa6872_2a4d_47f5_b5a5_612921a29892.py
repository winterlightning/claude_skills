'glue: independent smooth-curve repair.\n\nConstruction: Glue bottle with gently tapered nozzle and a broad rounded body.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/bottle-wine.svg and atomic-debug/bottle-wine.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'cefa6872-2a4d-47f5-b5a5-612921a29892'
SOURCE_PATH = 'pictographic-primitives/design/glue_cefa6872-2a4d-47f5-b5a5-612921a29892.svg'
AUTHOR = 'gpt-6'


class GlueVariant2(Solo48):
    icon_id = 'glue-v2'
    variant_of = 'glue'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('glue', 'design')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'nozzle',(16,20),('L',(21,6)),('C',(22,3.333333333),(26,3.333333333),(27,6)),('L',(32,20)))
        path(self,'body',(16,20),('L',(32,20)),('C',(37,20),(38,23),(38,27)),('L',(40,38)),('C',(40,42),(37,44),(33,44)),('L',(15,44)),('C',(11,44),(8,42),(8,38)),('L',(10,27)),('C',(10,23),(11,20),(16,20)),closed=True)
        contacts(self)
