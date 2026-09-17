"""Geometric Animal Paw Print.
Plan: Three equal circles and one triangular pad; mirrored toes and centered triangle.
References: supplied source; no useful exact Lucide match.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '52860099-ee8d-46b2-84ff-237a2c5f681c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/paw print_52860099-ee8d-46b2-84ff-237a2c5f681c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'geometric-three-toed-paw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/container-components'
    aliases = ()
    keywords = ('sub icon', 'geometric', 'three', 'toed', 'paw')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        circle('top-toe',24,10,4)
        circle('left-toe',10,22,4)
        circle('right-toe',38,22,4)
        poly('pad',(24,26),(12,42),(36,42),closed=True)
        contacts(self)
