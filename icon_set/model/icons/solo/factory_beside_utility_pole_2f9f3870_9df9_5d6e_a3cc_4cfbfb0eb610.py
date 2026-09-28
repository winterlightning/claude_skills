"""Factory beside Utility Pole.

Symbol plan: A low factory and chimney stand beside an open forked utility pole. Keep their unequal heights and natural industrial scene relationship. The pole crossbar, smoke, doorway and chimney band are omitted.
Lucide: factory; original and atomic-debug geometry inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f9f3870-9df9-5d6e-a3cc-4cfbfb0eb610'
SOURCE_PATH = 'pictographic-primitives/business/factory building_2f9f3870-9df9-5d6e-a3cc-4cfbfb0eb610.svg'
AUTHOR = 'gpt-6'

class FactoryBesideUtilityPole(Solo48):
    icon_id = 'factory-beside-utility-pole'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('factory', 'automation', 'industry', 'manufacturing', 'production', 'machine', 'robot', 'process')

    def build(self):
        self.path('factory',(20,40),(20,28),(26,20),(26,28),(34,28),(34,8),(42,8),(42,28),(44,28),(44,40),(20,40),closed=True)
        self.path('pole',(10,24),(10,40))
        self.path('crossarm',(4,16),(10,24),(16,16));self.relate('connect','pole','crossarm')

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
