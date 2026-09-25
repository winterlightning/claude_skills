"""Sewing Machine with Round Control.

Symbol plan: A rounded C-shaped body owns an open throat, needle and circular control. Wide body replaces tiny base bands.
Lucide construction: drill; original and atomic-debug inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0d1021fd-f2b9-45af-8ac0-77171e9e3be9'
SOURCE_PATH = 'pictographic-primitives/clothes/clothes design sewing machine_0d1021fd-f2b9-45af-8ac0-77171e9e3be9.svg'
AUTHOR = 'gpt-6'


class SewingMachineWithRoundControl(Solo48):
    icon_id = 'sewing-machine-with-round-control'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('sewing', 'machine', 'with', 'round', 'control')

    def build(self):
        self.path('body',(8,8),(40,8),(44,12,4,4,True),(44,36),(40,40,4,4,True),(8,40),(4,36,4,4,True),(4,32),(18,32),(22,28,4,4,False),(22,24),(18,20,4,4,False),(12,20),(4,20),(4,12),(8,8,4,4,True),closed=True)
        self.add_line('needle',(12,20),(12,24));self.relate('connect','needle','body')
        self.circle('control',33,26,2)

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
