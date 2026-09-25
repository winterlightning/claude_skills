from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='6da646a1-34eb-51f2-af2d-b08aed786a57'
SOURCE_PATH='pictographic-primitives/computers/batch-06/keyboard_6da646a1-34eb-51f2-af2d-b08aed786a57.svg'
AUTHOR='gpt-6'
PLAN='Rounded keyboard with two aligned rows of short key marks and a separate broad spacebar.'
CONSTRUCTION_REFERENCES='Lucide keyboard: two key rows and spacebar; supplied source uses short dash keys.'
OMISSIONS=['Four keys per row reduced to three to retain legal spacing; both rows preserved.']
class Drawing(Solo48):
    icon_id='computer-typing-keyboard'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('keyboard',)

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
        self.box('case',4,8,44,40,4,split=True)
        for row,y in enumerate((16,24)):
            for col,x in enumerate((14,24,34)):self.add_line(f'key-{row}-{col}',(x-1,y),(x+1,y))
        self.add_line('spacebar',(14,32),(34,32))
