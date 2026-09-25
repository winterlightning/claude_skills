from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='91199cb3-6e0d-41e0-9c27-12e09942eed6'
SOURCE_PATH='pictographic-primitives/other/tv circle check_91199cb3-6e0d-41e0-9c27-12e09942eed6.svg'
AUTHOR='gpt-6'
PLAN='Rounded monitor with a larger centered ring and hand-built check. Central stand shares the bottom-wall node.'
CONSTRUCTION_REFERENCES='monitor: rounded enclosure and shared central stand; circle: cardinal arc construction.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='monitor-with-check'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('tv', 'circle', 'check')

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
        self.path('screen',(10,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,32)),('A',(38,36),4,4,True),('L',(24,36)),('L',(10,36)),('A',(6,32),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
        self.add_line('stand',(24,36),(24,42));self.add_polyline('foot',(16,42),(24,42),(32,42))
        self.relate('connect','stand','screen');self.relate('connect','stand','foot')
        self.circle('status-ring',24,21,10)
        self.add_polyline('check',(21,21),(23,23),(27,19))
