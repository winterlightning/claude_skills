"""Hexagonal hardware nut.

Construction reference: circle.
No useful Lucide hardware-nut match; circle construction informs the bore.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '96b72901-1484-4367-8749-22e79938c954'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_28/nut_96b72901-1484-4367-8749-22e79938c954.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'hexagonal-hardware-nut-solo-96b72901'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ('hexagonal-hardware-nut',)
    keywords = ('hexagonal', 'hardware', 'nut')

    def build(self):
        # Mirrored six-sided nut around one centered circular bore.
        self.add_polyline('nut',(14,8),(34,8),(44,24),(34,40),(14,40),(4,24),closed=True)
        circle(self,'bore',24,24,7)
