"""Hands Cradling Continuous Person Bust.

Symbol plan: A rounded head flows through an explicit narrow neck into the shoulders, preserving the continuous anatomy of the reference. Mirrored open palms frame it. Omit the thumb creases; no detached-head gap applies to this continuous silhouette.
Lucide: hand-heart; original and atomic-debug geometry inspected.
Keyshape: VRECT_L; centerline (8,4)-(40,44); ink (6,2)-(42,46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ddc30f7b-9b10-45e2-bbee-111110335859'
SOURCE_PATH = 'pictographic-primitives/business/donation charity care person male_ddc30f7b-9b10-45e2-bbee-111110335859.svg'
AUTHOR = 'gpt-6'

class HandsCradlingContinuousPersonBust(Solo48):
    icon_id = 'hands-cradling-continuous-person-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('care', 'hands', 'person', 'support', 'protection', 'community', 'help', 'compassion')

    def build(self):
        self.path('bust',(16,26),(20,24,18,25,20,24),(20,20),(18,10,18,18,18,14),(24,4,6,6,True),(30,10,6,6,True),(28,20,30,14,30,18),(28,24),(32,26,28,24,30,25))

        axis=24
        for n,mirror in [('left',False),('right',True)]:
            def p(x,y):return (2*axis-x if mirror else x,y)
            self.path(n+'-hand',p(8,28),p(8,40),(*p(12,44),4,4,mirror),p(20,44),p(20,40),(*p(16,36),*p(20,38),*p(18,36)))

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
