from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='796e3289-99b8-4ef8-bce0-4e8fa2bfefc8'
SOURCE_PATH='pictographic-primitives/transportation/car_796e3289-99b8-4ef8-bce0-4e8fa2bfefc8.svg'
AUTHOR='gpt-6'
PLAN='Lowered the cabin, smoothed hood and trunk into a continuous body, and reattached body and sill to wheel sides. Natural car ink bounds(2,10)-(46,38) deliberately relax the standard HRECT_M height by2 at each edge.'
CONSTRUCTION_REFERENCES='Lucide car original and atomic-debug: coherent cabin, body ends and circular wheels.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='side-profile-sedan'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('car',)

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
        # Natural low sedan proportions: same48 canvas, relaxed keyshape-height fit.
        self.path('body',(8,31),[('L',(7,31)),('C',(4,28),(5,31),(4,30)),('L',(4,24)),('C',(9,20),(4,21),(6,20)),('L',(11,20)),('L',(16,14)),('C',(20,12),(17,12),(18,12)),('L',(28,12)),('C',(33,15),(30,12),(31,13)),('L',(37,20)),('L',(40,21)),('C',(44,25),(43,22),(44,23)),('L',(44,28)),('C',(41,31),(44,30),(43,31)),('L',(40,31))])
        for x in (13,35):self.circle(f'wheel-{x}',x,31,5)
        self.add_line('sill',(18,31),(30,31))
        for wheel in ['wheel-13','wheel-35']:
            self.relate('connect','body',wheel);self.relate('connect','sill',wheel)

USER_APPROVED_EXCEPTION = {'approved_by': 'user', 'approved_on': '2026-09-25', 'source_request': 'user-account-lock and car look bad, revise please, for cases related with text, use typeface v2 to fix it, we can make its as exception that the text not necesary to be have distance 4 unit, other unresolve could make as eception, global could use v-rect to amke passport bigger', 'reason': 'Lowered the cabin, smoothed hood and trunk into a continuous body, and reattached body and sill to wheel sides. Natural car ink bounds(2,10)-(46,38) deliberately relax the standard HRECT_M height by2 at each edge.', 'scope': ['keyshape vertical fit', 'body/wheel internal spacing'], 'svg_sha256': 'bc2ea24d9e80a34810c1632cd5f5c086a83f6225165f0980d31ea88f9e596dc2', 'recording': 'local SOLO48 approval; automatic QA is retained unchanged'}
