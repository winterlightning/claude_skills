"""Hands Cradling Woman with Bob.

Symbol plan: Circular face with outward-flared bob ends above domed shoulders. Omit the narrow neck and hair part; retain the flared silhouette. Matched palms share one definition; detached head-to-shoulder ink gap is exactly 4.
Lucide: hand-heart; original and atomic-debug geometry inspected.
Keyshape: VRECT_L; centerline (8,4)-(40,44); ink (6,2)-(42,46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'de56331a-5d11-40f6-a7a1-1943660a276d'
SOURCE_PATH = 'pictographic-primitives/business/donation charity care person female_de56331a-5d11-40f6-a7a1-1943660a276d.svg'
AUTHOR = 'gpt-6'

class HandsCradlingWomanWithBob(Solo48):
    icon_id = 'hands-cradling-woman-with-bob'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('care', 'hands', 'person', 'support', 'protection', 'community', 'help', 'compassion')

    def build(self):
        self.circle('head',24,10,6)
        for n,mirror in [('left',False),('right',True)]:
            def p(x,y):return (48-x if mirror else x,y)
            self.path(n+'-hair',p(18,10),(*p(14,18),*p(18,14),*p(17,18)));self.relate('connect',n+'-hair','head')
        self.path('shoulders',(18,30),(24,24,6,6,True),(30,30,6,6,True))

        axis=24
        for n,mirror in [('left',False),('right',True)]:
            def p(x,y):return (2*axis-x if mirror else x,y)
            self.path(n+'-hand',p(8,26),p(8,40),(*p(12,44),4,4,mirror),p(20,44),p(20,40),(*p(16,38),*p(20,40),*p(18,38)))

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
