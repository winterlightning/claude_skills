"""Restored a balanced wheel cross and splayed support beside a smooth coaster curve.
Symbol plan: Ferris wheel with radial spokes and splayed supports beside a smooth descending coaster track. Lucide ferris-wheel informs radial wheel.
Final reduction: Wheel spoke count reduced to four; small hub and repeated coaster supports omitted.
References: Lucide ferris-wheel original and atomic-debug: radial wheel and support.
Keyshape reason: Square two-subject scene.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7fa6c31c-7745-4025-99b4-16a7e22d9594'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/theme park_7fa6c31c-7745-4025-99b4-16a7e22d9594.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='roller-coaster-ferris-wheel'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('roller', 'coaster', 'ferris', 'wheel')
    def build(self):

        def path(n,start,steps,closed=False):
            p=start; members=[]
            for i,step in enumerate(steps):
                m=f"{n}-{i}"
                if len(step)==2:
                    self.add_line(m,p,step);p=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(m,p,end,radius_x=rx,radius_y=ry,sweep=sweep);p=end
                members.append(m)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[((x,y-r),r,r,True),((x+r,y),r,r,True),((x,y+r),r,r,True),((x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        circle('wheel',30,18,12)
        poly('spoke-v',(30,6),(30,18),(30,30));poly('spoke-h',(18,18),(30,18),(42,18))
        join('spoke-v','wheel');join('spoke-h','wheel');join('spoke-v','spoke-h')
        poly('support',(24,42),(30,30),(36,42));join('support','wheel');join('support','spoke-v')
        path('track',(6,42),[(6,30),((14,30),4,4,True),((26,42),12,12,False),(42,42)])
        join('track','support')
