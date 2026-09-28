"""Diagonal key with round lower-left bow and ring hole. Lucide key-round informs a single bow-and-shaft outline; source lacks teeth so none added.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='7f99ed9d-aefc-4d4a-9237-167f01c21fea'
SOURCE_PATH='pictographic-primitives/symbol/state key_7f99ed9d-aefc-4d4a-9237-167f01c21fea.svg'
AUTHOR = 'gpt-6'

class KeyRoundBow(Solo48):
    icon_id='key-round-bow'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords = ('key', 'access', 'unlock', 'password', 'security', 'lock', 'login', 'privacy', 'sub icon')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        self.add_arc('bow',(30,30),(18,18),radius_x=12,large_arc=True)
        self.path('shaft',[(18,18),(30,6),(42,6),(42,18),(30,30)])
        self.relate('connect','bow','shaft')
        self.oval('hole',18,30,3)


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('8d4e51db-4d2a-4285-a400-fd2f7b20a987', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-05/key_8d4e51db-4d2a-4285-a400-fd2f7b20a987.svg')]
