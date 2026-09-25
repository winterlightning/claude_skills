"""A smooth semicircular grill bowl on matching splayed legs under three gentle smoke curves.
Omissions: Lower leg brace omitted to preserve open space.
Construction references: ['soup'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='b55f60b7-bd1e-53bf-a79a-b549edab3c92'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__smoking-barbecue-grill/20260924T172356Z-thuan-mac/reference/barbecue grill_b55f60b7-bd1e-53bf-a79a-b549edab3c92.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='smoking-barbecue-grill-solo'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "food"
    categories = ("primitives", "food")
    aliases=()
    keywords=('barbecue', 'grill')

    def path(self, name, start, commands, closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            eid=f'{name}-{i}'; ids.append(eid)
            if c[0]=='L': self.add_line(eid,here,c[1])
            elif c[0]=='A': self.add_arc(eid,here,c[1],radius_x=c[2],radius_y=c[3],sweep=c[4],large_arc=c[5] if len(c)>5 else False)
            elif c[0]=='C': self.add_bezier(eid,here,(c[2],c[3],c[1]))
            here=c[1]
        self.add_contour(name,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,x,y,w,h,r):
        self.path(n,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)

    def build(self):
        self.path('bowl',(6,22),[('L',(42,22)),('C',(33,32),(42,27),(37,30)),('C',(24,34),(29,34),(27,34)),('C',(15,32),(21,34),(19,34)),('C',(6,22),(11,30),(6,27))],True)
        for n,x,z in [('left',15,10),('right',33,38)]:
            self.add_line('leg-'+n,(x,32),(z,42));self.relate('connect','leg-'+n,'bowl')
        for j,x in enumerate((14,24,34)):
            self.path('smoke-'+str(j),(x,6),[('C',(x,13),(x-3,8),(x+3,11))])
