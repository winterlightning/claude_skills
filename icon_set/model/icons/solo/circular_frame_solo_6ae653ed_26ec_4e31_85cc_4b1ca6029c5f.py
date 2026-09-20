"""Circular frame.

Construction reference: circle.
Complete isolated circular main; excludes inner glyphs.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '6ae653ed-26ec-4e31-85cc-4b1ca6029c5f'
SOURCE_PATH = 'pictographic-primitives/other/circle cursor up_6ae653ed-26ec-4e31-85cc-4b1ca6029c5f.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'circular-frame-solo-6ae653ed'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('circular-frame',)
    keywords = ('circular', 'frame')

    def build(self):
        circle(self,'rim',24,24,20)
