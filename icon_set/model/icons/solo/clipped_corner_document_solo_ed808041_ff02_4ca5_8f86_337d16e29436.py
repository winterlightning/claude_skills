"""Clipped corner document.

Construction reference: file.
Content is excluded as specified by the main-component brief.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = 'ed808041-ff02-4ca5-8f86-337d16e29436'
SOURCE_PATH = '/Applications/Workspaces/pictographic/pg_app_cdn/all_icons/ed808041-ff02-4ca5-8f86-337d16e29436.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'clipped-corner-document-solo-ed808041'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('clipped-corner-document',)
    keywords = ('clipped', 'corner', 'document')

    def build(self):
        # Tall page with one deliberate diagonal corner and equal lower radii.
        path(self,'page',(12,4),[('L',(28,4)),('L',(40,16)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
