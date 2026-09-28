"""Factory with Domed Hall and Chimney.

Symbol plan: A domed industrial hall adjoins a lower annex and tall chimney. Keep one doorway and the dome; omit the chimney band. Exact shared wall nodes organize the joined building.
Lucide: factory; original and atomic-debug geometry inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48562f00-7693-5f6f-81ad-6e233604135a'
SOURCE_PATH = 'pictographic-primitives/business/factory building_48562f00-7693-5f6f-81ad-6e233604135a.svg'
AUTHOR = 'gpt-6'

class FactoryWithDomedHallAndChimney(Solo48):
    icon_id = 'factory-with-domed-hall-and-chimney'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('factory', 'automation', 'industry', 'manufacturing', 'production', 'machine', 'robot', 'process')

    def build(self):
        self.path('hall',(4,40),(4,28),(16,16,12,12,True),(28,28,12,12,True),(28,32),(28,40),(20,40),(12,40),(4,40),closed=True)
        self.path('door',(12,40),(12,32),(20,32),(20,40));self.relate('connect','door','hall')
        self.path('annex',(28,32),(36,32),(44,32),(44,40),(28,40));self.relate('connect','annex','hall')
        self.path('chimney',(36,32),(36,8),(44,8),(44,32));self.relate('connect','chimney','annex')

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
