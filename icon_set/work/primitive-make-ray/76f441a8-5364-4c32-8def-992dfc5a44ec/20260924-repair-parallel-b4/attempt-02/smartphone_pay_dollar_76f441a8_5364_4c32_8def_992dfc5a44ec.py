"""Phone partly behind a tall dollar banknote. Enlarged note to hold currency stroke.
Symbol plan: shared contour owners and attachment nodes; repeated marks share a spacing parameter.
Omissions: Note corner decorations and footer.
Construction: Lucide smartphone and dollar-sign.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='76f441a8-5364-4c32-8def-992dfc5a44ec'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/smartphone pay dollar_76f441a8-5364-4c32-8def-992dfc5a44ec.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='smartphone-pay-dollar'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('smartphone', 'pay', 'dollar')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.path('phone',(18,42),[('L',(10,42)),('A',(6,38),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)])
        self.box('banknote',18,6,42,42,2)
        self.relate('connect','phone','banknote')
        self.path('dollar',(34,16),[('L',(30,16)),('A',(30,24),4,4,False),('A',(30,32),4,4,True),('L',(26,32))])
        self.add_line('dollar-top',(30,14),(30,16));self.relate('connect','dollar-top','dollar')
        self.add_line('dollar-bottom',(30,32),(30,34));self.relate('connect','dollar-bottom','dollar')

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
