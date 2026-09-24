from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d8495254-20a2-4d70-a2c6-140b4f7cd24a'
SOURCE_PATH='pictographic-primitives/_uncategorized_30/picture sun_d8495254-20a2-4d70-a2c6-140b4f7cd24a.svg'
AUTHOR='gpt-6'
PLAN='A framed sun above two rounded hills. Paired hills join the frame at explicit endpoints; smooth curves, centered sun and balanced openings.'
CONSTRUCTION_REFERENCE='Lucide image rounded frame, sun and joined landscape'
class Drawing(Solo48):
    icon_id='picture-sun'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('picture', 'sun')
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
        self.add_line('frame-left',(6,34),(6,10))
        self.add_arc('frame-tl',(6,10),(10,6),radius_x=4)
        self.add_line('frame-top',(10,6),(38,6))
        self.add_arc('frame-tr',(38,6),(42,10),radius_x=4)
        self.add_line('frame-right',(42,10),(42,34))
        self.add_contour('frame-upper','frame-left','frame-tl','frame-top','frame-tr','frame-right')
        self.add_polyline('frame-bottom',(42,34),(42,42),(6,42),(6,34))
        self.relate('connect','frame-upper','frame-bottom')
        self.circle('sun',24,18,3)
        self.add_bezier('hills',(6,34),((12,29),(19,29),(24,34)),((29,29),(36,29),(42,34)))
        self.relate('connect','hills','frame-upper');self.relate('connect','hills','frame-bottom')

FINAL_OMISSIONS = 'Drop detached sun rays.'
VISUAL_REVIEW = 'Paired hills join the frame at explicit endpoints; smooth curves, centered sun and balanced openings.'
