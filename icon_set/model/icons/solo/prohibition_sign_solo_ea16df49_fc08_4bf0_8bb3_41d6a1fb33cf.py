"""Prohibition Sign Symbol.
Plan: Circle with a continuous diagonal strike; shared endpoints at integer circle points.
References: supplied source; no useful exact Lucide match.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = 'ea16df49-fc08-4bf0-8bb3-41d6a1fb33cf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/prohitbition_ea16df49-fc08-4bf0-8bb3-41d6a1fb33cf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'prohibition-sign-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('sub icon', 'prohibition', 'sign', 'solo')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        path('ring',(12,8),('A',20,20,True,(40,12)),('A',20,20,True,(36,40)),('A',20,20,True,(8,36)),('A',20,20,True,(12,8)),closed=True)
        line('slash',(8,36),(40,12))
        contacts(self)
