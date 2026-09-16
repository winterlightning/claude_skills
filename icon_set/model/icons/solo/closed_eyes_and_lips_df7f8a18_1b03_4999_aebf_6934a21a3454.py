"""Closed Eyes and Lips.

Symbol plan: Two mirrored closed eyes sit above full lips. One lash per eye and a shallow upper-lip dip replace fine eyelashes and a crowded mouth seam.
Lucide: eye-closed; original and atomic-debug geometry inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'df7f8a18-1b03-4999-aebf-6934a21a3454'
SOURCE_PATH = 'pictographic-primitives/beauty/dating makeup_df7f8a18-1b03-4999-aebf-6934a21a3454.svg'
AUTHOR = 'gpt-6'


class ClosedEyesAndLips(Solo48):
    icon_id = 'closed-eyes-and-lips'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    aliases = ()
    keywords = ('closed eyes', 'face', 'eyes', 'lips', 'expression', 'beauty', 'features', 'mouth', 'portrait')

    def build(self):
        axis=24
        for n,x in [('left',12),('right',36)]:
            self.path(n+'-lid',(x-8,8),(x,12,8,4,False),(x+8,8,8,4,False))
            self.add_line(n+'-lash',(x,12),(x,16));self.relate('connect',n+'-lash',n+'-lid')
        self.path('lips',(10,30),(18,26,14,30,16,26),(24,28,20,26,22,28),(30,26,26,28,28,26),(38,30,32,26,34,30),(24,40,34,36,30,40),(10,30,18,40,14,36),closed=True)

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
