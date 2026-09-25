"""Airplane Flying Over Globe.
Plan: Open globe behind a diagonal passenger airplane; equator and meridian preserve globe identity.
References: supplied source; Lucide original and atomic-debug plane, earth.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = 'edb3fdfa-2f3d-4eac-81a5-1655e873407e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/globe plane_edb3fdfa-2f3d-4eac-81a5-1655e873407e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'airplane-flying-over-globe'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('sub icon', 'airplane', 'flying', 'over', 'globe')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        circle('globe',16,16,10)
        poly('latitude',(6,16),(16,16),(26,16))
        poly('longitude',(16,6),(16,16),(16,26))
        poly('fuselage',(28,42),(34,36),(42,28))
        poly('wings',(27,31),(34,36),(40,42))
        line('tail',(24,42),(28,42))
        contacts(self)
