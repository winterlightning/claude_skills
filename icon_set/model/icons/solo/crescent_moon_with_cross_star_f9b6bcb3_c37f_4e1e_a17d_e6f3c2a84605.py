"""Crescent Moon and Plus Sign.
Plan: Crescent night moon and a four-armed star in its opening; the cross is a celestial star per saved brief.
References: supplied source; Lucide original and atomic-debug moon-star.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = 'f9b6bcb3-c37f-4e1e-a17d-e6f3c2a84605'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/night_f9b6bcb3-c37f-4e1e-a17d-e6f3c2a84605.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crescent-moon-with-cross-star'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('sub icon', 'crescent', 'moon', 'with', 'cross', 'star')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        path('moon',(26,6),('C',(14,6),(6,14),(6,26)),('C',(6,36),(14,42),(24,42)),('C',(32,42),(38,38),(42,30)),('C',(29,35),(17,21),(26,6)),closed=True)
        poly('star-horizontal',(33,14),(38,14),(42,14))
        poly('star-vertical',(38,10),(38,14),(38,18))
        contacts(self)
