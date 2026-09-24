from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID='66464e9f-35f0-4894-b4e2-7c801bd38b27'
SOURCE_PATH='pictographic-primitives/_uncategorized_39/vr video 1_66464e9f-35f0-4894-b4e2-7c801bd38b27.svg'
AUTHOR="gpt-6"
PLAN='Pen reduced to diagonal stroke; cube right edge, headset rim and lenses omitted; cube and nose-notch goggle outline retained.'
class Drawing(Solo48):
    icon_id='vr-video-1'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,p,ops,closed=False):
        members=[]
        for i,op in enumerate(ops):
            eid=f'{n}-{i}';end=op[1]
            if op[0]=='L': self.add_line(eid,p,end)
            elif op[0]=='A': self.add_arc(eid,p,end,radius_x=op[2],radius_y=op[3],sweep=op[4])
            else: self.add_bezier(eid,p,(op[2],op[3],end))
            p=end;members.append(eid)
        self.add_contour(n,*members,closed=closed)
    def rect(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)

    def build(self):
        self.add_polyline('stylus',(6,6),(12,8))
        self.add_polyline('cube-top',(6,24),(14,18),(22,24),(14,30),(6,24))
        self.add_polyline('cube-left',(6,24),(6,34),(14,40),(14,30))
        self.relate('connect','cube-top','cube-left')
        self.path('headset',(30,32),[('L',(38,32)),('A',(42,36),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(34,38)),('L',(30,42)),('A',(26,38),4,4,True),('L',(26,36)),('A',(30,32),4,4,True)],True)
