"""Rebuilt a rounded caravan shell, restored the wheel size and separated the window from the doorway.
Symbol plan: Rounded caravan with upright doorway, window opening, one wheel and tow bar. Lucide caravan informs continuous shell broken at the wheel.
Final reduction: Small window represented by one clear horizontal mark.
References: Lucide caravan original and atomic-debug: shell broken at the wheel.
Keyshape reason: Wide caravan with tow bar.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'acc99c2a-b641-4443-9ca0-dcf2ffd052d3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/caravan_acc99c2a-b641-4443-9ca0-dcf2ffd052d3.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='rounded-camping-caravan'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('rounded', 'camping', 'caravan')
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
        path('shell',(11,35),[(4,35),(4,20),((16,8),12,12,True),(28,8),((40,20),12,12,True),(40,35),(28,35),(21,35)])
        circle('wheel',16,35,5);join('shell','wheel')
        poly('door',(28,35),(28,20),(40,20));join('door','shell')
        line('window',(13,19),(19,19))
        line('tow',(40,35),(44,35));join('tow','shell')
