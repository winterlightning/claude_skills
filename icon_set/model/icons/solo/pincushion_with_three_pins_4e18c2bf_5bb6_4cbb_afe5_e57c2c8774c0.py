"""Pincushion with Three Pins.

Symbol plan: A circular dome with three round pinheads; mirrored outer pins and a central pin. Small round heads retain the pin identity.
Lucide construction: pin; original and atomic-debug inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e18c2bf-5bb6-4cbb-afe5-e57c2c8774c0'
SOURCE_PATH = 'pictographic-primitives/clothes/clothes design pin cushion_4e18c2bf-5bb6-4cbb-afe5-e57c2c8774c0.svg'
AUTHOR = 'gpt-6'


class PincushionWithThreePins(Solo48):
    icon_id = 'pincushion-with-three-pins'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    aliases = ()
    keywords = ('pincushion', 'with', 'three', 'pins')

    def build(self):
        self.path('cushion',(4,40),(12,24,20,20,True),(24,20,20,20,True),(36,24,20,20,True),(44,40,20,20,True),(4,40),closed=True)
        for n,x,head_y,tip in [('left',6,14,(12,24)),('middle',24,10,(24,20)),('right',42,14,(36,24))]:
            self.path(n+'-head',(x,head_y+2),(x,head_y-2,2,2,True),(x,head_y+2,2,2,True),closed=True)
            self.add_line(n+'-pin',(x,head_y+2),tip)
            self.relate('connect',n+'-pin','cushion');self.relate('connect',n+'-pin',n+'-head')

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
