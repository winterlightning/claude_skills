"""Rounded both scroll rolls, opened the lower curl, and restored a visible wavy center mark.
Symbol plan: Upright scroll with rounded rolled top and lower curl, one visible wave. Lucide scroll informs split shared boundaries and rolled-end construction.
Final reduction: Wave reduced to one broad cycle.
References: Lucide scroll original and atomic-debug: rolled ends and shared sheet boundaries.
Keyshape reason: Upright parchment.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3ba958e6-0fce-4357-b442-e59dc5f9ec6c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/parchment_3ba958e6-0fce-4357-b442-e59dc5f9ec6c.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='rolled-parchment-wavy-mark'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('rolled', 'parchment', 'wavy', 'mark')
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
        path('sheet',(12,4),[(30,4),((38,12),8,8,True),(38,34),(40,34),(40,38),((34,44),6,6,True),(18,44),((12,38),6,6,True),(12,16)])
        path('top-roll',(8,16),[(8,8),((12,4),4,4,True),((16,8),4,4,True),(16,16),(12,16),(8,16)],True);join('sheet','top-roll')
        path('lower-curl',(24,34),[(24,38),((30,44),6,6,False)]);join('lower-curl','sheet')
        line('lip',(24,34),(38,34));join('lip','sheet');join('lip','lower-curl')
        path('wave',(21,25),[((25,23),4,4,True),((29,25),4,4,False)])
