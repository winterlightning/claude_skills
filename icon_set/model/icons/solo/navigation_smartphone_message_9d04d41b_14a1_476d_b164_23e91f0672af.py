from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='9d04d41b-14a1-476d-b164-23e91f0672af'
SOURCE_PATH='pictographic-primitives/_uncategorized_28/navigation smartphone message_9d04d41b-14a1-476d-b164-23e91f0672af.svg'
AUTHOR='gpt-6'
PLAN='A smartphone with a location message bubble. Pin is clear inside bubble; actual shared phone/bubble endpoints. Deliberate offset overlap.'
CONSTRUCTION_REFERENCE='Lucide smartphone coherent enclosure; map-pin dome'
class Drawing(Solo48):
    icon_id='navigation-smartphone-message'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('navigation', 'smartphone', 'message')
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
        self.add_polyline('phone',(16,6),(6,6),(6,42),(16,42))
        self.add_polyline('bubble',(16,6),(42,6),(42,34),(28,34),(16,42),closed=True)
        self.relate('connect','phone','bubble')
        self.add_arc('pin-dome',(25,19),(33,19),radius_x=4)
        self.add_line('pin-tip-1',(33,19),(29,25))
        self.add_line('pin-tip-2',(29,25),(25,19))
        self.add_contour('pin','pin-dome',*['pin-tip-1','pin-tip-2'],closed=True)

FINAL_OMISSIONS = 'Drop home button and divider; enlarge bubble relative to phone.'
VISUAL_REVIEW = 'Pin is clear inside bubble; actual shared phone/bubble endpoints. Deliberate offset overlap.'
