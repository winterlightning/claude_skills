from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='30dfa027-64b7-4bea-957e-c1a147e61020'
SOURCE_PATH='pictographic-primitives/_uncategorized_33/robot wifi 5g_30dfa027-64b7-4bea-957e-c1a147e61020.svg'
AUTHOR='gpt-6'
PLAN='Wireless arcs above a robot arm with two pivots and gripper. Single arm stroke replaces crowded parallel edges.'
CONSTRUCTION_REFERENCE='Lucide bot circular joints; wifi nested radio arcs'
class Drawing(Solo48):
    icon_id='robot-wifi-5g'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('robot', 'wifi', '5g')
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
        self.add_arc('wifi-outer',(6,10),(22,10),radius_x=8,radius_y=4)
        self.add_arc('wifi-inner',(10,19),(18,19),radius_x=4,radius_y=3)
        self.circle('base-joint',14,34,4)
        self.circle('upper-joint',34,19,4)
        self.add_line('arm',(18,34),(34,23))
        self.relate('connect','arm','base-joint');self.relate('connect','arm','upper-joint')
        self.add_line('base-left',(10,34),(12,42))
        self.add_line('base-right',(18,34),(22,42))
        self.relate('connect','base-left','base-joint');self.relate('connect','base-right','base-joint');self.relate('connect','base-right','arm')
        self.add_polyline('gripper',(38,19),(42,25),(42,31))
        self.relate('connect','gripper','upper-joint')
