from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='cd870bf9-9544-4c9b-a2dd-608effb82774'
SOURCE_PATH='pictographic-primitives/_uncategorized_30/people arrows_cd870bf9-9544-4c9b-a2dd-608effb82774.svg'
AUTHOR='gpt-6'
PLAN='Two mirrored busts, exact8 head/shoulder gap, arrow beneath. Shared head radius5 and shoulder width8.'
CONSTRUCTION_REFERENCE='human_ref/user.svg'
class Drawing(Solo48):
    icon_id='people-arrows'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('people', 'arrows')
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
        for n,x in [('left',12),('right',36)]:
            self.circle(n+'-head',x,13,5)
            self.add_arc(n+'-shoulder',(x-8,30),(x+8,30),radius_x=8,radius_y=4)
        self.add_polyline('arrow-left',(17,34),(11,40),(17,40))
        self.add_polyline('arrow-right',(31,34),(37,40),(31,40))
        self.add_line('shaft',(17,40),(31,40))
        self.relate('connect','shaft','arrow-left');self.relate('connect','shaft','arrow-right')
