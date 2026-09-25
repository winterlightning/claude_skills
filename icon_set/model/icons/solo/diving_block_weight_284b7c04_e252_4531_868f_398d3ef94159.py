'diving-block-weight: independent smooth-curve repair.\n\nConstruction: Diving weight with a semicircular crown and gently rounded base; centered horizontal band.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/weight.svg and atomic-debug/weight.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '284b7c04-e252-4531-868f-398d3ef94159'
SOURCE_PATH = 'pictographic-primitives/recreation/diving block weight_284b7c04-e252-4531-868f-398d3ef94159.svg'
AUTHOR = 'gpt-6'


class DivingBlockWeight(Solo48):
    icon_id = 'diving-block-weight'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'recreation'
    categories = ('primitives', 'recreation')
    aliases = ()
    keywords = ('diving', 'block', 'weight', 'recreation')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'weight',(8,28),('L',(8,20)),('A',16,16,True,(24,4)),('A',16,16,True,(40,20)),('L',(40,28)),('L',(40,38)),('C',(40,42),(33,44),(24,44)),('C',(15,44),(8,42),(8,38)),('L',(8,28)),closed=True)
        line(self,'band',(8,28),(40,28))
        contacts(self)
