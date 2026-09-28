"""Factory Control Console beside Conveyor.

Symbol plan: A tall control console stands beside a parcel on a short conveyor. Simplify the display to a mark and retain one button. Omit the package seam and roller marks.
Lucide: briefcase-conveyor-belt; original and atomic-debug geometry inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6fe570bc-a430-487a-b050-d50ad1529288'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__factory-control-console-beside-conveyor/20260927T032256Z-thuan-mac-1/reference/factory manufacturing plan box_6fe570bc-a430-487a-b050-d50ad1529288.svg'
AUTHOR = 'gpt-6'

class FactoryControlConsoleBesideConveyor(Solo48):
    icon_id = 'factory-control-console-beside-conveyor'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('factory', 'automation', 'industry', 'manufacturing', 'production', 'machine', 'robot', 'process')

    def build(self):
        self.path('console',(4,8),(20,8),(20,24),(20,40),(4,40),(4,24),(4,8),closed=True)
        self.add_line('panel',(4,24),(20,24));self.relate('connect','panel','console')
        self.add_dot('display',(12,16));self.add_dot('button',(12,32))
        self.path('belt',(32,32),(40,32),(44,36,4,4,True),(40,40,4,4,True),(32,40),(28,36,4,4,True),(32,32,4,4,True),closed=True)
        self.add_line('post',(34,20),(34,32))
        self.relate('connect','post','belt')

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
