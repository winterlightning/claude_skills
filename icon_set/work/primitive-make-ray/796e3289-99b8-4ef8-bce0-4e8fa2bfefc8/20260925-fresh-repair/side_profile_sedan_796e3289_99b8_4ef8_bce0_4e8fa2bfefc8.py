from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='796e3289-99b8-4ef8-bce0-4e8fa2bfefc8'
SOURCE_PATH='pictographic-primitives/transportation/car_796e3289-99b8-4ef8-bce0-4e8fa2bfefc8.svg'
AUTHOR='gpt-6'
PLAN='Broad low sedan cabin above smooth hood and trunk; equal circular wheels join the body at explicit side nodes.'
CONSTRUCTION_REFERENCES='car: coherent cabin outline, short body ends and full round wheels.'
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
        self.path('body',(7,33),[('L',(4,33)),('L',(4,24)),('A',(8,20),4,4,True),('L',(10,20)),('L',(17,12)),('C',(21,10),(18,10),(19,10)),('L',(27,10)),('C',(31,12),(29,10),(30,10)),('L',(36,20)),('L',(40,20)),('A',(44,24),4,4,True),('L',(44,33)),('L',(41,33))])
        for x in (12,36):self.circle(f'wheel-{x}',x,33,5)
        self.add_line('sill',(17,33),(31,33))
        for wheel in ['wheel-12','wheel-36']:
            self.relate('connect','body',wheel);self.relate('connect','sill',wheel)
