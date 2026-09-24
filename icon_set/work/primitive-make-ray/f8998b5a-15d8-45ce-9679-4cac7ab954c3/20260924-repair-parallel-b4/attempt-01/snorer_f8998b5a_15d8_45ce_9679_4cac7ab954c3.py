"""Sleeping head and shoulder beside a raised blanket; one clear Z. Detached head bottom30 and torso start38 give exactly4 ink gap; deliberate reclining neck bend from reference.
Symbol plan: shared contour owners and attachment nodes; repeated marks share a spacing parameter.
Omissions: Second Z and pillow seam.
Construction: Shared human_ref/user.svg and full_body_ref.png: circular head and coherent body.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f8998b5a-15d8-45ce-9679-4cac7ab954c3'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/snorer_f8998b5a-15d8-45ce-9679-4cac7ab954c3.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='snorer'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('snorer',)
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.circle('head',12,24,6)
        self.add_line('torso',(12,38),(24,42))
        self.mark_human_figure('sleeper',head='head',torso='torso',torso_junction='start')
        self.path('blanket',(24,42),[('L',(27,30)),('A',(31,27),4,4,True),('L',(38,27)),('A',(42,31),4,4,True),('L',(42,42)),('L',(24,42))],True)
        self.relate('connect','torso','blanket')
        self.add_polyline('sleep-z',(32,6),(42,6),(32,14),(42,14))

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
