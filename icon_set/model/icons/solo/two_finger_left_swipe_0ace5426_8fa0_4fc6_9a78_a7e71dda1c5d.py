"""Two matching upright fingertips under a smooth leftward motion arrow, with a clearly open arrowhead.
Omissions: None
Construction references: ['hand'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='0ace5426-8fa0-4fc6-9a78-a7e71dda1c5d'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__two-finger-left-swipe/20260924T172356Z-thuan-mac/reference/gesture swipe horizontal left two fingers_0ace5426-8fa0-4fc6-9a78-a7e71dda1c5d.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='two-finger-left-swipe'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('gesture', 'swipe', 'horizontal', 'left', 'two', 'fingers')

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
        for i,x in enumerate((9,29)):
            self.path('finger-'+str(i),(x,40),[('L',(x,29)),('A',(x+10,29),5,5,True),('L',(x+10,40))])
        self.path('swipe',(44,16),[('C',(24,8),(38,11),(31,8)),('C',(4,16),(17,8),(10,11))])
        self.add_polyline('head',(10,8),(4,16),(14,16));self.relate('connect','swipe','head')
