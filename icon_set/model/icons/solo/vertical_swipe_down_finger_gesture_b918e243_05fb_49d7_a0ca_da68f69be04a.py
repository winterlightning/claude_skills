"""Horizontal finger with rounded nail and a smoothly bowed downward motion arrow.
Omissions: None
Construction references: ['hand'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='b918e243-05fb-49d7-a0ca-da68f69be04a'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__vertical-swipe-down-finger-gesture/20260924T172356Z-thuan-mac/reference/gesture swipe vertical down_b918e243-05fb-49d7-a0ca-da68f69be04a.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='vertical-swipe-down-finger-gesture'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('gesture', 'swipe', 'vertical', 'down')

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
        self.path('finger',(4,11),[('L',(18,11)),('A',(18,37),13,13,True),('L',(4,37))])
        self.path('nail',(12,20),[('L',(17,20)),('A',(17,28),4,4,True),('L',(12,28)),('L',(12,20))],True)
        self.path('swipe',(38,8),[('C',(44,24),(42,13),(44,18)),('C',(36,40),(44,30),(40,36))])
        self.add_polyline('head',(38,32),(36,40),(44,38));self.relate('connect','head','swipe')
