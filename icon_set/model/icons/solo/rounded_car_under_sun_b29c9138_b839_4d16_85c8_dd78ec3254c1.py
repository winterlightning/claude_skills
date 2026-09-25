"""Restored the complete car body around equal wheels and preserved the separate sun.
Symbol plan: Complete rounded side car with two wheels below sun; Lucide car informs wheel breaks and roof slope. Tiny window seam and fine sun rays omitted.
Final reduction: Fine sun rays and interior window seam omitted for spacing; sun remains a small circle.
References: Lucide car original and atomic-debug: side silhouette and wheel breaks.
Keyshape reason: Car and upper sun form a square scene.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b29c9138-b839-4d16-85c8-dd78ec3254c1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/car sun_b29c9138-b839-4d16-85c8-dd78ec3254c1.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='rounded-car-under-sun'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('rounded', 'car', 'under', 'sun')
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
        path('body',(9,37),[(6,37),(6,30),((12,24),6,6,True),(18,18),(24,18),(32,24),(36,24),((42,30),6,6,True),(42,37),(39,37)])
        circle('rear-wheel',14,37,5);circle('front-wheel',34,37,5)
        line('sill',(19,37),(29,37));join('sill','rear-wheel');join('sill','front-wheel');join('body','rear-wheel');join('body','front-wheel')
        circle('sun',37,9,3)
