from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='7812933e-4da0-4067-9131-d948a045fef8'
SOURCE_PATH='pictographic-primitives/_uncategorized_11/clapboard_7812933e-4da0-4067-9131-d948a045fef8.svg'
AUTHOR='gpt-6'
PLAN='Raised striped clapper above a striped lower band and blank slate; shared left hinge; one stripe per band preserves the clapper vocabulary with wider open regions.'
CONSTRUCTION_REFERENCES='clapperboard: diagonal raised blade and rounded lower slate.'
OMISSIONS=['Stripe count reduced to one on each band.']
class Drawing(Solo48):
    icon_id='movie-production-clapperboard'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
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
        self.add_polyline('clapper',(6,18),(18,14),(30,10),(42,6),(42,14),(30,18),(18,22),(6,26),closed=True)
        self.add_line('upper-stripe',(30,10),(18,22));self.relate('connect','upper-stripe','clapper')
        self.path('slate',(6,26),[('L',(18,26)),('L',(42,26)),('L',(42,34)),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,34)),('L',(6,26))],True)
        self.add_polyline('band-bottom',(6,34),(10,34),(42,34));self.relate('connect','band-bottom','slate')
        self.add_line('lower-stripe',(18,26),(10,34));self.relate('connect','lower-stripe','slate');self.relate('connect','lower-stripe','band-bottom')
        self.relate('connect','clapper','slate')
