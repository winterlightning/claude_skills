"""Minimalist Happy Smiling Face.
Plan: Two vertical eyes above one broad smile, without added face enclosure.
References: supplied source; Lucide original and atomic-debug smile.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = 'b3826549-0cc8-4855-a250-66873df772a9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/smiley face_b3826549-0cc8-4855-a250-66873df772a9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'minimal-happy-smiling-face'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sub icon', 'minimal', 'happy', 'smiling', 'face')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        line('left-eye',(12,8),(12,14));line('right-eye',(36,8),(36,14))
        path('smile',(4,26),('A',20,14,False,(44,26)))
        contacts(self)
