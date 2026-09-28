"""Person above Organization Branches.

Symbol plan: A detached circular head over a domed bust and three shared branch nodes. The small boxes become round terminals; shoulders follow human_ref/user.svg with an exact 4-unit ink gap.
Lucide: network; original and atomic-debug geometry inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '78cdcd12-a8af-52c7-89a0-c0f93928d644'
SOURCE_PATH = 'pictographic-primitives/business/customer relationship management categorization list_78cdcd12-a8af-52c7-89a0-c0f93928d644.svg'
AUTHOR = 'gpt-6'


class PersonAboveOrganizationBranches(Solo48):
    icon_id = 'person-above-organization-branches'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('hierarchy', 'network', 'organization', 'connection', 'structure', 'branch', 'diagram', 'relationship')

    def build(self):
        axis=24
        self.circle('head',axis,12,4)
        self.path('shoulders',(16,32),(axis,24,8,8,True),(32,32,8,8,True))
        self.path('branch',(6,32),(16,32),(axis,32),(32,32),(42,32));self.relate('connect','branch','shoulders')
        for index,x in enumerate((6,axis,42)):
            n=f'node-{index}'
            self.circle(n,x,38,2)
            self.add_line(n+'-stem',(x,32),(x,36))
            self.relate('connect',n+'-stem',n);self.relate('connect',n+'-stem','branch')

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
