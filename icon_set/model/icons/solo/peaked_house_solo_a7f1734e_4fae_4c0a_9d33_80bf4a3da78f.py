"""Peaked house.

Construction reference: house.
Only the isolated house; excludes paw/lock content.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = 'a7f1734e-4fae-4c0a-9d33-80bf4a3da78f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/house lock_a7f1734e-4fae-4c0a-9d33-80bf4a3da78f.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'peaked-house-solo-a7f1734e'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('peaked-house',)
    keywords = ('peaked', 'house')

    def build(self):
        # Symmetric roof and equal walls; rounded lower corners.
        path(self,'house',(24,4),[('L',(40,18)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,18)),('L',(24,4))],True)
