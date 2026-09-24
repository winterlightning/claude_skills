"""Frontal bust enclosed in a square. Shared head/body axis24; head bottom21, shoulder top29: exactly4 units of visible gap.
Symbol plan: shared contour owners and attachment nodes; repeated marks share a spacing parameter.
Omissions: Arm slits and lower closing edge removed to retain open negative space.
Construction: Shared human_ref/user.svg: circular head and open smooth shoulders; Lucide square-parking: rounded outer frame.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='405a762c-b2c7-43c2-8ccd-42ddd4967863'
SOURCE_PATH='pictographic-primitives/_uncategorized_35/square person confined_405a762c-b2c7-43c2-8ccd-42ddd4967863.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='square-person-confined'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('square', 'person', 'confined')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.box('frame',6,6,42,42,4)
        self.circle('head',24,18,3)
        self.add_arc('shoulder-left',(15,33),(24,29),radius_x=9,radius_y=4)
        self.add_arc('shoulder-right',(24,29),(33,33),radius_x=9,radius_y=4)
        self.add_contour('body','shoulder-left','shoulder-right')

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
