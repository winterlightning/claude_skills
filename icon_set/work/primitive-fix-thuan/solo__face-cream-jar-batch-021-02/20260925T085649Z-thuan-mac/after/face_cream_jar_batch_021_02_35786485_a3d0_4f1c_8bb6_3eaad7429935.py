'Broadened the jar neck, rounded base corners and softened the asymmetric cream curl.\nSymbol plan: coherent named contours, common repeated dimensions and shared joins.\nConstruction: No useful exact Lucide match; supplied original defines subject.\nKeyshape SQUARE; integer SOLO48 geometry. Human faces follow circular jaw construction; no detached torso.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='35786485-a3d0-4f1c-8bb6-3eaad7429935'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__face-cream-jar-batch-021-02/20260925T085649Z-thuan-mac/reference/face cream_35786485-a3d0-4f1c-8bb6-3eaad7429935.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='face-cream-jar-batch-021-02'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category='other'
    aliases=()
    keywords=('face', 'cream', 'jar', 'batch', '021', '02')

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
        self.box('jar',6,27,42,42,3)
        self.path('rim',(10,27),('L',(10,19)),('L',(38,19)),('L',(38,27)));self.relate('connect','jar','rim')
        self.path('cream',(14,19),('C',(15,13),(24,13),(23,6)),('C',(28,9),(34,13),(34,19)));self.relate('connect','cream','rim')
