"""Two balanced counterclockwise arrows with smooth orbit curves and equal arrowhead arms surround a crisp clock-hand pair.
Omissions: None
Construction references: ['clock'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='ab913828-297d-4c94-ab76-5b92952287d3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__watch-hands/20260924T172356Z-thuan-mac/reference/watch hands_ab913828-297d-4c94-ab76-5b92952287d3.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='watch-hands'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "state"
    categories = ("state",)
    aliases=()
    keywords=('watch', 'hands')

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
        for n,flip in [('top',False),('bottom',True)]:
            def p(x,y):return (48-x,48-y) if flip else (x,y)
            self.path(n,p(40,12),[('C',p(24,6),p(36,8),p(31,6)),('A',p(6,24),18,18,False)])
            self.add_polyline(n+'-head',p(6,18),p(6,24),p(12,24));self.relate('connect',n,n+'-head')
        self.add_polyline('hands',(24,16),(24,28),(28,28))
