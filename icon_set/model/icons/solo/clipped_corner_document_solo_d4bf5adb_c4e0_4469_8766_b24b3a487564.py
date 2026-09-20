"""Clipped corner document.

Construction reference: file.
Content is excluded as specified by the main-component brief.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = 'd4bf5adb-c4e0-4469-8766-b24b3a487564'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/a text in file_d4bf5adb-c4e0-4469-8766-b24b3a487564.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'clipped-corner-document-solo-d4bf5adb'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('clipped-corner-document',)
    keywords = ('clipped', 'corner', 'document')

    def build(self):
        # Tall page with one deliberate diagonal corner and equal lower radii.
        path(self,'page',(12,4),[('L',(28,4)),('L',(40,16)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
