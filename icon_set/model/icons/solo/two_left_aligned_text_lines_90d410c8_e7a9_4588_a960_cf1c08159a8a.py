"""Left Aligned Horizontal Text.
Plan: Two horizontal lines share their left origin; lower line is shorter.
References: supplied source; no useful exact Lucide match.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '90d410c8-e7a9-4588-a960-cf1c08159a8a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/comment_90d410c8-e7a9-4588-a960-cf1c08159a8a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-left-aligned-text-lines'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('sub icon', 'two', 'left', 'aligned', 'text', 'lines')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        line('first',(4,8),(44,8))
        line('second',(4,40),(30,40))
        contacts(self)
