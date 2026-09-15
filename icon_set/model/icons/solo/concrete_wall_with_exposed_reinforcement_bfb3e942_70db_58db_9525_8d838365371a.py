"""Concrete Wall with Exposed Reinforcement.

Symbol plan: A stepped concrete silhouette owns a regular two-column exposed reinforcement grid.
Lucide construction: construction; original and atomic-debug inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bfb3e942-70db-58db-9525-8d838365371a'
SOURCE_PATH = 'pictographic-primitives/construction/construction fence_bfb3e942-70db-58db-9525-8d838365371a.svg'
AUTHOR = 'gpt-6'


class ConcreteWallWithExposedReinforcement(Solo48):
    icon_id = 'concrete-wall-with-exposed-reinforcement'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    aliases = ()
    keywords = ('concrete', 'wall', 'with', 'exposed', 'reinforcement')

    def build(self):
        self.path('concrete',(6,6),(14,6),(14,14),(14,22),(24,32),(30,32),(42,32),(42,42),(6,42),(6,6),closed=True)
        for n,x in [('near',30),('far',42)]:
            self.path(n+'-rod',(x,6),(x,14),(x,22),(x,32));self.relate('connect',n+'-rod','concrete')
        for y in (14,22):
            self.path('cross-'+str(y),(14,y),(30,y),(42,y))
            for n in ('concrete','near-rod','far-rod'):self.relate('connect','cross-'+str(y),n)

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
