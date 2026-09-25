"""Rounded the rhino back and muzzle, rebuilt the horn and ear, and regularized the leg openings.
Symbol plan: Heavy rhino silhouette with rounded back, two broad legs, low muzzle and rising horn. No useful Lucide match. Inner leg seams omitted.
Final reduction: Inner leg seams omitted; two primary legs retained.
References: No useful exact Lucide match.
Keyshape reason: Wide animal silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '94f0b2d9-0d53-4bde-940f-e2260212a757'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/rhinoceros_94f0b2d9-0d53-4bde-940f-e2260212a757.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='rhinoceros-facing-right'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('rhinoceros', 'facing', 'right')
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
        path('rhino',(4,40),[(4,26),((18,12),14,14,True),(26,12),(31,8),(32,18),(36,22),(44,14),(44,26),((38,32),6,6,True),(32,30),(32,40),(24,40),(24,30),(12,30),(12,40),(4,40)],True)
