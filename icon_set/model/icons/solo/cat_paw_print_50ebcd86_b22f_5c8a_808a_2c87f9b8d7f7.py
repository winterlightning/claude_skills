"""Fresh SOLO48 revision of cat-paw-print from the claimed reference.

The original and rejected drawing were compared before this construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
from icon_set.model.icons.solo._payments_batch02 import small_dollar

SOURCE_ICON_ID = '50ebcd86-b22f-5c8a-808a-2c87f9b8d7f7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cat-paw-print/20260927T071330Z-thuan-mac-1/reference/cat-paw-print_50ebcd86-b22f-5c8a-808a-2c87f9b8d7f7.svg'
AUTHOR = "gpt-6"

class CatPawPrint(Solo48):
    icon_id = 'cat-paw-print-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals',)
    aliases = ('feline paw print',)
    keywords = ('cat', 'paw', 'pet', 'kitten', 'footprint', 'animal')

    def build(self) -> None:

        # Rebalance the paw pad and four toes; current drawing is the only source.
        ellipse(self,'pad',24,34,11,8)
        for i,(x,y) in enumerate(((6,20),(16,6),(32,6),(42,20))):
            self.add_dot(f'toe-{i}',(x,y))
