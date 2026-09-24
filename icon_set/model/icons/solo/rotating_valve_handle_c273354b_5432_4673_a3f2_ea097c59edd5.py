"""Rebuilt the valve handle with equal end radii and separated the opposed rotation arrows from its base.
Symbol plan: Centered horizontal valve handle and stem above a broad base, flanked by opposite rotation arrows. Lucide rotate-cw informs curved directional arrows.
Final reduction: Base represented by a broad foot; fine base enclosure omitted.
References: Lucide rotate-cw original and atomic-debug: curved arrows and corner arrowheads.
Keyshape reason: Opposed arrows frame the valve in a square.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c273354b-5432-4673-a3f2-ea097c59edd5'
SOURCE_PATH = 'pictographic-primitives/construction/valve_c273354b-5432-4673-a3f2-ea097c59edd5.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='rotating-valve-handle'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="construction"
    aliases=()
    keywords=('rotating', 'valve', 'handle')
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
        path('handle',(19,14),[(29,14),((29,22),4,4,True),(24,22),(19,22),((19,14),4,4,True)],True)
        line('stem',(24,22),(24,42));join('stem','handle')
        poly('base',(14,42),(24,42),(34,42));join('base','stem')
        path('left-arrow',(12,6),[((6,18),15,15,False),(6,30),(12,30)])
        poly('left-head',(6,22),(6,30),(14,30));join('left-head','left-arrow')
        path('right-arrow',(36,34),[((42,22),15,15,False),(42,6),(34,6)])
        poly('right-head',(34,6),(42,6),(42,14));join('right-head','right-arrow')
