from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='796e3289-99b8-4ef8-bce0-4e8fa2bfefc8'
SOURCE_PATH='pictographic-primitives/transportation/car_796e3289-99b8-4ef8-bce0-4e8fa2bfefc8.svg'
AUTHOR='gpt-6'
PLAN='Side-view sedan with a broad cabin, matching hood and trunk shoulders, equal wheels and connected sill.'
CONSTRUCTION_REFERENCES='Lucide car original and atomic-debug: coherent cabin, body ends and circular wheels.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='side-profile-sedan'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('car',)

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
        self.path('body',(12,28),[('L',(8,28)),('A',(4,24),4,4,True),('L',(4,22)),('A',(8,18),4,4,True),('L',(10,18)),('L',(17,12)),('C',(21,10),(18,10),(19,10)),('L',(27,10)),('C',(31,12),(29,10),(30,10)),('L',(36,18)),('L',(40,18)),('A',(44,22),4,4,True),('L',(44,24)),('A',(40,28),4,4,True),('L',(36,28))])
        for x in (12,36):self.circle(f'wheel-{x}',x,33,5)
        self.add_line('sill',(17,33),(31,33))
        for wheel in ['wheel-12','wheel-36']:
            self.relate('connect','body',wheel);self.relate('connect','sill',wheel)
