"""Animal Paw Print.
Plan: Three circular toe pads above a smooth rounded central pad; bilateral symmetry.
References: supplied source; no useful exact Lucide match.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '162eae61-5c7a-4f66-b659-3f2fbd11c0a5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/paw print_162eae61-5c7a-4f66-b659-3f2fbd11c0a5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-toed-animal-paw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sub icon', 'three', 'toed', 'animal', 'paw')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        circle('toe-top',24,10,4)
        circle('toe-left',10,19,4)
        circle('toe-right',38,19,4)
        path('pad',(24,27),('C',(19,27),(20,32),(15,34)),('C',(6,42),(15,42),(24,42)),('C',(33,42),(42,42),(33,34)),('C',(28,32),(29,27),(24,27)),closed=True)
        contacts(self)
