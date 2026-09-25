from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='fc535717-5e07-564a-aad9-923ace667ffb'
SOURCE_PATH='pictographic-primitives/holidays/star_fc535717-5e07-564a-aad9-923ace667ffb.svg'
AUTHOR='gpt-6'
PLAN='Crisp star and ribbon retained; user accepts the inset star-to-medal clearance exception.'
CONSTRUCTION_REFERENCES='Lucide star original and atomic-debug: alternating points and valleys with a common vertical axis.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='star'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'holidays'
    aliases=()
    keywords=('star',)

    def path(self,n,start,commands,closed=False):
        here=start;members=[]
        for i,(kind,end,*a) in enumerate(commands):
            k=f'{n}-{i}';members.append(k)
            if kind=='L':self.add_line(k,here,end)
            elif kind=='A':self.add_arc(k,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C':self.add_bezier(k,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)

    def build(self):
        # Slightly upright round medal, with ribbon contacts owned by explicit nodes.
        self.path('medal',(24,4),[('C',(40,19),(33,4),(40,10)),('C',(36,29),(40,23),(39,26)),('C',(24,34),(33,32),(28,34)),('C',(12,29),(20,34),(15,32)),('C',(8,19),(9,26),(8,23)),('C',(24,4),(8,10),(15,4))],True)
        # Crisp five-point star retains the reference identity; unresolved spacing is reported.
        self.add_polyline('star',(24,12),(27,17),(32,18),(28,22),(29,27),(24,24),(19,27),(20,22),(16,18),(21,17),closed=True)
        self.add_polyline('ribbon',(12,29),(10,44),(24,42),(38,44),(36,29));self.relate('connect','ribbon','medal')

USER_APPROVED_EXCEPTION = {'approved_by': 'user', 'approved_on': '2026-09-25', 'source_request': 'user-account-lock and car look bad, revise please, for cases related with text, use typeface v2 to fix it, we can make its as exception that the text not necesary to be have distance 4 unit, other unresolve could make as eception, global could use v-rect to amke passport bigger', 'reason': 'Crisp star and ribbon retained; user accepts the inset star-to-medal clearance exception.', 'scope': ['star/medal clearance'], 'svg_sha256': '69421dcc6f41cc2a7c25e124f630a15508cf3bfde8df6f0c0a9972f8f1e3a98f', 'recording': 'local SOLO48 approval; automatic QA is retained unchanged'}

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': 'f4833d4ccdf095ed45bec4c0df730c5b89267572a2ff9df67f5c018b6b678d42', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': 'fc535717-5e07-564a-aad9-923ace667ffb'}
