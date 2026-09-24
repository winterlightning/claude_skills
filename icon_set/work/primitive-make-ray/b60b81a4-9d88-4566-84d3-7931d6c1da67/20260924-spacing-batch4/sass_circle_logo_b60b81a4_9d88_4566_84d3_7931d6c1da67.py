from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b60b81a4-9d88-4566-84d3-7931d6c1da67'
SOURCE_PATH='pictographic-primitives/_uncategorized_33/sass circle logo_b60b81a4-9d88-4566-84d3-7931d6c1da67.svg'
AUTHOR='gpt-6'
PLAN='A circular Sass script logo. Expanded upper script loop and circular lower loop preserve the calligraphic S. Actual shared endpoint24,31; source-directed asymmetry retained.'
CONSTRUCTION_REFERENCE='No useful Lucide logo match; supplied Sass script'
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
        self.add_bezier('script',(24,22),((32,24),(33,13),(28,13)),((23,13),(15,18),(15,22)),((15,25),(24,26),(24,31)))
        self.circle('lower-loop',21,31,3)
        self.relate('connect','script','lower-loop')

FINAL_OMISSIONS = 'Regularize lower loop as a circle and omit terminal curl.'
VISUAL_REVIEW = 'Expanded upper script loop and circular lower loop preserve the calligraphic S. Actual shared endpoint24,31; source-directed asymmetry retained.'
