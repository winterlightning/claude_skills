from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='8eb34e8a-c1a0-4770-a3b1-2f00e05fdaef'
SOURCE_PATH='pictographic-primitives/_uncategorized_30/pesach passover 2_8eb34e8a-c1a0-4770-a3b1-2f00e05fdaef.svg'
AUTHOR='gpt-6'
PLAN='Repair6: further reduce left star reach and rebalance to center20. Star internal spacing remains blocker if further reduction destroys identity.'
CONSTRUCTION_REFERENCE='Source star plate and matzo'
class Drawing(Solo48):
    icon_id='pesach-passover-2'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('pesach', 'passover', '2')
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
        self.add_arc('plate',(20,40),(20,8),radius_x=16)
        self.add_polyline('star',(20,17),(23,20),(27,22),(25,25),(25,30),(20,28),(15,30),(15,25),(13,22),(17,20),closed=True)
        self.add_polyline('matzo',(35,24),(44,24),(44,32),(44,40),(35,40),(35,32),closed=True)
        self.add_line('row',(35,32),(44,32))
        self.relate('connect','row','matzo')
