"""Open shoulder user bust.

Construction reference: human_ref/user.svg.
Detached head/body centerline gap exactly 8; ink gap exactly 4.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '4a672a0c-7986-4e33-83d3-278b80db497b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/profile_4a672a0c-7986-4e33-83d3-278b80db497b.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'open-shoulder-user-bust-solo-4a672a0c'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ('open-shoulder-user-bust',)
    keywords = ('open', 'shoulder', 'user', 'bust')

    def build(self):
        # Shared user reference: head r=6 ends at y=16, shoulders begin y=24.
        circle(self,'head',24,10,6)
        path(self,'shoulders',(8,44),[('L',(8,40)),('A',(24,24),16,16,True),('A',(40,40),16,16,True),('L',(40,44))])
