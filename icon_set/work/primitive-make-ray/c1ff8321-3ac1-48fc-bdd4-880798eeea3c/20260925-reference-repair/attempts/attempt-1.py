from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='c1ff8321-3ac1-48fc-bdd4-880798eeea3c'
SOURCE_PATH='pictographic-primitives/other/hand holding_c1ff8321-3ac1-48fc-bdd4-880798eeea3c.svg'
AUTHOR='gpt-6'
PLAN='Mirrored cupped hands with rounded tall fingers, visible inward thumb folds and curved palms.'
CONSTRUCTION_REFERENCES='Lucide hand: coherent finger/palm curves. Supplied reference: paired cupped gesture and thumb branches.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='two-open-cupped-hands'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('hand', 'holding')

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
            def p(x,y):return (x,y) if side==-1 else (48-x,y)
            n='left' if side==-1 else 'right'
            self.path(n+'-outer',p(12,40),[('L',p(12,35)),('C',p(4,22),p(12,31),p(4,29)),('L',p(4,12)),('A',p(12,12),4,4,side==-1),('L',p(12,18))])
            self.path(n+'-thumb-palm',p(16,26),[('L',p(10,20)),('C',p(12,18),p(9,19),p(10,18)),('C',p(20,32),p(18,23),p(20,26)),('L',p(20,40))])
            self.relate('connect',n+'-outer',n+'-thumb-palm')
