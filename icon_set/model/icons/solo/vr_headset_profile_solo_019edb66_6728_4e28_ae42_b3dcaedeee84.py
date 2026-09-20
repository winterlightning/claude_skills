"""Vr headset profile.

Construction reference: human_ref/user.svg.
Continuous profile neck; no detached-head gap applies. Visor and nose retain direction.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '019edb66-6728-4e28-ae42-b3dcaedeee84'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/vr headset 1_019edb66-6728-4e28-ae42-b3dcaedeee84.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'vr-headset-profile-solo-019edb66'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('vr-headset-profile',)
    keywords = ('vr', 'headset', 'profile')

    def build(self):
        # Head silhouette and visor share a real strap join; left-facing profile.
        path(self,'head',(18,14),[('A',(28,6),10,8,True),('A',(42,20),14,14,True),('L',(42,26)),('A',(32,36),10,10,True),('L',(32,42))])
        box(self,'visor',6,14,26,26,4,nodes=((18,14),(14,26),(26,20)))
        self.add_line('strap',(26,20),(42,20))
        self.relate('connect','head','visor')
        self.relate('connect','strap','head')
        self.relate('connect','strap','visor')
        self.add_polyline('face',(14,26),(10,34),(18,34),(18,42))
        self.relate('connect','face','visor')
