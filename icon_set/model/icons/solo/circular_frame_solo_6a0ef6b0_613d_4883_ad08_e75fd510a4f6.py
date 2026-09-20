"""Circular frame.

Construction reference: circle.
Complete isolated circular main; excludes inner glyphs.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '6a0ef6b0-613d-4883-ad08-e75fd510a4f6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/circle colon_6a0ef6b0-613d-4883-ad08-e75fd510a4f6.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'circular-frame-solo-6a0ef6b0'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('circular-frame',)
    keywords = ('circular', 'frame')

    def build(self):
        circle(self,'rim',24,24,20)
