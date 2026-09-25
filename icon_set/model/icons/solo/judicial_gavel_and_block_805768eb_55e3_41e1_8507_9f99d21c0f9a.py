"""Judicial Gavel and Sounding Block.
Plan: Diagonal rectangular hammer head, long handle, and separate low sounding block.
References: supplied source; Lucide original and atomic-debug gavel.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '805768eb-55e3-41e1-8507-9f99d21c0f9a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/judge_805768eb-55e3-41e1-8507-9f99d21c0f9a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'judicial-gavel-and-block'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('sub icon', 'judicial', 'gavel', 'and', 'block')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        poly('head',(6,17),(18,6),(30,18),(18,30),closed=True)
        line('handle',(24,24),(42,42))
        poly('block',(6,42),(6,38),(20,38),(20,42))
        contacts(self)
