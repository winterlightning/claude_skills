from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='d7b60535-d86c-4822-a2a7-f6c1499603fc'
SOURCE_PATH='pictographic-primitives/other/folder file_d7b60535-d86c-4822-a2a7-f6c1499603fc.svg'
AUTHOR='gpt-6'
PLAN='Tall beveled document behind a smaller lower-left tabbed folder, with two document lines.'
CONSTRUCTION_REFERENCES='Lucide folder-open: folder tab and rounded corners; source owns the page-in-back layering.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='document-behind-folder'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('folder', 'file')

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

        self.add_line('page-left',(12,28),(12,10))
        self.add_arc('page-corner',(12,10),(16,6),radius_x=4)
        self.add_line('page-top',(16,6),(32,6))
        self.add_line('page-bevel',(32,6),(42,16))
        self.add_line('page-right',(42,16),(42,38))
        self.add_arc('page-bottom-corner',(42,38),(38,42),radius_x=4)
        self.add_line('page-bottom',(38,42),(30,42))
        members=['page-left','page-corner','page-top','page-bevel','page-right','page-bottom-corner','page-bottom']
        for a,b in zip(members,members[1:]):self.relate('connect',a,b)
        self.path('folder',(6,32),[('A',(10,28),4,4,True),('L',(12,28)),('L',(14,28)),('L',(18,32)),('L',(26,32)),('A',(30,36),4,4,True),('L',(30,42)),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,32))],True)
        self.add_line('text-top',(20,14),(28,14));self.add_line('text-bottom',(20,22),(32,22))
        self.relate('connect','page-left','folder');self.relate('connect','page-bottom','folder')
