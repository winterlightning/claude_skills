'Circular head and curved shoulders separated from a wide desk with splayed legs.'
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='1461f130-1461-5759-8ff2-8de25b9591b9'
SOURCE_PATH='pictographic-primitives/users/neutral podium_1461f130-1461-5759-8ff2-8de25b9591b9.svg'
AUTHOR='gpt-6'
PLAN='Circular head and curved shoulders separated from a wide desk with splayed legs.'
CONSTRUCTION_REFERENCE='human_ref/user.svg: circular head and arched shoulders; source desk separation.'
class Drawing(Solo48):
    icon_id='person-behind-desk'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('neutral', 'podium')
    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,start,commands,closed=False):
        ids=[];here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid);here=end
        self.add_contour(n,*ids,closed=closed)

    def box(self,n,l,t,r,b,rad=4):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def file(self,l=8,t=4,r=40,b=44):
        self.path('page',(l+4,t),[('L',(r-10,t)),('L',(r,t+10)),('L',(r,b-4)),('A',(r-4,b),4,4,True),('L',(l+4,b)),('A',(l,b-4),4,4,True),('L',(l,t+4)),('A',(l+4,t),4,4,True)],True)

    def build(self):
        self.circle('head',24,9,5)
        self.path('shoulders',(14,28),[('C',(24,22),(14,24),(19,22)),('C',(34,28),(29,22),(34,24))])
        self.add_polyline('desk',(8,36),(12,36),(36,36),(40,36))
        for n,x,end in [('left',12,10),('right',36,38)]:
            self.add_line(n+'-leg',(x,36),(end,44));self.relate('connect','desk',n+'-leg')

# Keyshape: VRECT_L accommodates head, shoulders, table clearance and splayed legs.
# Visual review: Shoulders are separated from the tabletop as in the reference; equal splayed legs and centered head.
OMISSIONS='No defining parts omitted; shoulder mass reduced to an open arch.'
HUMAN_REVIEW={'reference': 'icon_set/references/human_ref/user.svg', 'head_center': [24, 9], 'radius': 5, 'shoulder_top': [24, 22], 'centerline_gap': 8, 'ink_gap': 4, 'proof': '22-(9+5)=8. Symmetric shoulder curves attain their nearest point at their top junction.'}
