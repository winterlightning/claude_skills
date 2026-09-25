'Restored curved outward arms and three outlined round lamps; balanced dome and hanging stem.\nSymbol plan: coherent named contours, common repeated dimensions and shared joins.\nConstruction: Lucide lamp-ceiling, original and atomic geometry inspected.\nKeyshape SQUARE; integer SOLO48 geometry. Human faces follow circular jaw construction; no detached torso.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='199cd4a2-400c-4d47-8fa9-5daa34d913e4'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__domed-three-light-chandelier/20260925T085649Z-thuan-mac/reference/ceiling lamp chandelier_199cd4a2-400c-4d47-8fa9-5daa34d913e4.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='domed-three-light-chandelier'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category='primitives-generate'
    aliases=()
    keywords=('domed', 'three', 'light', 'chandelier')

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
        self.path('shade',(8,26),('A',(24,10),16,16,True),('A',(40,26),16,16,True),('L',(8,26)),closed=True)
        self.add_line('stem',(24,6),(24,10));self.relate('connect','stem','shade')
        for i,x in enumerate((9,24,39)):
            self.oval(f'bulb-{i}',x,39,3)
            if i==1:self.add_line(f'cord-{i}',(24,26),(24,36))
            else:
                a=16 if i==0 else 32
                self.path(f'cord-{i}',(a,26),('C',(a,32),(x,32),(x,36)))
            self.relate('connect',f'cord-{i}','shade');self.relate('connect',f'cord-{i}',f'bulb-{i}')
