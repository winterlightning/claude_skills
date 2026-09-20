"""Circular frame.

Construction reference: circle.
Complete isolated circular main; excludes inner glyphs.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '5237809e-84ca-4d2d-bd80-dd045d692a17'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/circle peso_5237809e-84ca-4d2d-bd80-dd045d692a17.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'circular-frame-solo-5237809e'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('circular-frame',)
    keywords = ('circular', 'frame')

    def build(self):
        circle(self,'rim',24,24,20)
