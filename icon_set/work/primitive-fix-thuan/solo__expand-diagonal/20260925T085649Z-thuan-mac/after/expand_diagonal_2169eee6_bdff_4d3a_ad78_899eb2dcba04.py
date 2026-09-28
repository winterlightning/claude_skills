'Made diagonal arrows equal under half-turn rotation; unified round frame corners and removed fragmented tiny arrow segments.\nSymbol plan: coherent named contours, common repeated dimensions and shared joins.\nConstruction: Lucide expand, original and atomic geometry inspected.\nKeyshape SQUARE; integer SOLO48 geometry. Human faces follow circular jaw construction; no detached torso.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='2169eee6-bdff-4d3a-ad78-899eb2dcba04'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__expand-diagonal/20260925T085649Z-thuan-mac/reference/expand diagonal_2169eee6-bdff-4d3a-ad78-899eb2dcba04.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='expand-diagonal'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category='design'
    aliases=()
    keywords=('expand', 'diagonal')

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
        self.path('upper-frame',(6,24),('L',(6,10)),('A',(10,6),4,4,True),('L',(24,6)))
        self.path('lower-frame',(42,24),('L',(42,38)),('A',(38,42),4,4,True),('L',(24,42)))
        for i,flip in enumerate((False,True)):
         p=lambda x,y:(48-x,48-y) if flip else (x,y)
         self.add_polyline(f'arrow-{i}',p(32,6),p(42,6),p(42,16))
         self.add_line(f'shaft-{i}',p(42,6),p(28,20));self.relate('connect',f'arrow-{i}',f'shaft-{i}')
