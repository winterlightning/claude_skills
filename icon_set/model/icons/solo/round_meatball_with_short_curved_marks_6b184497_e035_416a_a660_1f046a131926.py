"""Restored four short curved texture marks and evenly separated them from each other and the circular edge.
Symbol plan: Circular meatball with four curved texture strokes arranged rotationally around center. Lucide cookie informs sparse internal texture; restore reference arcs instead of dots.
Final reduction: Curves shortened to preserve spacing at 48 pixels.
References: Lucide cookie original and atomic-debug: sparse texture inside a circular outline.
Keyshape reason: Circular meatball.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6b184497-e035-416a-a660-1f046a131926'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/meatball_6b184497-e035-416a-a660-1f046a131926.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='round-meatball-with-short-curved-marks'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('round', 'meatball', 'with', 'short', 'curved', 'marks')
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
        circle('ball',24,24,20)
        for i,(a,b) in enumerate([((15,21),(19,17)),((27,15),(31,19)),((33,27),(29,31)),((21,33),(17,29))]):
         self.add_arc(f'texture-{i}',a,b,radius_x=7,sweep=True)
