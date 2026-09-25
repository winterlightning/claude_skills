"""Horned Bull Head Symbol.
Plan: Broad symmetric bull face, tapered muzzle and upward horns. Omit eyes to protect negative space.
References: supplied source; no useful exact Lucide match.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '749c49e8-3491-46dc-9c16-62b4f5a5ab0c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/goat head_749c49e8-3491-46dc-9c16-62b4f5a5ab0c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horned-bull-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sub icon', 'horned', 'bull', 'head')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        path('face',(12,24),('C',(12,13),(36,13),(36,24)),('L',(36,32)),('L',(29,37)),('L',(29,39)),('A',5,5,True,(19,39)),('L',(19,37)),('L',(12,32)),('L',(12,24)),closed=True)
        path('horn-left',(12,24),('C',(8,23),(8,20),(8,16)),('L',(8,4)))
        path('horn-right',(36,24),('C',(40,23),(40,20),(40,16)),('L',(40,4)))
        contacts(self)
