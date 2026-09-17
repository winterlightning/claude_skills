"""Simple Human Figure Symbol.
Plan: Circular head and compact shirt-like body with short squared sleeves and tapered base; exact head gap.
References: supplied source; no useful exact Lucide match.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = 'de7e132d-7335-404c-ba94-0dc5f8acf724'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/full body person_de7e132d-7335-404c-ba94-0dc5f8acf724.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-human-figure'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/container-components'
    aliases = ()
    keywords = ('sub icon', 'standing', 'human', 'figure')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        circle('head',24,10,6)
        path('body',(10,32),('A',14,8,True,(24,24)),('A',14,8,True,(38,32)),('L',(38,35)),('L',(32,35)),('L',(30,44)),('L',(18,44)),('L',(16,35)),('L',(10,35)),('L',(10,32)),closed=True)
        contacts(self)
