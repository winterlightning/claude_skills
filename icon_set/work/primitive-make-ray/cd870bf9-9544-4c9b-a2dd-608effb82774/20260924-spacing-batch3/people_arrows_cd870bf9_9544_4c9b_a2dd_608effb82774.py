from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='cd870bf9-9544-4c9b-a2dd-608effb82774'
SOURCE_PATH='pictographic-primitives/_uncategorized_30/people arrows_cd870bf9-9544-4c9b-a2dd-608effb82774.svg'
AUTHOR='gpt-6'
PLAN='Two people with a bidirectional arrow beneath. Head bottoms14 and shoulder crests22 give exact8 centerline /4 ink gap. Matched busts and arrow mirror about x=24.'
CONSTRUCTION_REFERENCE='human_ref/user.svg; Lucide users paired bust construction'
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
            self.circle(n+'-head',x,11,3)
            self.add_arc(n+'-shoulder',(x-8,25),(x+8,25),radius_x=8,radius_y=3)
        self.add_polyline('arrow-left',(15,34),(11,37),(15,40))
        self.add_polyline('arrow-right',(33,34),(37,37),(33,40))
        self.add_line('shaft',(11,37),(37,37))
        self.relate('connect','shaft','arrow-left');self.relate('connect','shaft','arrow-right')

FINAL_OMISSIONS = 'Smaller heads and shallower shoulders provide room for arrow.'
VISUAL_REVIEW = 'Head bottoms14 and shoulder crests22 give exact8 centerline /4 ink gap. Matched busts and arrow mirror about x=24.'
