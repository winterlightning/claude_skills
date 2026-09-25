"""Two equal square sliders on straight vertical rails beside a Bitcoin B with smooth elliptical bowls and an exposed currency stem.
Omissions: Second Bitcoin stem reduced to one at 48px.
Construction references: ['sliders-vertical'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='807318c5-21cc-453f-a7fa-a1c902d1a221'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__bitcoin-with-adjust/20260924T172356Z-thuan-mac/reference/bitcoin with adjust_807318c5-21cc-453f-a7fa-a1c902d1a221.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='bitcoin-with-adjust'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('bitcoin', 'with', 'adjust')

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
        for n,x,y in [('low',8,32),('high',20,16)]:
            self.path(n,(x,y-4),[('L',(x+4,y-4)),('L',(x+4,y+4)),('L',(x,y+4)),('L',(x-4,y+4)),('L',(x-4,y-4)),('L',(x,y-4))],True)
            self.add_line(n+'-up',(x,8),(x,y-4));self.add_line(n+'-down',(x,y+4),(x,40))
            self.relate('connect',n,n+'-up');self.relate('connect',n,n+'-down')
        self.add_polyline('stem',(33,8),(33,12),(33,24),(33,36),(33,40))
        self.path('bowls',(33,12),[('L',(36,12)),('A',(36,24),8,6,True),('A',(36,36),8,6,True),('L',(33,36))])
        self.relate('connect','stem','bowls')
        self.add_line('middle',(33,24),(36,24));self.relate('connect','middle','bowls');self.relate('connect','middle','stem')
