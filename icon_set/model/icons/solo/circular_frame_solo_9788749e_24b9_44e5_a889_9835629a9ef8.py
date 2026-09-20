"""Circular frame.

Construction reference: circle.
Complete isolated circular main; excludes inner glyphs.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '9788749e-24b9-44e5-a889-9835629a9ef8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/pg_app_cdn/all_icons/9788749e-24b9-44e5-a889-9835629a9ef8.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'circular-frame-solo-9788749e'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('circular-frame',)
    keywords = ('circular', 'frame')

    def build(self):
        circle(self,'rim',24,24,20)
