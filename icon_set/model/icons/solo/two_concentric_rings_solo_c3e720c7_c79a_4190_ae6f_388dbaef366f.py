"""Two concentric rings.

Construction reference: circle.
Two rings with a broad 8-unit visible band.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = 'c3e720c7-c79a-4190-ae6f-388dbaef366f'
SOURCE_PATH = 'pictographic-primitives/other/ripple_c3e720c7-c79a-4190-ae6f-388dbaef366f.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'two-concentric-rings-solo-c3e720c7'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('two-concentric-rings',)
    keywords = ('two', 'concentric', 'rings')

    def build(self):
        circle(self,'outer',24,24,20)
        circle(self,'inner',24,24,8)
