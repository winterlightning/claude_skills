'logistic-weight: independent smooth-curve repair.\n\nConstruction: Trapezoidal weight with a circular lifting eye and softly rounded lower corners.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/weight.svg and atomic-debug/weight.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '5e5822a7-dae5-5da9-ba63-90a30a651229'
SOURCE_PATH = 'pictographic-primitives/shipping/logistic weight_5e5822a7-dae5-5da9-ba63-90a30a651229.svg'
AUTHOR = 'gpt-6'


class LogisticWeight(Solo48):
    icon_id = 'logistic-weight'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    categories = ('primitives', 'shipping')
    aliases = ()
    keywords = ('logistic', 'weight', 'shipping')
    keyshape = Keyshape.VRECT_L

    def build(self):
        ellipse(self,'eye',24,10,6)
        path(self,'body',(14,16),('L',(24,16)),('L',(34,16)),('L',(40,39)),('C',(40,42),(38,44),(35,44)),('L',(13,44)),('C',(10,44),(8,42),(8,39)),('L',(14,16)),closed=True)
        contacts(self)
