from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='91199cb3-6e0d-41e0-9c27-12e09942eed6'
SOURCE_PATH='pictographic-primitives/other/tv circle check_91199cb3-6e0d-41e0-9c27-12e09942eed6.svg'
AUTHOR='gpt-6'
PLAN='Circled-check monitor retained; user accepts its nested ring/screen and ring/check spacing as an exception.'
CONSTRUCTION_REFERENCES='Lucide monitor original and atomic-debug: rounded screen corners and central stand.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='tv-circle-check'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('tv', 'circle', 'check')

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
        self.path('screen',(10,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,30)),('A',(38,34),4,4,True),('L',(24,34)),('L',(10,34)),('A',(6,30),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
        self.add_line('stand',(24,34),(24,42));self.add_polyline('foot',(16,42),(24,42),(32,42))
        self.relate('connect','stand','screen');self.relate('connect','stand','foot')
        self.circle('status-ring',24,20,9)
        self.add_polyline('check',(21,20),(23,22),(27,18))

USER_APPROVED_EXCEPTION = {'approved_by': 'user', 'approved_on': '2026-09-25', 'source_request': 'user-account-lock and car look bad, revise please, for cases related with text, use typeface v2 to fix it, we can make its as exception that the text not necesary to be have distance 4 unit, other unresolve could make as eception, global could use v-rect to amke passport bigger', 'reason': 'Circled-check monitor retained; user accepts its nested ring/screen and ring/check spacing as an exception.', 'scope': ['screen/status-ring clearance', 'status-ring/check clearance'], 'svg_sha256': '803e1b1f29506cbb9edc1204d62bedee7ed3c5005b440fb354cab5d3aac1324d', 'recording': 'local SOLO48 approval; automatic QA is retained unchanged'}

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': '50c7143e5a47e611c95df24a760338865a21475b5c4aab43ad58a798dfe63459', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': '91199cb3-6e0d-41e0-9c27-12e09942eed6'}
