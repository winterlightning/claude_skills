'Smoothed raised wing, head-to-neck transition and fan tail, retaining the right-facing flight silhouette.\nSymbol plan: coherent named contours, common repeated dimensions and shared joins.\nConstruction: Lucide bird, original and atomic geometry inspected.\nKeyshape SQUARE; integer SOLO48 geometry. Human faces follow circular jaw construction; no detached torso.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f512d6dd-1499-4436-b24c-e444dbfb80de'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__dove-flying-right-with-raised-wing/20260925T085649Z-thuan-mac/reference/dove_f512d6dd-1499-4436-b24c-e444dbfb80de.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='dove-flying-right-with-raised-wing'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category='primitives-generate'
    aliases=()
    keywords=('dove', 'flying', 'right', 'with', 'raised', 'wing')

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
        self.path('dove',(6,6),('C',(13,12),(22,13),(26,20)),('C',(29,17),(28,12),(34,12)),('C',(38,12),(38,17),(42,18)),('L',(37,21)),('C',(35,24),(38,32),(26,34)),('C',(23,35),(23,39),(20,42)),('C',(14,42),(9,39),(6,36)),('L',(20,27)),('C',(9,27),(6,19),(6,6)),closed=True)
