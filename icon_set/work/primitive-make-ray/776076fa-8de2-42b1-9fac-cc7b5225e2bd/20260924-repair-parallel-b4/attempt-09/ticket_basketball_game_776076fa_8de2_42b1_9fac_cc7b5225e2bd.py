"""Enlarged basketball upper hemisphere with two seams behind a notched ticket.
Symbol plan: shared contour owners and attachment nodes; repeated marks share a spacing parameter.
Omissions: Small detached circle and ticket text; shallow notches retain eight-unit space to top and bottom.
Construction: Lucide ticket: notched admission outline; source basketball seam structure.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='776076fa-8de2-42b1-9fac-cc7b5225e2bd'
SOURCE_PATH='pictographic-primitives/_uncategorized_37/ticket basketball game_776076fa-8de2-42b1-9fac-cc7b5225e2bd.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='ticket-basketball-game'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('ticket', 'basketball', 'game')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.path('ball',(42,24),[('A',(24,6),18,18,False),('A',(6,24),18,18,False)])
        self.path('ball-meridian',(24,6),[('A',(18,15),6,9,False),('A',(24,24),6,9,False)])
        self.path('ball-seam',(18,15),[('B',(42,24),(27,15),(37,15))])
        self.path('ticket',(6,24),[('L',(24,24)),('L',(42,24)),('L',(42,32)),('A',(42,34),1,1,False),('L',(42,42)),('L',(6,42)),('L',(6,34)),('A',(6,32),1,1,False),('L',(6,24))],True)
        for a,b in [('ball','ticket'),('ball','ball-meridian'),('ticket','ball-meridian'),('ball-seam','ball-meridian'),('ball-seam','ball'),('ball-seam','ticket')]:self.relate('connect',a,b)

    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)
    def box(self,n,l,t,r,b,rad=3):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
    def path(self,n,start,ops,closed=False):
        p=start;members=[]
        for i,op in enumerate(ops):
            name=f'{n}-{i}';end=op[1]
            if op[0]=='L':self.add_line(name,p,end)
            elif op[0]=='A':self.add_arc(name,p,end,radius_x=op[2],radius_y=op[3],sweep=op[4])
            elif op[0]=='B':self.add_bezier(name,p,(op[2],op[3],end))
            members.append(name);p=end
        if closed and p!=start:
            self.add_line(n+'-close',p,start);members.append(n+'-close')
        self.add_contour(n,*members,closed=closed)
