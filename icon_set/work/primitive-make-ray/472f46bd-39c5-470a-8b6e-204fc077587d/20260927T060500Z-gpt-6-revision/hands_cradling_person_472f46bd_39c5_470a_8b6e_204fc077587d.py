"""Hands Cradling Person.

Symbol plan: A small person sits between mirrored open hands with long outer fingers and shorter thumbs. Finger creases are omitted. Circular head and smooth shoulders retain exactly 4 units of detached ink clearance.
Lucide: hand-heart; original and atomic-debug geometry inspected.
Keyshape: VRECT_L; centerline (8,4)-(40,44); ink (6,2)-(42,46).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '472f46bd-39c5-470a-8b6e-204fc077587d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-cradling-person/20260927T060349Z-thuan-mac-1/reference/customer retention hands_472f46bd-39c5-470a-8b6e-204fc077587d.svg'
AUTHOR = 'gpt-6'


class HandsCradlingPerson(Solo48):
    icon_id = 'hands-cradling-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('care', 'hands', 'person', 'support', 'protection', 'community', 'help', 'compassion')

    def build(self):
        axis=24
        self.circle('head',axis,8,4)
        self.path('shoulders',(18,26),(axis,20,6,6,True),(30,26,6,6,True))
        for n,mirror in [('left',False),('right',True)]:
            def p(x,y):return (2*axis-x if mirror else x,y)
            self.path(n+'-hand', p(8,24), p(8,34), (*p(12,41), *p(8,38), *p(10,40)), p(14,44), p(20,44), p(20,39), (*p(12,35), *p(20,36), *p(16,35)), p(10,34))

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
