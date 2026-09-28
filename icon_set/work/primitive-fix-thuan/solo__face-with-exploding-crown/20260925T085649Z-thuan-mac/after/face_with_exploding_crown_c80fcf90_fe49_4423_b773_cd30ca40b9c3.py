'Rounded lower face and enlarged surprised mouth; rebuilt the burst with balanced sharp rays instead of blunt crown lobes.\nSymbol plan: coherent named contours, common repeated dimensions and shared joins.\nConstruction: No useful exact Lucide match; supplied original defines subject.\nKeyshape VRECT_L; integer SOLO48 geometry. Human faces follow circular jaw construction; no detached torso.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='c80fcf90-fe49-4423-b773-cd30ca40b9c3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__face-with-exploding-crown/20260925T085649Z-thuan-mac/reference/face explode_c80fcf90-fe49-4423-b773-cd30ca40b9c3.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='face-with-exploding-crown'
    keyshape=Keyshape.VRECT_L
    exception={'reason': 'Preserve the integrated burst tips and the surprised circular mouth. Local burst notches and exact curved mouth clearance remain legible at native size.', 'approved_by': 'user-delegated visual judgment, gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '0c2466bdb2f735ef56be1493d6928dbf7e55dd511164c65072a16b86ca63b899'}
    semantic_role="MAIN"
    semantic_kind="noun"
    category='primitives-generate'
    aliases=()
    keywords=('face', 'with', 'exploding', 'crown')

    def path(self,n,p,*steps,closed=False):
        ids=[]
        for i,s in enumerate(steps):
            k=f'{n}-{i}'
            if s[0]=='L': q=s[1]; self.add_line(k,p,q)
            elif s[0]=='A': q=s[1]; self.add_arc(k,p,q,radius_x=s[2],radius_y=s[3],sweep=s[4])
            else: q=s[3]; self.add_bezier(k,p,(s[1],s[2],q))
            ids.append(k);p=q
        self.add_contour(n,*ids,closed=closed)
    def oval(self,n,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.path(n,(x,y-ry),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True),('A',(x,y-ry),rx,ry,True),closed=True)
    def box(self,n,l,t,r,b,q=3):
        self.path(n,(l+q,t),('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True),closed=True)

    def build(self):
        self.path('face',(8,28),('A',(40,28),16,16,False),('L',(39,18)),('L',(34,15)),('L',(40,10)),('L',(31,11)),('L',(32,4)),('L',(25,10)),('L',(19,4)),('L',(18,11)),('L',(10,8)),('L',(14,16)),('L',(8,17)),('L',(8,28)),closed=True)
        self.add_dot('eye-left',(17,24));self.add_dot('eye-right',(31,24));self.oval('mouth',24,33,3)
