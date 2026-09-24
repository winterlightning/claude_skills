from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7d27b436-d05f-41d3-b72f-2e31759f48e2'
SOURCE_PATH='pictographic-primitives/_uncategorized_29/onam 1_7d27b436-d05f-41d3-b72f-2e31759f48e2.svg'
AUTHOR='gpt-6'
PLAN='A six-lobed Onam flower inside a circular rim. Six smooth lobes mirror about both axes; rim and flower remain separated.'
CONSTRUCTION_REFERENCE='Lucide flower coherent petal boundary'
class Drawing(Solo48):
    icon_id='onam-1'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('onam', '1')
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
        self.circle('rim',24,24,20)
        # One six-lobed outline, mirrored about x=24 and y=24.
        self.add_bezier('petals',(24,13),((28,13),(28,17),(28,18)),((32,16),(34,17),(34,20)),((34,22),(32,23),(31,24)),((32,25),(34,26),(34,28)),((34,31),(32,32),(28,30)),((28,31),(28,35),(24,35)),((20,35),(20,31),(20,30)),((16,32),(14,31),(14,28)),((14,26),(16,25),(17,24)),((16,23),(14,22),(14,20)),((14,17),(16,16),(20,18)),((20,17),(20,13),(24,13)))
        self.add_contour('flower','petals',closed=True)

FINAL_OMISSIONS = 'Drop center hexagon and internal petal seams.'
VISUAL_REVIEW = 'Six smooth lobes mirror about both axes; rim and flower remain separated.'
