"""Fresh SOLO48 revision of house-above-stepped-cellar from its claimed original reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '66d61c39-06d6-41c2-a9d1-44513486e148'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__house-above-stepped-cellar/20260927T061852Z-thuan-mac-1/reference/cellar 2_66d61c39-06d6-41c2-a9d1-44513486e148.svg'
AUTHOR = 'gpt-6'

class HouseAboveSteppedCellar(Solo48):
    icon_id = 'house-above-stepped-cellar'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('house', 'above', 'stepped', 'cellar')

    def build(self) -> None:

        # Gabled house, square window and three-step cellar.
        poly(self,'roof',(14,17),(26,6),(38,17))
        poly(self,'house',(14,17),(14,27),(38,27),(38,17))
        poly(self,'window',(23,17),(29,17),(29,23),(23,23),closed=True)
        poly(self,'cellar',(6,18),(6,27),(14,27),(14,34),(22,34),(22,42),
             (42,42),(42,27),(38,27))
        contacts(self)
