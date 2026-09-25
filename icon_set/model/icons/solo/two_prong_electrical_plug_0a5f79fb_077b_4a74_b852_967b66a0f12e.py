"""Two Prong Electrical Plug.
Plan: Two equal plug pins, bowl-shaped plug body and short central cord.
References: supplied source; Lucide original and atomic-debug plug.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '0a5f79fb-077b-4a74-b852-967b66a0f12e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/plug_0a5f79fb-077b-4a74-b852-967b66a0f12e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-prong-electrical-plug'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sub icon', 'two', 'prong', 'electrical', 'plug')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        path('body',(8,16),('L',(16,16)),('L',(32,16)),('L',(40,16)),('L',(40,25)),('A',16,11,True,(24,36)),('A',16,11,True,(8,25)),('L',(8,16)),closed=True)
        line('left-pin',(16,4),(16,16));line('right-pin',(32,4),(32,16))
        line('cord',(24,36),(24,44))
        contacts(self)
