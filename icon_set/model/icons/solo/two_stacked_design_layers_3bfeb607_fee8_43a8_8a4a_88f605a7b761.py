from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
from ...keyshapes import Keyshape
SOURCE_ICON_ID='3bfeb607-fee8-43a8-8a4a-88f605a7b761'
SOURCE_PATH='pictographic-primitives/design/fill adjustment layer_3bfeb607-fee8-43a8-8a4a-88f605a7b761.svg'
AUTHOR='gpt-6'
PLAN = 'Two straight-sided diamond layers with tangent rounded corners and no tiny corner fragments.'
CONSTRUCTION_REFERENCES='Lucide layers: repeated rhombus proportions and open lower layer.'
OMISSIONS = []
class Drawing(Solo48):
    icon_id='two-stacked-design-layers'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('fill', 'adjustment', 'layer')
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
    def ellipse(self,n,x,y,rx,ry):
        self.path(n,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
    def box(self,n,l,t,r,b,k=4,split=False):
        pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
        ids=[]
        for i,a in enumerate(pts):
            ident=f'{n}-{i}';ids.append(ident);z=pts[(i+1)%8]
            if i%2:self.add_arc(ident,a,z,radius_x=k)
            else:self.add_line(ident,a,z)
        if split:
            for i in range(8):self.relate('connect',ids[i],ids[(i+1)%8])
        else:self.add_contour(n,*ids,closed=True)

    def avatar_body(self,top=32):
        self.add_line('body-left-side',(8,44),(8,top+8))
        self.add_arc('body-left-shoulder',(8,top+8),(16,top),radius_x=8)
        self.add_line('body-top',(16,top),(24,top))
        self.add_line('body-top-right',(24,top),(32,top))
        self.add_arc('body-right-shoulder',(32,top),(40,top+8),radius_x=8)
        self.add_line('body-right-side',(40,top+8),(40,44))
        self.add_contour('body','body-left-side','body-left-shoulder','body-top','body-top-right','body-right-shoulder','body-right-side')
    def portrait_head(self):
        self.add_line('root-left',(14,18),(14,14))
        self.add_arc('crown',(14,14),(34,14),radius_x=10)
        self.add_line('root-right',(34,14),(34,18))
        self.add_arc('jaw',(34,18),(14,18),radius_x=10)
        self.add_contour('head','root-left','crown','root-right','jaw',closed=True)
        self.add_bezier('fringe',(14,18),((20,18),(22,13),(24,13)),((26,13),(28,18),(34,18)))
        self.relate('connect','head','fringe')
    def build(self):
        self.path('top-layer',(24,6),[('C',(27,8),(25,6),(24,6)),('L',(39,16)),('C',(42,18),(42,18),(42,17)),('C',(39,20),(42,19),(42,18)),('L',(33,24)),('L',(27,28)),('C',(24,30),(24,30),(25,30)),('C',(21,28),(23,30),(24,30)),('L',(15,24)),('L',(9,20)),('C',(6,18),(6,18),(6,19)),('C',(9,16),(6,17),(6,18)),('L',(21,8)),('C',(24,6),(24,6),(23,6))],True)
        self.path('lower-layer',(15,24),[('L',(9,28)),('C',(6,30),(6,30),(6,29)),('C',(9,32),(6,31),(6,30)),('L',(21,40)),('C',(24,42),(24,42),(23,42)),('C',(27,40),(25,42),(24,42)),('L',(39,32)),('C',(42,30),(42,30),(42,31)),('C',(39,28),(42,29),(42,30)),('L',(33,24))])
        self.relate('connect','top-layer','lower-layer')
