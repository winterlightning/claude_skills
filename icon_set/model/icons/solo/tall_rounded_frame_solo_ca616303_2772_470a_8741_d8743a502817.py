"""Tall rounded frame.

Construction reference: smartphone.
Tall empty main; temperature content excluded.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = 'ca616303-2772-470a-8741-d8743a502817'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/rectangle uv high_ca616303-2772-470a-8741-d8743a502817.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'tall-rounded-frame-solo-ca616303'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('tall-rounded-frame',)
    keywords = ('tall', 'rounded', 'frame')

    def build(self):
        box(self,'frame',10,4,38,44,4)
