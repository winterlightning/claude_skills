"""Rebuilt the flask shoulders and bulb using coherent arcs and exact neck/lip attachments.
Symbol plan: Round flask with straight neck, distinct rolled lip and exact tangent circular bulb. Lucide flask-round informs circular bulb and upright neck. No liquid line because reference is empty.
Final reduction: Rolled lip reduced to one broad rim; empty flask retained.
References: Lucide flask-round original and atomic-debug: neck over round bulb.
Keyshape reason: Upright flask silhouette.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='db5d0816-6bfc-489d-95c5-5623b4efb1c5'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__round-bottom-flask-solo/20260924T152553Z-thuan-mac/reference/beaker_db5d0816-6bfc-489d-95c5-5623b4efb1c5.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='round-bottom-flask-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/reference"
    aliases=()
    keywords=('round', 'bottom', 'flask', 'solo')
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
        path('bulb',(18,16),[(18,4),(30,4),(30,16),((40,30),16,16,True),((24,44),16,14,True),((8,30),16,14,True),((18,16),16,16,True)],True)
        line('lip-left',(14,4),(18,4));line('lip-right',(30,4),(34,4));join('lip-left','bulb');join('lip-right','bulb')
