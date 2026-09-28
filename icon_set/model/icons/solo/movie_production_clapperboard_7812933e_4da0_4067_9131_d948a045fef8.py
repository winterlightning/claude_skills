from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='7812933e-4da0-4067-9131-d948a045fef8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__movie-production-clapperboard/20260927T142540Z-thuan-mac-1/reference/clapboard_7812933e-4da0-4067-9131-d948a045fef8.svg'
AUTHOR='gpt-6'
PLAN='A broad raised clapper pivots from the left over a complete slate with one horizontal band.'
CONSTRUCTION_REFERENCES='Lucide clapperboard original and atomic-debug: raised striped blade and rounded slate.'
OMISSIONS=['Fine blade stripes omitted because they close at 48 pixels.']
class Drawing(Solo48):
    icon_id='movie-production-clapperboard'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('clapboard',)

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
        # Wide raised clapper pivots at the left rim of a complete slate.
        self.add_polyline('blade',(6,16),(36,6),(40,6),(42,14),(8,25),closed=True)
        self.path('slate',(8,25),[('L',(42,25)),('L',(42,38)),
                     ('A',(38,42),4,4,True),('L',(12,42)),
                     ('A',(8,38),4,4,True),('L',(8,25))],True)
        self.add_line('slate-band',(8,33),(42,33))
        self.relate('connect','blade','slate')
        self.relate('connect','slate','slate-band')
