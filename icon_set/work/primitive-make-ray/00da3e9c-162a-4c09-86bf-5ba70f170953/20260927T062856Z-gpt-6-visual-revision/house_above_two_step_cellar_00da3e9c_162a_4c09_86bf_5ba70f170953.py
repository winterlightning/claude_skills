"""Fresh SOLO48 revision of house-above-two-step-cellar from its claimed original reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '00da3e9c-162a-4c09-86bf-5ba70f170953'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__house-above-two-step-cellar/20260927T061852Z-thuan-mac-1/reference/cellar_00da3e9c-162a-4c09-86bf-5ba70f170953.svg'
AUTHOR = "gpt-6"

class HouseAboveTwoStepCellar(Solo48):
    icon_id = 'house-above-two-step-cellar'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('house', 'above', 'two-step', 'cellar')

    def build(self) -> None:

        # Gabled house, square window and two broad cellar steps.
        poly(self,'roof',(14,17),(26,6),(38,17))
        poly(self,'house',(14,17),(14,27),(38,27),(38,17))
        poly(self,'window',(23,17),(29,17),(29,23),(23,23),closed=True)
        poly(self,'cellar',(6,27),(6,34),(22,34),(22,42),(42,42),(42,27),(38,27))
        contacts(self)
