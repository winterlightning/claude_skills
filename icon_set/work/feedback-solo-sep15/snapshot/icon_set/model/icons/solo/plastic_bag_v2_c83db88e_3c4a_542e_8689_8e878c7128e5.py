'plastic-bag: independent smooth-curve repair.\n\nConstruction: Plastic carrier with rounded handles and a broad integrated body; mirrored handle notch.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/shopping-bag.svg and atomic-debug/shopping-bag.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'c83db88e-3c4a-542e-8689-8e878c7128e5'
SOURCE_PATH = 'pictographic-primitives/ecology/plastic bag_c83db88e-3c4a-542e-8689-8e878c7128e5.svg'
AUTHOR = 'gpt-6'


class PlasticBagVariant2(Solo48):
    icon_id = 'plastic-bag-v2'
    variant_of = 'plastic-bag'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'ecology'
    aliases = ()
    keywords = ('plastic', 'bag', 'ecology')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'bag',(8,38),('L',(10,8)),('C',(10,5),(12,4),(15,4)),('L',(18,4)),('L',(18,12)),('A',6,6,False,(24,18)),('A',6,6,False,(30,12)),('L',(30,4)),('L',(33,4)),('C',(36,4),(38,5),(38,8)),('L',(40,38)),('C',(40,42),(37,44),(33,44)),('L',(15,44)),('C',(11,44),(8,42),(8,38)),closed=True)
        contacts(self)
