from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='39d51711-cb0a-4cf4-bdca-37c1fe832458'
SOURCE_PATH='pictographic-primitives/other/bubble message pm text_39d51711-cb0a-4cf4-bdca-37c1fe832458.svg'
AUTHOR='gpt-6'
PLAN='Rounded speech bubble containing full PM lettering, with a lower-left tail. Wider M stems and a round P bowl preserve both letters.'
CONSTRUCTION_REFERENCES='message-square: rounded bubble and integral tail; supplied source owns PM letterforms.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='private-message-bubble'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('bubble', 'message', 'pm', 'text')

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
        self.path('bubble',(8,8),[('L',(40,8)),('A',(44,12),4,4,True),('L',(44,32)),('A',(40,36),4,4,True),('L',(16,36)),('L',(4,40)),('L',(4,12)),('A',(8,8),4,4,True)],True)
        self.add_polyline('p-stem',(12,30),(12,24),(12,16))
        self.path('p-bow',(12,16),[('L',(16,16)),('A',(16,24),4,4,True),('L',(12,24))]);self.relate('connect','p-stem','p-bow')
        self.add_polyline('m',(28,30),(28,16),(32,24),(36,16),(36,30))
