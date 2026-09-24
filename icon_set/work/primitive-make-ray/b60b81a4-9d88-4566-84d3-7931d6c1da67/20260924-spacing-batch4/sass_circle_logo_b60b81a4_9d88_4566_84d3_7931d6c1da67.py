from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b60b81a4-9d88-4566-84d3-7931d6c1da67'
SOURCE_PATH='pictographic-primitives/_uncategorized_33/sass circle logo_b60b81a4-9d88-4566-84d3-7931d6c1da67.svg'
AUTHOR='gpt-6'
PLAN='Circular Sass badge with calligraphic S; raise lower loop and simplify terminal curl while retaining both loops.'
CONSTRUCTION_REFERENCE='No useful Lucide logo match; supplied Sass silhouette owns script'
class Drawing(Solo48):
    icon_id='sass-circle-logo'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('sass', 'circle', 'logo')
    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,l,t,r,b,k=4):
        ps=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
        ns=[]
        for j,a in enumerate(ps):
            z=ps[(j+1)%8]
            if a==z: continue
            m=f'{n}-{j}'; ns.append(m)
            if j%2:self.add_arc(m,a,z,radius_x=k)
            else:self.add_line(m,a,z)
        self.add_contour(n,*ns,closed=True)
    def cross(self,n,x,y,r):
        ns=[]
        for j,p in enumerate([(x-r,y),(x+r,y),(x,y-r),(x,y+r)]):
            m=f'{n}-{j}';ns.append(m);self.add_line(m,(x,y),p)
        self.relate('connect',*ns)
    def build(self):
        self.circle('badge',24,24,20)
        self.add_bezier('script',(23,21),((30,24),(35,17),(29,15)),((25,13),(15,18),(15,22)),((14,26),(27,27),(24,32)),((22,36),(15,34),(18,31)),((22,28),(30,27),(31,31)))
