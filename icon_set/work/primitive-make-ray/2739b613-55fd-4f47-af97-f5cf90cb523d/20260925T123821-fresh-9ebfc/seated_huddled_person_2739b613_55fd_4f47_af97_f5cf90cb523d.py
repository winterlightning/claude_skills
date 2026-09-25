'Huddled seated person with rounded back, arms over knees and one extended lower leg.'
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='2739b613-55fd-4f47-af97-f5cf90cb523d'
SOURCE_PATH='pictographic-primitives/other/poverty person_2739b613-55fd-4f47-af97-f5cf90cb523d.svg'
AUTHOR='gpt-6'
PLAN='Huddled seated person with rounded back, arms over knees and one extended lower leg.'
CONSTRUCTION_REFERENCE='human_ref/full_body_ref.png: seated pose and round-ended limbs; supplied huddled action.'
class Drawing(Solo48):
    icon_id='seated-huddled-person'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('poverty', 'person')
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
        self.circle('head',24,10,6)
        self.path('torso',(24,24),[('C',(8,36),(24,28),(8,28)),('A',(16,44),8,8,False),('L',(18,44))])
        self.add_polyline('arm',(24,24),(36,24),(30,30))
        self.add_polyline('legs',(18,44),(30,30),(40,44))
        for a,b in [('torso','arm'),('torso','legs'),('arm','legs')]:self.relate('connect',a,b)
        self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')

# Keyshape: VRECT_L gives a round head above the folded seated body.
# Visual review: Rounded hunched back and arms over the folded knees replace the box-like torso. Head follows the vertical tangent at the actual upper torso junction.
OMISSIONS='Outlined clothing/body mass reduced to the shared human line vocabulary; no fingers or facial detail.'
HUMAN_REVIEW={'reference': 'icon_set/references/human_ref/full_body_ref.png', 'head_center': [24, 10], 'radius': 6, 'torso_junction': [24, 24], 'centerline_gap': 8, 'ink_gap': 4, 'proof': '24-(10+6)=8. Upper torso has a vertical tangent at the junction, continuing toward the head; torso then curls left and down.'}
