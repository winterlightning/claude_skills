"""Biometric Fingerprint Identification.
Plan: Nested fingertip arches and interrupted ridge tails; shared axis and clear ridge spacing.
References: supplied source; no useful exact Lucide match.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '18f6118d-0b0a-4a7b-89e0-52ba5abbcb54'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/fingerprint_18f6118d-0b0a-4a7b-89e0-52ba5abbcb54.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'biometric-fingerprint'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/container-components'
    aliases = ()
    keywords = ('sub icon', 'biometric', 'fingerprint')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        path('outer',(6,30),('L',(6,24)),('A',18,18,True,(42,24)),('L',(42,30)))
        path('inner',(14,36),('C',(16,30),(15,24),(16,22)),('C',(16,13),(33,13),(33,22)),('L',(33,30)),('C',(33,36),(34,39),(36,42)))
        path('ridge',(24,26),('C',(24,32),(24,38),(20,42)))
        contacts(self)
