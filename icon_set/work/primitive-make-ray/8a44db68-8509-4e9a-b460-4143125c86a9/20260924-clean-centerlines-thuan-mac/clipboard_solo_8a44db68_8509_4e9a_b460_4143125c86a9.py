"""Clipboard with tangent radius-4 corners and a rounded capsule clip. Page terminates at clip side nodes.
Omissions: None
Construction references: ['clipboard'].
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='8a44db68-8509-4e9a-b460-4143125c86a9'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__clipboard-solo/20260924T171046Z-thuan-mac/reference/clipboard_8a44db68-8509-4e9a-b460-4143125c86a9.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='clipboard-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('clipboard',)

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
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,x,y,w,h,r):
        self.path(n,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)

    def build(self):
        self.path('clip',(20,4),[('L',(28,4)),('A',(28,12),4,4,True),('L',(20,12)),('A',(20,4),4,4,True)],True)
        self.path('page',(16,8),[('L',(12,8)),('A',(8,12),4,4,False),('L',(8,40)),('A',(12,44),4,4,False),('L',(36,44)),('A',(40,40),4,4,False),('L',(40,12)),('A',(36,8),4,4,False),('L',(32,8))])
        self.relate('connect','page','clip')
