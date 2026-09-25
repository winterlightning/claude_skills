from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='dd1e6365-7d94-41e2-84d6-66c8ad75ede1'
SOURCE_PATH='pictographic-primitives/other/rectangle sub text_dd1e6365-7d94-41e2-84d6-66c8ad75ede1.svg'
AUTHOR='gpt-6'
PLAN='Full uppercase SUB text inside the rounded display. U has wider stems; B uses two evenly spaced bowls.'
CONSTRUCTION_REFERENCES='rectangle-ellipsis: rounded panel; supplied source: full SUB inscription.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='subtitles-display'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('rectangle', 'sub', 'text')

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
        self.box('panel',4,8,44,40,4)
        self.path('s',(18,17),[('C',(10,20),(13,13),(9,16)),('C',(18,28),(10,25),(18,23)),('C',(10,31),(18,33),(13,35))])
        self.path('u',(23,16),[('L',(23,28)),('A',(31,28),4,4,False),('L',(31,16))])
        self.add_polyline('b-stem',(38,32),(38,24),(38,16))
        self.path('b-bow',(38,16),[('A',(38,24),4,4,True),('A',(38,32),4,4,True)])
        self.relate('connect','b-stem','b-bow')
