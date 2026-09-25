"""Rebuilt mirrored signal arcs with exact extrema and kept the dish divider and splayed legs separated.
Symbol plan: Circular antenna with horizontal divider, two splayed supports, balanced curved signal arcs. Lucide radio-tower informs paired arcs and splayed support.
Final reduction: No essential parts omitted.
References: Lucide radio-tower original and atomic-debug: paired arcs and support.
Keyshape reason: Symmetric signal and antenna composition.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e1c164fb-4742-4765-a109-02303168257e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/amazon web service global network antennas_e1c164fb-4742-4765-a109-02303168257e.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='round-antenna-on-splayed-legs'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('round', 'antenna', 'on', 'splayed', 'legs')
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
        circle('dish',24,22,9)
        poly('divider',(15,22),(24,22),(33,22));join('divider','dish')
        poly('legs',(16,42),(24,31),(32,42));join('legs','dish')
        path('signal-left',(12,6),[((6,22),6,16,False),((10,32),4,10,False)])
        path('signal-right',(36,6),[((42,22),6,16,True),((38,32),4,10,True)])
