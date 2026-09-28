'Made equal circular nodes larger and replaced lopsided connector with two matching tangent quarter-circle bends.\nSymbol plan: coherent named contours, common repeated dimensions and shared joins.\nConstruction: Lucide workflow, original and atomic geometry inspected.\nKeyshape SQUARE; integer SOLO48 geometry. Human faces follow circular jaw construction; no detached torso.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='ea1bde8b-e7f7-4fc3-b915-1043468acb6d'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__dynamic/20260925T085649Z-thuan-mac/reference/dynamic_ea1bde8b-e7f7-4fc3-b915-1043468acb6d.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='dynamic'
    keyshape=Keyshape.SQUARE
    exception={'reason': 'Retain tangent rounded connector elbows at the attached circular nodes. Local internal-spacing advisories concern the immediate node/connector bends; the two nodes and connecting line remain unambiguous.', 'approved_by': 'user-delegated visual judgment, gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '20a4717f96f23eb96d7f13c57ca33ceb6d5bb9d34203c31f1d007e0b14621677'}
    semantic_role="MAIN"
    semantic_kind="noun"
    category='diagrams'
    aliases=()
    keywords=('dynamic',)

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
        self.oval('lower-node',12,36,6);self.oval('upper-node',36,12,6)
        self.path('link',(12,30),('L',(12,28)),('A',(16,24),4,4,True),('L',(32,24)),('A',(36,20),4,4,False),('L',(36,18)))
        self.relate('connect','link','lower-node');self.relate('connect','link','upper-node')
