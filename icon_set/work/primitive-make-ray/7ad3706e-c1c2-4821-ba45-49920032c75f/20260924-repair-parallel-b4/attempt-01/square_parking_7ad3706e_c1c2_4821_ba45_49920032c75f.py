"""Parking P centered inside a rounded square. Shared bowl attachment heights15 and27.
Symbol plan: shared contour owners and attachment nodes; repeated marks share a spacing parameter.
Omissions: Double outline on the letter replaced with a single stroke to preserve the counter.
Construction: Lucide square-parking: continuous P stem and rounded bowl within a square.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7ad3706e-c1c2-4821-ba45-49920032c75f'
SOURCE_PATH='pictographic-primitives/_uncategorized_35/square parking_7ad3706e-c1c2-4821-ba45-49920032c75f.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='square-parking'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('square', 'parking')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.box('frame',6,6,42,42,5)
        self.add_polyline('p-stem',(16,33),(16,27),(16,15))
        self.path('p-bowl',(16,15),[('L',(26,15)),('A',(26,27),6,6,True),('L',(16,27))])
        self.relate('connect','p-stem','p-bowl')

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
