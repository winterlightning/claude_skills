'Rebuilt both signal arches as smooth symmetric elliptical arcs with equal clear spacing and a centered terminal dot.\nSymbol plan: coherent named contours, common repeated dimensions and shared joins.\nConstruction: Lucide wifi, original and atomic geometry inspected.\nKeyshape HRECT_M; integer SOLO48 geometry. Human faces follow circular jaw construction; no detached torso.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e6789468-9cc2-4444-a388-10e9ec1fdcb5'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__electric-waves-1/20260925T085649Z-thuan-mac/reference/electric waves 1_e6789468-9cc2-4444-a388-10e9ec1fdcb5.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='electric-waves-1'
    keyshape=Keyshape.HRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category='state'
    aliases=()
    keywords=('electric', 'waves', '1')

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
        self.path('outer',(4,18),('A',(24,10),28,20,True),('A',(44,18),28,20,True))
        self.path('inner',(12,28),('A',(24,23),18,15,True),('A',(36,28),18,15,True))
        self.add_dot('terminal',(24,38))
