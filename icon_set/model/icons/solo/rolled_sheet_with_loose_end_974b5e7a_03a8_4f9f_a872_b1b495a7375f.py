"""Rebuilt the front as a continuous spiral, with tangent barrel ends and a clean attached flap.
Symbol plan: Horizontal cylinder with open spiral front and a loose sheet extending to lower right; circle and cylinder use shared tangent extrema. Lucide cylinder informs barrel.
Final reduction: No essential parts omitted.
References: Lucide cylinder original and atomic-debug: tangent barrel and matching end curves.
Keyshape reason: Wide horizontal rolled material.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '974b5e7a-03a8-4f9f-a872-b1b495a7375f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/roll_974b5e7a-03a8-4f9f-a872-b1b495a7375f.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='rolled-sheet-with-loose-end'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('rolled', 'sheet', 'with', 'loose', 'end')
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
        path('spiral',(17,23),[((13,19),4,4,True),((19,13),6,6,True),((27,21),8,8,True),((16,32),11,11,True),((4,20),12,12,True),((16,8),12,12,True)])
        path('barrel',(16,8),[(32,8),((44,20),12,12,True),((32,32),12,12,True),(16,32)]);join('spiral','barrel')
        poly('flap',(16,32),(24,40),(44,40),(32,32));join('flap','barrel');join('flap','spiral')
