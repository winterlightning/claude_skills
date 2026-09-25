"""Electricity Pylon with Lower Crossarm.

Symbol plan: A tapered pylon carries a broad lower crossarm and a mirrored pair of crossing lower braces. Exact shared nodes retain the lattice. Triangular side-arm frames and extra upper braces reduce to a single crossarm to avoid cramped openings.
Lucide: utility-pole; original and atomic-debug geometry inspected.
Keyshape: VRECT_L; centerline (8,4)-(40,44); ink (6,2)-(42,46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb64d367-e318-4e6f-a967-aab5e9828e09'
SOURCE_PATH = 'pictographic-primitives/construction/electricity tower 1_cb64d367-e318-4e6f-a967-aab5e9828e09.svg'
AUTHOR = 'gpt-6'

class ElectricityPylonWithLowerCrossarm(Solo48):
    icon_id = 'electricity-pylon-with-lower-crossarm'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('power line', 'pylon', 'electricity', 'pole', 'transmission', 'infrastructure', 'energy', 'utility')

    def build(self):
        self.path('tower',(12,44),(16,24),(20,4),(28,4),(32,24),(36,44))
        self.path('crossarm',(8,24),(16,24),(32,24),(40,24));self.relate('connect','crossarm','tower')
        self.path('brace-a',(16,24),(24,32),(36,44))
        self.path('brace-b',(32,24),(24,32),(12,44))
        for n in ('brace-a','brace-b'):
            self.relate('connect',n,'tower');self.relate('connect',n,'crossarm')
        self.relate('connect','brace-a','brace-b')

    def path(self, name, start, *steps, closed=False):
        members=[]
        point=start
        for index, step in enumerate(steps):
            member=f"{name}-{index+1}"
            if len(step)==2:
                self.add_line(member,point,step)
                point=step
            elif len(step)==5:
                x,y,rx,ry,sweep=step
                self.add_arc(member,point,(x,y),radius_x=rx,radius_y=ry,sweep=sweep)
                point=(x,y)
            else:
                x,y,cx1,cy1,cx2,cy2=step
                self.add_bezier(member,point,((cx1,cy1),(cx2,cy2),(x,y)))
                point=(x,y)
            members.append(member)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x,y-r),(x+r,y,r,r,True),(x,y+r,r,r,True),
                  (x-r,y,r,r,True),(x,y-r,r,r,True),closed=True)

    def rect(self,name,x,y,w,h,r=2):
        self.path(name,(x+r,y),(x+w-r,y),(x+w,y+r,r,r,True),
                  (x+w,y+h-r),(x+w-r,y+h,r,r,True),(x+r,y+h),
                  (x,y+h-r,r,r,True),(x,y+r),(x+r,y,r,r,True),closed=True)
