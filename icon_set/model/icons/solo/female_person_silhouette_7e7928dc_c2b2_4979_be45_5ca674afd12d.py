from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='7e7928dc-c2b2-4979-be45-5ca674afd12d'
SOURCE_PATH='pictographic-primitives/other/full body women_7e7928dc-c2b2-4979-be45-5ca674afd12d.svg'
AUTHOR='gpt-6'
PLAN='Circular detached head above rounded shoulders, sloped blouse sides and tapered lower section; remove the prior arrow-like shoulder corners.'
CONSTRUCTION_REFERENCES='human_ref/user.svg and full_body_ref.png: circular head and simple coherent body; source owns the blouse and lower outline.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='female-person-silhouette'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('full', 'body', 'women')

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

        self.circle('head',24,10,6)
        self.path('body',(22,24),[('L',(26,24)),('C',(33,29),(30,24),(32,26)),('L',(40,38)),('L',(31,38)),('L',(29,44)),('L',(19,44)),('L',(17,38)),('L',(8,38)),('L',(15,29)),('C',(22,24),(16,26),(18,24))],True)

HUMAN_CONSTRUCTION_REVIEW = {'references': ['icon_set/references/human_ref/user.svg', 'icon_set/references/human_ref/full_body_ref.png'], 'head_center': [24, 10], 'head_radius': 6, 'body_top': 24, 'head_to_body_ink_gap': 4, 'proof': '24-(10+6)-4=4; nearest body point (24,24) is on its horizontal shoulder segment.'}
