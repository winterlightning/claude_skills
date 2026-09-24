from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4bd2f046-d00e-4c3d-99dd-153eae347474'
SOURCE_PATH='pictographic-primitives/_uncategorized_33/seo search eye_4bd2f046-d00e-4c3d-99dd-153eae347474.svg'
AUTHOR='gpt-6'
PLAN='Eye-shaped magnifying lens with iris and attached handle; merge redundant circular lens and eye boundary.'
CONSTRUCTION_REFERENCE='Lucide eye paired curves and iris; search attached handle'
class Drawing(Solo48):
    icon_id='seo-search-eye'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('seo', 'search', 'eye')
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
        # Eye boundary itself forms the magnifier lens; omit redundant enclosing circle.
        self.add_bezier('eye-upper',(6,24),((14,6),(34,6),(42,24)))
        self.add_bezier('eye-lower',(42,24),((34,42),(14,42),(6,24)))
        self.add_contour('lens','eye-upper','eye-lower',closed=True)
        self.circle('iris',24,24,3)
        self.add_line('handle',(42,24),(42,42));self.relate('connect','handle','lens')
