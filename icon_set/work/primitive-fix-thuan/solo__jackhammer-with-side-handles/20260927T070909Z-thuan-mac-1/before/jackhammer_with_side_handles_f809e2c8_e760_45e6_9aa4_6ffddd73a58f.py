"""Jackhammer with Side Handles.

Symbol plan: A symmetric rounded housing steps into a narrower lower barrel and bit. Mirrored side grips share the shoulder junctions; internal controls are omitted.
Lucide construction: drill; original and atomic-debug inspected.
Keyshape: VRECT_L; centerline (8,4)-(40,44); ink (6,2)-(42,46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f809e2c8-e760-45e6-9aa4-6ffddd73a58f'
SOURCE_PATH = 'pictographic-primitives/construction/construction drill_f809e2c8-e760-45e6-9aa4-6ffddd73a58f.svg'
AUTHOR = 'gpt-6'


class JackhammerWithSideHandles(Solo48):
    icon_id = 'jackhammer-with-side-handles'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('jackhammer', 'with', 'side', 'handles')

    def build(self):
        axis=24
        self.path('housing',(axis,4),(32,12,8,8,True),(32,22),(30,24,2,2,True),(28,24),(28,32),(24,36,4,4,True),(20,32,4,4,True),(20,24),(18,24),(16,22,2,2,True),(16,12),(axis,4,8,8,True),closed=True)
        for n,x,tip in [('left',16,8),('right',32,40)]:
            self.add_line(n+'-grip',(x,12),(tip,12));self.relate('connect',n+'-grip','housing')
        self.add_line('bit',(24,36),(24,44));self.relate('connect','bit','housing')

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
