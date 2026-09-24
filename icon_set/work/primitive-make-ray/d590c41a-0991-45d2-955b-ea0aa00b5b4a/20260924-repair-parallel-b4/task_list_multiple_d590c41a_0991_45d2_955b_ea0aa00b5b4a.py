"""Two offset task sheets with a prominent completed-task check. Sheet offset8; each rounded corner4.
Symbol plan: shared contour owners and attachment nodes; repeated marks share a spacing parameter.
Omissions: Reduced two checks to one; removed text rules to leave clear interior.
Construction: Lucide list-checks: joined check strokes and consistent repeated spacing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d590c41a-0991-45d2-955b-ea0aa00b5b4a'
SOURCE_PATH='pictographic-primitives/_uncategorized_37/task list multiple_d590c41a-0991-45d2-955b-ea0aa00b5b4a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='task-list-multiple'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('task', 'list', 'multiple')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.path('front',(10,14),[('L',(14,14)),('L',(30,14)),('A',(34,18),4,4,True),('L',(34,34)),('L',(34,38)),('A',(30,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,18)),('A',(10,14),4,4,True)],True)
        self.path('rear',(14,14),[('L',(14,10)),('A',(18,6),4,4,True),('L',(38,6)),('A',(42,10),4,4,True),('L',(42,30)),('A',(38,34),4,4,True),('L',(34,34))])
        self.relate('connect','front','rear')
        self.add_polyline('check',(15,27),(19,31),(25,23))

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
