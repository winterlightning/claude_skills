from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='5bf1aba4-f7d5-46d8-ad17-5b349ba3bb93'
SOURCE_PATH='pictographic-primitives/_uncategorized_32/rectangle history_5bf1aba4-f7d5-46d8-ad17-5b349ba3bb93.svg'
AUTHOR='gpt-6'
PLAN='A clipped-corner history document with a clock. Large clock provides legal spacing around both hands. Deliberate asymmetric overlap follows Lucide file-clock construction.'
CONSTRUCTION_REFERENCE='Lucide file-clock: clock overlapping an interrupted document'
class Drawing(Solo48):
    icon_id='rectangle-history'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('rectangle', 'history')
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
        self.add_polyline('document',(6,8),(6,6),(34,6),(42,14),(42,42),(40,42))
        self.circle('clock',19,29,13)
        self.add_polyline('hands',(19,25),(19,29),(23,29))

FINAL_OMISSIONS = 'Drop bottom text rule; move clock to lower-left overlap.'
VISUAL_REVIEW = 'Large clock provides legal spacing around both hands. Deliberate asymmetric overlap follows Lucide file-clock construction.'
