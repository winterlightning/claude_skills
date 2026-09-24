from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='edc387fb-8345-489a-a276-38ea07c6e827'
SOURCE_PATH='pictographic-primitives/_uncategorized_30/pin add_edc387fb-8345-489a-a276-38ea07c6e827.svg'
AUTHOR='gpt-6'
PLAN='A location pin with a lower-right plus. Pin retains smooth dome and coherent taper; separate plus has four truly joined arms. Deliberate offset composition.'
CONSTRUCTION_REFERENCE='Lucide map-pin domed pin and taper'
class Drawing(Solo48):
    icon_id='pin-add'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('pin', 'add')
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
        self.add_arc('pin-dome',(6,16),(26,16),radius_x=10)
        self.add_bezier('pin-right',(26,16),((26,23),(21,31),(16,38)))
        self.add_bezier('pin-left',(16,38),((11,31),(6,23),(6,16)))
        self.add_contour('pin','pin-dome','pin-right','pin-left',closed=True)
        self.cross('plus',36,36,6)

FINAL_OMISSIONS = 'Drop circular add-badge boundary.'
VISUAL_REVIEW = 'Pin retains smooth dome and coherent taper; separate plus has four truly joined arms. Deliberate offset composition.'
