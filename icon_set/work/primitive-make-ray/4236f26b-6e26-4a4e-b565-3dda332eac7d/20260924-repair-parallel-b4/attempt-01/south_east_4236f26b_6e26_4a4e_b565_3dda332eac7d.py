"""Compass dial above SE lettering; intentional directional needle asymmetry.
Symbol plan: shared contour owners and attachment nodes; repeated marks share a spacing parameter.
Omissions: Four rim ticks.
Construction: Lucide arrow-down-right: joined directional marks; original reference preserves needle direction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4236f26b-6e26-4a4e-b565-3dda332eac7d'
SOURCE_PATH='pictographic-primitives/_uncategorized_35/south east_4236f26b-6e26-4a4e-b565-3dda332eac7d.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='south-east'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('south', 'east')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.circle('dial',24,16,12)
        self.add_polyline('pointer',(20,17),(28,12),(25,21),closed=True)
        self.path('s',(18,34),[('L',(14,34)),('A',(14,39),3,3,False),('A',(14,44),3,3,True),('L',(10,44))])
        self.add_polyline('e',(38,34),(28,34),(28,39),(28,44),(38,44))
        self.add_line('e-bar',(28,39),(36,39));self.relate('connect','e','e-bar')

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
