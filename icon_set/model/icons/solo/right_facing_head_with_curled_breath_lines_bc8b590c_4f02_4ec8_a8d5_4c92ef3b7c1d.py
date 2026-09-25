"""Rebuilt the skull and mouth as a coherent contour and restored two separated breath curls.
Symbol plan: Circular rear skull, continuous neck, rounded open mouth and two outward breath curls. Human user.svg informs skull flow; preserve attached anatomical neck.
Final reduction: Tiny facial details omitted; source blank face retained.
References: human_ref/user.svg: circular anatomy.
Keyshape reason: Head and breath fit a square composition; anatomical neck is continuous, no detached head gap applies.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bc8b590c-4f02-4ec8-a8d5-4c92ef3b7c1d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/spit_bc8b590c-4f02-4ec8-a8d5-4c92ef3b7c1d.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='right-facing-head-with-curled-breath-lines'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('right', 'facing', 'head', 'with', 'curled', 'breath', 'lines')
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
        path('head',(6,42),[(6,18),((18,6),12,12,True),((30,18),12,12,True),(30,20),(31,23),(24,23),((24,33),5,5,False),((22,39),6,6,True),(22,42)])
        path('breath-upper',(40,17),[((42,20),2,3,True),((40,23),2,3,True)])
        path('breath-lower',(36,34),[(39,34),((42,37),3,3,True),((39,40),3,3,True)])
