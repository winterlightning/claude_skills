from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='ca0b86cd-f823-4251-8d27-7775eddb1f7a'
SOURCE_PATH='pictographic-primitives/other/lock person_ca0b86cd-f823-4251-8d27-7775eddb1f7a.svg'
AUTHOR='gpt-6'
PLAN='Padlock with rounded shackle, outlined circular head, and broad shoulders forming the inset lower silhouette.'
CONSTRUCTION_REFERENCES='Lucide lock original and atomic-debug: rounded shackle. icon_set/references/human_ref/user.svg: circular head and broad symmetric shoulders.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='lock-person'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('lock', 'person')

    def path(self,n,start,commands,closed=False):
        here=start;members=[]
        for i,(kind,end,*a) in enumerate(commands):
            k=f'{n}-{i}';members.append(k)
            if kind=='L':self.add_line(k,here,end)
            elif kind=='A':self.add_arc(k,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C':self.add_bezier(k,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)

    def build(self):
        # Split at real corner/shoulder nodes so exact axis clearance is certifiable.
        self.add_polyline('top',(12,16),(16,16),(32,16),(36,16))
        self.path('left',(8,44),[('L',(8,20)),('A',(12,16),4,4,True)])
        self.path('right',(36,16),[('A',(40,20),4,4,True),('L',(40,44))])
        self.path('shoulders',(40,44),[('A',(24,40),16,4,False),('A',(8,44),16,4,False)])
        for a,b in [('left','top'),('top','right'),('right','shoulders'),('shoulders','left')]:self.relate('connect',a,b)
        self.path('shackle',(16,16),[('L',(16,12)),('A',(32,12),8,8,True),('L',(32,16))]);self.relate('connect','shackle','top')
        self.circle('head',24,28,4)
        # human_ref/user.svg: head lower extremum32, shoulder upper extremum40.
        # Exact detached ink clearance: 40-32-4=4. No waiver or false contact.
