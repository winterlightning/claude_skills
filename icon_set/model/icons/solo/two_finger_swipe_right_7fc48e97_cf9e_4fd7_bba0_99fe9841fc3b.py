"""Two matching finger arches below a gently curved rightward swipe arrow.
Omissions: None
Construction references: ['hand'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='7fc48e97-cf9e-4fd7-bba0-99fe9841fc3b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__two-finger-swipe-right-solo/20260924T172356Z-thuan-mac/reference/gesture flip right_7fc48e97-cf9e-4fd7-bba0-99fe9841fc3b.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='two-finger-swipe-right-solo'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('gesture', 'flip', 'right')

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
        for i,x in enumerate((4,30)):
            self.path('finger-'+str(i),(x,40),[('L',(x,31)),('A',(x+14,31),7,7,True),('L',(x+14,40))])
        self.path('swipe',(20,8),[('C',(42,16),(29,8),(36,12))])
        self.add_polyline('head',(36,8),(42,16),(32,16));self.relate('connect','head','swipe')
