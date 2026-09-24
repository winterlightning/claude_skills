from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4bd2f046-d00e-4c3d-99dd-153eae347474'
SOURCE_PATH='pictographic-primitives/_uncategorized_33/seo search eye_4bd2f046-d00e-4c3d-99dd-153eae347474.svg'
AUTHOR='gpt-6'
PLAN='An eye-shaped search magnifier. Ellipse and pupil form a simplified eye. Handle uses exact3-4-5 ellipse node30,24; deliberate lower-right handle.'
CONSTRUCTION_REFERENCE='Lucide eye symmetric eye/pupil; search attached handle'
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
        pts=[(6,16),(21,6),(36,16),(30,24),(6,16)]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):self.add_arc(f'lens-{i}',a,b,radius_x=15,radius_y=10)
        self.add_contour('eye-lens',*[f'lens-{i}' for i in range(4)],closed=True)
        self.add_dot('pupil',(21,16))
        self.add_line('handle',(30,24),(42,42));self.relate('connect','handle','eye-lens')

FINAL_OMISSIONS = 'Merge eye boundary with magnifier lens; reduce iris to pupil dot.'
VISUAL_REVIEW = 'Ellipse and pupil form a simplified eye. Handle uses exact3-4-5 ellipse node30,24; deliberate lower-right handle.'
