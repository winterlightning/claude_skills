"""Person in Car Seat.
Plan: Seated figure with circular head, bent knees and supporting seat back; exact detached head gap.
References: supplied source; no useful exact Lucide match.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '6ecd4032-1f65-4fa1-8af7-1cf770b292d3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/person with seat_6ecd4032-1f65-4fa1-8af7-1cf770b292d3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-in-car-seat'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('sub icon', 'person', 'in', 'car', 'seat')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        path('head',(24,16),('A',5,5,True,(24,6)),('A',5,5,True,(24,16)),closed=True)
        line('torso',(24,24),(24,32))
        poly('legs',(24,32),(34,32),(42,40))
        poly('arm',(24,24),(33,24),(39,18))
        path('seat',(6,23),('L',(6,34)),('A',8,8,False,(14,42)),('L',(32,42)))
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        contacts(self)
