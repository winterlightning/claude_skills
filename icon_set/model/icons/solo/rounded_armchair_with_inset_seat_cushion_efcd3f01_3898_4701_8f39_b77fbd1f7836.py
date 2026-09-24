"""Rounded the chair back and arms, rebuilt the continuous seat/base contour, and restored two feet.
Symbol plan: Rounded armchair with thick arms, inset seat and two feet; Lucide armchair informs one coherent lower silhouette and tangent corners.
Final reduction: Cushion uses one shared seat edge instead of a doubled narrow seam.
References: Lucide armchair original and atomic-debug: continuous arms and lower silhouette.
Keyshape reason: Square frontal chair with mirrored parts.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'efcd3f01-3898-4701-8f39-b77fbd1f7836'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/divan_efcd3f01-3898-4701-8f39-b77fbd1f7836.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='rounded-armchair-with-inset-seat-cushion'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/reference"
    aliases=()
    keywords=('rounded', 'armchair', 'with', 'inset', 'seat', 'cushion')
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
        path('back',(14,22),[(14,12),((20,6),6,6,True),(28,6),((34,12),6,6,True),(34,22)])
        path('chair',(14,28),[(14,22),((6,22),4,4,False),(6,34),((10,38),4,4,False),(38,38),((42,34),4,4,False),(42,22),((34,22),4,4,False),(34,28),(14,28)],True);join('back','chair')
        line('foot-left',(10,38),(10,42));line('foot-right',(38,38),(38,42));join('foot-left','chair');join('foot-right','chair')
