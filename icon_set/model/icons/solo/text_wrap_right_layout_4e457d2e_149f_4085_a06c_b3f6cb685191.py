"""Text Wrap Right Layout.
Plan: Right-side rectangular object and left/underneath text rules; wide document layout.
References: supplied source; no useful exact Lucide match.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '4e457d2e-149f-4085-a06c-b3f6cb685191'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/lines with small square_4e457d2e-149f-4085-a06c-b3f6cb685191.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'text-wrap-right-layout'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('sub icon', 'text', 'wrap', 'right', 'layout')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        poly('object',(28,8),(44,8),(44,24),(28,24),closed=True)
        line('short-top',(4,8),(18,8));line('short-middle',(4,24),(18,24))
        line('bottom',(4,40),(44,40))
        contacts(self)
