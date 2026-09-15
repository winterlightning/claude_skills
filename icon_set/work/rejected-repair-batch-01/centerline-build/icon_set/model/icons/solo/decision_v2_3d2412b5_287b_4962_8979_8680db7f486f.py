'decision: independent smooth-curve repair.\n\nConstruction: A clean centered diamond; intentional directional vertices remain crisp and equal.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/diamond.svg and atomic-debug/diamond.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '3d2412b5-287b-4962-8979-8680db7f486f'
SOURCE_PATH = 'pictographic-primitives/design/decision_3d2412b5-287b-4962-8979-8680db7f486f.svg'
AUTHOR = 'gpt-6'


class DecisionVariant2(Solo48):
    icon_id = 'decision-v2'
    variant_of = 'decision'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('decision', 'design')
    keyshape = Keyshape.HRECT_L

    def build(self):
        poly(self,'diamond',(24,8),(44,24),(24,40),(4,24),closed=True)
        contacts(self)
