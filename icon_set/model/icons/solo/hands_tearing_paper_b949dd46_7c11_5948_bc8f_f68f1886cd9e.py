"""Hands Tearing Paper.

Symbol plan: Mirrored hands with round thumbs grip two jagged paper halves. Finger creases and the hidden lower paper edges are omitted.
Lucide construction: hand; original and atomic-debug inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b949dd46-7c11-5948-bc8f-f68f1886cd9e'
SOURCE_PATH = 'pictographic-primitives/business/contract break_b949dd46-7c11-5948-bc8f-f68f1886cd9e.svg'
AUTHOR = 'gpt-6'


class HandsTearingPaper(Solo48):
    icon_id = 'hands-tearing-paper'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('hands', 'tearing', 'paper')

    def build(self):
        axis=24
        for name,mirror in [('left',False),('right',True)]:
            def p(x,y):return (2*axis-x if mirror else x,y)
            self.path(name+'-paper',p(4,22),p(4,8),p(20,8),p(18,14),p(20,20))
            self.path(name+'-hand',p(4,40),p(4,22),(*p(12,22),4,4,not mirror),p(12,30),p(16,34),p(16,40))
            self.relate('connect',name+'-paper',name+'-hand')

    def path(self, name, start, *steps, closed=False):
        members=[]
        point=start
        for i, step in enumerate(steps):
            member=f"{name}-{i+1}"
            if len(step)==2:
                self.add_line(member, point, step)
                point=step
            else:
                x,y,rx,ry,sweep=step
                self.add_arc(member, point, (x,y), radius_x=rx, radius_y=ry, sweep=sweep)
                point=(x,y)
            members.append(member)
        self.add_contour(name,*members,closed=closed)

    def circle(self, name, x, y, r):
        self.path(name,(x-r,y),(x+r,y,r,r,True),(x-r,y,r,r,True),closed=True)

    def rect(self, name, x, y, w, h, r=2):
        self.path(name,(x+r,y),(x+w-r,y),(x+w,y+r,r,r,True),
                  (x+w,y+h-r),(x+w-r,y+h,r,r,True),(x+r,y+h),
                  (x,y+h-r,r,r,True),(x,y+r),(x+r,y,r,r,True),closed=True)
