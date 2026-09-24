"""Person seated on a toilet with a checkmark. Head bottom16, torso neck24: exact4 ink gap; head and upper torso share axis20.
Symbol plan: shared contour owners and attachment nodes; repeated marks share a spacing parameter.
Omissions: Tank double wall and folded forearm simplified to coherent strokes.
Construction: Shared human_ref/full_body_ref.png and user.svg: circular head and coherent seated limbs; Lucide toilet: bowl and tank profile.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='2dff611f-5296-466d-ac68-3fd4303496ea'
SOURCE_PATH='pictographic-primitives/_uncategorized_38/toilet use right_2dff611f-5296-466d-ac68-3fd4303496ea.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='toilet-use-right'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('toilet', 'use', 'right')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.circle('head',20,11,5)
        self.add_line('torso',(20,24),(20,32))
        self.add_polyline('leg',(20,32),(32,32),(40,42))
        self.add_line('arm',(20,24),(28,24))
        self.relate('connect','torso','leg');self.relate('connect','torso','arm')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.add_polyline('toilet',(6,24),(6,32),(20,32))
        self.path('bowl',(20,32),[('A',(12,40),8,8,True),('L',(12,42))])
        self.relate('connect','toilet','bowl');self.relate('connect','torso','toilet');self.relate('connect','leg','bowl')
        self.add_polyline('check',(34,12),(38,16),(42,6))

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
