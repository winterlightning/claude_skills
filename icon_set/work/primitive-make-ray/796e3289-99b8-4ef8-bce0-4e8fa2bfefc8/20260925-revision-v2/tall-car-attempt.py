from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
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
        # Low continuous body meets wheel sides; roof/hood/trunk flow as one contour.
        self.path('body',(8,33),[('L',(7,33)),('C',(4,30),(5,33),(4,32)),('L',(4,25)),('C',(9,21),(4,22),(6,21)),('L',(11,21)),('L',(16,13)),('C',(20,10),(17,11),(18,10)),('L',(28,10)),('C',(33,14),(30,10),(31,11)),('L',(37,20)),('L',(40,21)),('C',(44,26),(43,22),(44,23)),('L',(44,30)),('C',(41,33),(44,32),(43,33)),('L',(40,33))])
        for x in (13,35):self.circle(f'wheel-{x}',x,33,5)
        self.add_line('sill',(18,33),(30,33))
        for wheel in ['wheel-13','wheel-35']:
            self.relate('connect','body',wheel);self.relate('connect','sill',wheel)
