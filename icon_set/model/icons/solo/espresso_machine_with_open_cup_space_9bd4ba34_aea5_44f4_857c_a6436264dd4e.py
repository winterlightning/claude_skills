"""Espresso Machine with Open Cup Space.

Symbol plan: A tall C-shaped appliance owns the brew head and one structural control; open cup space remains empty.
Lucide construction: drill; original and atomic-debug inspected.
Keyshape: VRECT_L; centerline (8,4)-(40,44); ink (6,2)-(42,46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9bd4ba34-aea5-44f4-857c-a6436264dd4e'
SOURCE_PATH = 'pictographic-primitives/clothes/coffee espresso machine_9bd4ba34-aea5-44f4-857c-a6436264dd4e.svg'
AUTHOR = 'gpt-6'


class EspressoMachineWithOpenCupSpace(Solo48):
    icon_id = 'espresso-machine-with-open-cup-space'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('espresso', 'machine', 'with', 'open', 'cup', 'space')

    def build(self):
        self.path('body',(12,4),(36,4),(40,8,4,4,True),(40,40),(36,44,4,4,True),(8,44),(8,36),(20,36),(24,32,4,4,False),(24,24),(20,20,4,4,False),(16,20),(8,20),(8,8),(12,4,4,4,True),closed=True)
        self.add_line('spout',(16,20),(16,26));self.relate('connect','spout','body')
        self.add_dot('control',(31,13))

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
