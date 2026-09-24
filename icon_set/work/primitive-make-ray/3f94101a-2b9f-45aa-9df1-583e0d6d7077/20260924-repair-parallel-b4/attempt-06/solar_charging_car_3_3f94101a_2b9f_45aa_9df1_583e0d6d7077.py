"""Solar panel and sun beside a tall charging column. Horizontal keyshape allocates more width to the two objects.
Symbol plan: shared contour owners and attachment nodes; repeated marks share a spacing parameter.
Omissions: Sun rays and panel cell grid removed to open spacing.
Construction: Lucide smartphone: smooth column corners; no useful full composition match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3f94101a-2b9f-45aa-9df1-583e0d6d7077'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/solar charging car 3_3f94101a-2b9f-45aa-9df1-583e0d6d7077.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='solar-charging-car-3'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('solar', 'charging', 'car', '3')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.box('charger',18,8,44,40,3)
        self.add_polyline('bolt',(35,17),(27,25),(35,25),(27,31))
        self.circle('sun',7,11,3)
        self.add_polyline('panel',(4,28),(14,28),(16,40),(4,40),closed=True)

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
