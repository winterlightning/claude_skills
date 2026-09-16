"""Football Pitch in Perspective.

Symbol plan: A trapezoidal field carries an oval centre circle and halfway line. The line stops at the circle boundary to retain one clear opening. Omit the small near and far penalty boxes; mirrored perspective preserves the pitch.
Lucide: goal; original and atomic-debug geometry inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f73dffbc-69a9-40dd-acf9-a2809f053a9c'
SOURCE_PATH = 'pictographic-primitives/building/field_f73dffbc-69a9-40dd-acf9-a2809f053a9c.svg'
AUTHOR = 'gpt-6'

class FootballPitchInPerspective(Solo48):
    icon_id = 'football-pitch-in-perspective'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('football', 'pitch', 'field', 'sport', 'stadium', 'plan', 'soccer', 'playing field')

    def build(self):
        self.path('pitch',(12,8),(36,8),(40,24),(44,40),(4,40),(8,24),(12,8),closed=True)
        self.path('centre',(18,24),(24,20,6,4,True),(30,24,6,4,True),(24,28,6,4,True),(18,24,6,4,True),closed=True)
        self.add_line('half-left',(8,24),(18,24));self.add_line('half-right',(30,24),(40,24))
        for n in ('half-left','half-right'):self.relate('connect',n,'pitch');self.relate('connect',n,'centre')

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
