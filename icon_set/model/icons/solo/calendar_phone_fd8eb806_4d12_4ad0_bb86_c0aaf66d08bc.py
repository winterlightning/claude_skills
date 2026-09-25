"""Calendar with identical rounded corners and bindings; phone receiver is one coherent flowing contour.
Omissions: Handset pads rendered as short ends instead of tiny enclosed pads.
Construction references: ['calendar'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='fd8eb806-4d12-4ad0-bb86-c0aaf66d08bc'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__calendar-phone/20260924T172356Z-thuan-mac/reference/calendar phone_fd8eb806-4d12-4ad0-bb86-c0aaf66d08bc.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='calendar-phone'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('calendar', 'phone')

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
        self.path('frame',(12,8),[('L',(16,8)),('L',(32,8)),('L',(36,8)),('A',(40,12),4,4,True),('L',(40,17)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,17)),('L',(8,12)),('A',(12,8),4,4,True)],True)
        self.add_line('header',(8,17),(40,17));self.relate('connect','header','frame')
        for x in (16,32):
            self.add_line('binding-'+str(x),(x,4),(x,8));self.relate('connect','binding-'+str(x),'frame')
        self.path('phone',(20,26),[('L',(17,29)),('C',(27,35),(19,33),(24,35)),('L',(31,31)),('L',(29,29))])
