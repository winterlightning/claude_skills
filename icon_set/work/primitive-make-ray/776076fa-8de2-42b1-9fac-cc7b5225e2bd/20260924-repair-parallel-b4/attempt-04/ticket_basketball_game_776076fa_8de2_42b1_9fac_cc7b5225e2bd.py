"""Basketball upper hemisphere behind a broad notched ticket;16-radius ball sectors and20-high ticket preserve openings.
Symbol plan: shared contour owners and attachment nodes; repeated marks share a spacing parameter.
Omissions: Small detached circle, extra ball seam and ticket text; ticket made level to enlarge its opening.
Construction: Lucide ticket: opposed inward notches and a coherent perimeter.
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
        self.path('ball',(38,22),[('A',(22,6),16,16,False),('A',(6,22),16,16,False)])
        self.path('ball-meridian',(22,6),[('A',(27,14),5,8,True),('A',(22,22),5,8,True)])
        self.path('ball-seam',(6,22),[('B',(27,14),(16,22),(22,18)),('B',(22,6),(27,10),(25,8))])
        self.relate('connect','ball-seam','ball-meridian');self.relate('connect','ball-seam','ball');self.relate('connect','ball-seam','ticket')
        self.path('ticket',(6,22),[('L',(22,22)),('L',(38,22)),('L',(42,22)),('L',(42,30)),('A',(42,34),2,2,False),('L',(42,42)),('L',(6,42)),('L',(6,34)),('A',(6,30),2,2,False),('L',(6,22))],True)
        self.relate('connect','ball','ticket');self.relate('connect','ball','ball-meridian');self.relate('connect','ticket','ball-meridian')

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
