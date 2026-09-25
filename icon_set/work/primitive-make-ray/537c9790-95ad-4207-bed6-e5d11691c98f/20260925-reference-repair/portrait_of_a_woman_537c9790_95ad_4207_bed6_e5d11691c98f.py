from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='537c9790-95ad-4207-bed6-e5d11691c98f'
SOURCE_PATH='pictographic-primitives/other/artist_537c9790-95ad-4207-bed6-e5d11691c98f.svg'
AUTHOR='gpt-6'
PLAN='Asymmetric left-facing portrait with long hair behind the right shoulder, a blank round face, connected neck and curved shirt neckline.'
CONSTRUCTION_REFERENCES='Shared human_ref/user.svg: round face and shoulder vocabulary. Supplied artist reference: asymmetric long hair, connected neck and neckline.'
OMISSIONS=['Source oval face regularized to the shared circular human vocabulary; long hair, real neck and asymmetric shoulders retained.']
class Drawing(Solo48):
    icon_id='portrait-of-a-woman'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('artist',)

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

    def build(self):
        # Face sits left of the long hair, preserving the asymmetric reference silhouette.
        self.path('face',(18,6),[('A',(28,16),10,10,True),('A',(24,24),10,10,True),('A',(12,24),10,10,True),('A',(8,16),10,10,True),('A',(18,6),10,10,True)],True)
        self.path('hair',(18,6),[('C',(30,4),(22,4),(27,4)),('C',(40,26),(40,4),(40,14)),('C',(38,34),(40,29),(39,32))]);self.relate('connect','hair','face')
        self.path('left-body',(8,44),[('C',(10,34),(8,39),(9,36)),('L',(12,32)),('L',(12,24))]);self.relate('connect','left-body','face')
        self.path('right-body',(24,24),[('L',(24,34)),('C',(38,34),(30,30),(34,30)),('C',(40,44),(40,37),(40,41))]);self.relate('connect','right-body','face');self.relate('connect','right-body','hair')
        self.path('neckline',(10,34),[('C',(24,34),(14,40),(20,40))]);self.relate('connect','neckline','left-body');self.relate('connect','neckline','right-body')
        # Real connected neck retained; no detached-head spacing declaration.
