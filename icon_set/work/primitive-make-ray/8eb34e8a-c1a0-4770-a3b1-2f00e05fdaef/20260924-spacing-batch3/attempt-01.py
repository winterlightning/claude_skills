from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='8eb34e8a-c1a0-4770-a3b1-2f00e05fdaef'
SOURCE_PATH='pictographic-primitives/_uncategorized_30/pesach passover 2_8eb34e8a-c1a0-4770-a3b1-2f00e05fdaef.svg'
AUTHOR='gpt-6'
PLAN='Passover plate with five-point star and lower-right matzo; preserve all three symbols.'
CONSTRUCTION_REFERENCE='No useful exact Lucide match; source star and tile arrangement'
class Drawing(Solo48):
    icon_id='pesach-passover-2'
    keyshape=Keyshape.SQUARE
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
        self.add_arc('plate',(20,42),(42,20),radius_x=18,large_arc=True)
        self.add_polyline('star',(21,12),(24,19),(31,20),(26,25),(27,32),(21,28),(15,32),(16,25),(11,20),(18,19),closed=True)
        self.box('matzo',28,28,42,42,2)
        self.add_line('row',(28,35),(42,35));self.relate('connect','row','matzo')
