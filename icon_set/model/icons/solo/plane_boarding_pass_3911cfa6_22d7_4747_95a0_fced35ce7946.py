"""Rounded boarding pass and rising airplane, with open stroked wings. Lucide tickets-plane informs the open aircraft; plane informs swept wings."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3911cfa6-22d7-4747-95a0-fced35ce7946'
SOURCE_PATH = 'pictographic-primitives/travel/plane boarding pass_3911cfa6-22d7-4747-95a0-fced35ce7946.svg'
AUTHOR = 'gpt-6'
PLAN = 'Rounded boarding pass and rising airplane, with open stroked wings. Lucide tickets-plane informs the open aircraft; plane informs swept wings.'
OMISSIONS = ['Text ticks omitted to prioritize aircraft; outlined aircraft reduced to open strokes.']
class Drawing(Solo48):
    icon_id = 'plane-boarding-pass'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('plane', 'boarding', 'pass')
    def build(self):
        self.box('ticket',4,8,44,40)
        self.add_polyline('fuselage',(15,27),(19,31),(27,25),(35,19))
        self.add_polyline('wings',(20,17),(27,25),(27,31))
        self.relate('connect','fuselage','wings')


    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)
    def box(self,n,l,t,r,b,rad=3):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        members=[]
        for i,a in enumerate(pts):
            z=pts[(i+1)%8]; p=n+str(i)
            if i%2:self.add_arc(p,a,z,radius_x=rad)
            else:self.add_line(p,a,z)
            members.append(p)
        self.add_contour(n,*members,closed=True)
