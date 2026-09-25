from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='2543e428-8532-5444-9cdb-344b1eca155c'
SOURCE_PATH='pictographic-primitives/artificial-intelligence/brain_2543e428-8532-5444-9cdb-344b1eca155c.svg'
AUTHOR='gpt-6'
PLAN='Paired organic brain hemispheres with scalloped upper and lower lobes, central fissure and two folds on each side.'
CONSTRUCTION_REFERENCES='Lucide brain: organic bilateral lobes and inward folds; supplied source controls straight central fissure.'
OMISSIONS=['Fine perimeter wrinkles condensed into broad lobes; two folds per side retained.']
class Drawing(Solo48):
    icon_id='human-brain-top-view'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'artificial-intelligence'
    aliases=()
    keywords=('brain',)

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
        for side in (-1,1):
            p=lambda x,y:(x,y) if side==-1 else (48-x,y)
            n='left' if side==-1 else 'right'
            self.path(n+'-hemisphere',p(24,12),[('C',p(18,6),p(24,8),p(22,6)),('C',p(10,14),p(13,6),p(10,9)),('C',p(6,23),p(6,14),p(6,19)),('C',p(10,32),p(6,29),p(8,31)),('C',p(18,42),p(9,38),p(14,42)),('C',p(24,36),p(22,42),p(24,40))])
            self.path(n+'-upper-fold',p(10,14),[('C',p(16,20),p(14,14),p(16,16))]);self.relate('connect',n+'-upper-fold',n+'-hemisphere')
            self.path(n+'-lower-fold',p(10,32),[('C',p(16,28),p(10,28),p(13,28))]);self.relate('connect',n+'-lower-fold',n+'-hemisphere')
        self.add_line('fissure',(24,12),(24,36))
        for n in ('left','right'):self.relate('connect','fissure',n+'-hemisphere')
        self.relate('connect','left-hemisphere','right-hemisphere')
