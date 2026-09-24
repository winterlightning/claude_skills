"""Sailboat with clockwise transfer arrows above-right and below-left.
Symbol plan: shared contour owners and attachment nodes; repeated marks share a spacing parameter.
Omissions: Wave extension omitted; hull curve retains nautical silhouette.
Construction: Lucide arrow-down-right: shared arrow endpoints; supplied boat reference retains directional arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='79b63fb3-53d2-42aa-af62-afdbc09d4964'
SOURCE_PATH='pictographic-primitives/_uncategorized_38/transportation ticket boat transfer_79b63fb3-53d2-42aa-af62-afdbc09d4964.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='transportation-ticket-boat-transfer'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('transportation', 'ticket', 'boat', 'transfer')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_polyline('sail',(6,22),(18,6),(18,22),(18,30))
        self.add_line('sail-foot',(6,22),(18,22));self.relate('connect','sail','sail-foot')
        self.path('hull',(6,30),[('L',(18,30)),('L',(30,30)),('A',(18,38),12,8,True),('A',(6,30),12,8,True)],True)
        self.relate('connect','sail','hull')
        self.path('transfer-top',(32,10),[('A',(42,20),10,10,True)])
        self.add_polyline('arrow-top',(36,16),(42,20),(42,12));self.relate('connect','transfer-top','arrow-top')
        self.path('transfer-bottom',(34,42),[('A',(42,34),8,8,False)])
        self.add_polyline('arrow-bottom',(36,34),(42,34),(42,40));self.relate('connect','transfer-bottom','arrow-bottom')

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
