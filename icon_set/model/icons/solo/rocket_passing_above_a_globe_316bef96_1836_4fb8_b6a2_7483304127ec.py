"""Rebuilt the diagonal rocket, separated its exhaust, and restored globe grid detail below it.
Symbol plan: Diagonal pointed rocket with two fins above a curved globe, short exhaust and continent seam. Lucide rocket informs coherent pointed fuselage.
Final reduction: Fins reduced to projecting strokes; one exhaust retained; geography represented by latitude and meridian.
References: Lucide rocket original and atomic-debug: pointed fuselage and fins.
Keyshape reason: Diagonal rocket and lower globe occupy a square.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '316bef96-1836-4fb8-b6a2-7483304127ec'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/rocket attack global_316bef96-1836-4fb8-b6a2-7483304127ec.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='rocket-passing-above-a-globe'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('rocket', 'passing', 'above', 'a', 'globe')
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
        path('rocket',(16,18),[(28,8),(42,6),(40,12),(30,22),(26,25),(16,18)],True)
        line('fin-left',(16,18),(6,18));join('fin-left','rocket')
        line('fin-right',(30,22),(34,24));join('fin-right','rocket')
        line('exhaust',(6,34),(8,30))
        path('globe',(16,29),[((17,34),13,13,False),((29,42),13,13,False),((41,34),13,13,False),((42,29),13,13,False)])
        poly('latitude',(17,34),(29,34),(41,34));join('latitude','globe')
        line('meridian',(29,34),(29,42));join('meridian','globe');join('meridian','latitude')
