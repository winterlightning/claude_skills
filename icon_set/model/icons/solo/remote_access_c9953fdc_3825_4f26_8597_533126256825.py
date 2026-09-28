from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='c9953fdc-3825-4f26-8597-533126256825'
SOURCE_PATH='pictographic-primitives/_uncategorized_32/remote access_c9953fdc-3825-4f26-8597-533126256825.svg'
AUTHOR='gpt-6'
PLAN='Nested hexagons around a central remote-access dot. Both hexagons share axes and paired dimensions. Even bands and centered point remain clear at48px.'
CONSTRUCTION_REFERENCE='No useful exact Lucide match; regular paired polygon construction from source'
class Drawing(Solo48):
    icon_id='remote-access'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('remote', 'access')
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
        for n,w,t,h in [('outer',20,10,16),('inner',10,5,8)]:
            self.add_polyline(n,(24-w,24),(24-t,24-h),(24+t,24-h),(24+w,24),(24+t,24+h),(24-t,24+h),closed=True)
        self.add_dot('center',(24,24))

FINAL_OMISSIONS = 'Reduce center circle to a dot.'
VISUAL_REVIEW = 'Both hexagons share axes and paired dimensions. Even bands and centered point remain clear at48px.'
