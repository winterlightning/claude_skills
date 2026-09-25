"""Happy Smiling Face.
Plan: Two mirrored arched eyes and a wide smile, without an enclosing face circle.
References: supplied source; Lucide original and atomic-debug smile.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '5ee1d8ff-a85e-4f98-8d10-414df21c0f8a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/smiley face_5ee1d8ff-a85e-4f98-8d10-414df21c0f8a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'happy-face-with-closed-eyes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sub icon', 'happy', 'face', 'with', 'closed', 'eyes')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        path('left-eye',(6,14),('A',6,8,True,(18,14)))
        path('right-eye',(30,14),('A',6,8,True,(42,14)))
        path('smile',(8,28),('A',16,14,False,(40,28)))
        contacts(self)
