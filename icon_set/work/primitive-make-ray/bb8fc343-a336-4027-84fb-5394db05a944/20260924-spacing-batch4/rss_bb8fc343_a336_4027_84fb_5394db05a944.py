from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='bb8fc343-a336-4027-84fb-5394db05a944'
SOURCE_PATH='pictographic-primitives/_uncategorized_33/rss_bb8fc343-a336-4027-84fb-5394db05a944.svg'
AUTHOR='gpt-6'
PLAN='An RSS symbol in a rounded badge. Quarter-circle broadcast geometry follows the source origin; asymmetric lower-left dot preserved.'
CONSTRUCTION_REFERENCE='Lucide rss concentric quarter-circle construction'
class Drawing(Solo48):
    icon_id='rss'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('rss',)
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
        self.add_line('top',(10,6),(14,6))
        self.add_arc('outer-curve',(14,6),(42,34),radius_x=28)
        self.add_line('right',(42,34),(42,38))
        self.add_arc('br',(42,38),(38,42),radius_x=4)
        self.add_line('bottom',(38,42),(10,42))
        self.add_arc('bl',(10,42),(6,38),radius_x=4)
        self.add_line('left',(6,38),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('badge','top','outer-curve','right','br','bottom','bl','left','tl',closed=True)
        self.add_arc('radio',(15,15),(33,33),radius_x=18)
        self.add_dot('dot',(15,33))

FINAL_OMISSIONS = 'Outer badge curve doubles as outer broadcast arc; remove redundant inner arc and reduce source circle to dot.'
VISUAL_REVIEW = 'Quarter-circle broadcast geometry follows the source origin; asymmetric lower-left dot preserved.'
