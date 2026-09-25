'Replaced angular drop with a taller curved teardrop and softened puddle lobes.\nSymbol plan: coherent named contours, common repeated dimensions and shared joins.\nConstruction: Lucide droplet, original and atomic geometry inspected.\nKeyshape SQUARE; integer SOLO48 geometry. Human faces follow circular jaw construction; no detached torso.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='55d73bcc-348c-5d24-89f9-39afd521e3bc'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__drop-falling-into-puddle/20260925T085649Z-thuan-mac/reference/blood stain_55d73bcc-348c-5d24-89f9-39afd521e3bc.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='drop-falling-into-puddle'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category='nature'
    aliases=()
    keywords=('drop', 'falling', 'into', 'puddle')

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
        self.path('drop',(32,6),('C',(30,10),(26,13),(26,16)),('A',(38,16),6,6,False),('C',(38,13),(34,10),(32,6)),closed=True)
        self.path('puddle',(6,35),('C',(6,32),(13,33),(12,30)),('C',(11,26),(25,27),(26,31)),('C',(29,34),(42,30),(42,36)),('C',(42,40),(31,39),(28,41)),('C',(27,42),(25,42),(23,42)),('C',(15,42),(6,41),(6,35)),closed=True)
