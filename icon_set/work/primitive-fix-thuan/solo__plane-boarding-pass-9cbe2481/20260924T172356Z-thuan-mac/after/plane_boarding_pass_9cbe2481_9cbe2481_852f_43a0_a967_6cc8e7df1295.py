"""Boarding ticket with matching rounded corners and semicircular notches, enclosing a clean diagonal plane mark.
Omissions: Ticket divider and plane outline reduced to readable wing, fuselage and tail strokes.
Construction references: ['ticket', 'plane'].
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='9cbe2481-852f-43a0-a967-6cc8e7df1295'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__plane-boarding-pass-9cbe2481/20260924T172356Z-thuan-mac/reference/plane boarding pass_9cbe2481-852f-43a0-a967-6cc8e7df1295.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='plane-boarding-pass-9cbe2481'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('plane', 'boarding', 'pass')

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
        self.path('ticket',(8,8),[('L',(40,8)),('A',(44,12),4,4,True),('L',(44,20)),('A',(44,28),4,4,False),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,28)),('A',(4,20),4,4,False),('L',(4,12)),('A',(8,8),4,4,True)],True)
        self.add_polyline('plane',(16,27),(20,31),(27,24),(33,18))
        self.add_line('wing',(20,17),(27,24));self.relate('connect','plane','wing')
