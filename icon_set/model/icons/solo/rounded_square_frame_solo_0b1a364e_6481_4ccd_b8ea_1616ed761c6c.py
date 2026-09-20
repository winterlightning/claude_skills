"""Rounded square frame.

Construction reference: panel-top.
Square outline with equal-radius corners; note excluded.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '0b1a364e-6481-4ccd-b8ea-1616ed761c6c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/music note square_0b1a364e-6481-4ccd-b8ea-1616ed761c6c.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'rounded-square-frame-solo-0b1a364e'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('rounded-square-frame',)
    keywords = ('rounded', 'square', 'frame')

    def build(self):
        box(self,'frame',6,6,42,42,4)
