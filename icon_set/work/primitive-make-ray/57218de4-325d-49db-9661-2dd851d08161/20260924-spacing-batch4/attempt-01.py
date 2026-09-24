from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='57218de4-325d-49db-9661-2dd851d08161'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/share holder notification 2_57218de4-325d-49db-9661-2dd851d08161.svg'
AUTHOR='gpt-6'
PLAN='Bell over three shareholder busts. Omit top loop and clapper, use shared joined shoulders and head radius2. Exact detached4 ink gap.'
CONSTRUCTION_REFERENCE='Lucide bell flared silhouette; human_ref/user.svg circular heads and broad shoulders'
class Drawing(Solo48):
    icon_id='share-holder-notification-2'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('share', 'holder', 'notification', '2')
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
        self.add_line('bell-left',(14,16),(18,12))
        self.add_arc('bell-dome',(18,12),(30,12),radius_x=6)
        self.add_line('bell-right',(30,12),(34,16))
        self.add_line('bell-base',(34,16),(14,16))
        self.add_contour('bell','bell-left','bell-dome','bell-right','bell-base',closed=True)
        # Shared human_ref/user.svg vocabulary; exact head bottom29 / shoulder crest37 gap8.
        for n,x in [('left',12),('center',24),('right',36)]:
            self.circle(n+'-head',x,27,2)
            self.add_arc(n+'-shoulder',(x-6,42),(x+6,42),radius_x=6,radius_y=5)
        self.relate('connect','left-shoulder','center-shoulder');self.relate('connect','center-shoulder','right-shoulder')
