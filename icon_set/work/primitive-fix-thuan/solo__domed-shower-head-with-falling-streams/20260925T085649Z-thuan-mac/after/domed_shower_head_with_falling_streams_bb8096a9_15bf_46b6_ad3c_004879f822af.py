'Broadened dome and aligned all water columns beneath it; made water marks clear vertical dashes.\nSymbol plan: coherent named contours, common repeated dimensions and shared joins.\nConstruction: Lucide shower-head, original and atomic geometry inspected.\nKeyshape VRECT_L; integer SOLO48 geometry. Human faces follow circular jaw construction; no detached torso.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='bb8096a9-15bf-46b6-ad3c-004879f822af'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__domed-shower-head-with-falling-streams/20260925T085649Z-thuan-mac/reference/shower_bb8096a9-15bf-46b6-ad3c-004879f822af.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='domed-shower-head-with-falling-streams'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category='primitives-generate'
    aliases=()
    keywords=('domed', 'shower', 'head', 'with', 'falling', 'streams')

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
        self.path('head',(8,24),('A',(20,12),12,12,True),('A',(32,24),12,12,True),('L',(8,24)),closed=True)
        self.path('pipe',(20,12),('A',(28,4),8,8,True),('L',(40,4)))
        self.relate('connect','pipe','head')
        for i,x in enumerate((10,20,30)):
            for j,y in enumerate((33,43)): self.add_line(f'water-{i}-{j}',(x,y),(x,y+1))
