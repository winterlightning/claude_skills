"""Horizontal paired fingers beside a single smooth descending gesture arrow.
Omissions: Second finger kept as a single open lower edge as in the reference.
Construction references: ['hand'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='a3e6d289-ee88-4de3-ba1a-d29da5c5d1e9'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__two-finger-swipe-down-gesture/20260924T172356Z-thuan-mac/reference/gesture swipe vertical down two fingers_a3e6d289-ee88-4de3-ba1a-d29da5c5d1e9.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='two-finger-swipe-down-gesture'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('gesture', 'swipe', 'vertical', 'down', 'two', 'fingers')

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
        self.path('upper',(4,14),[('L',(26,14)),('A',(26,22),4,4,True),('L',(4,22))])
        self.add_line('lower',(4,32),(21,32))
        self.path('swipe',(36,8),[('C',(44,23),(41,12),(44,17)),('C',(34,40),(44,29),(40,35))])
        self.add_polyline('head',(31,31),(34,40),(43,37));self.relate('connect','head','swipe')
