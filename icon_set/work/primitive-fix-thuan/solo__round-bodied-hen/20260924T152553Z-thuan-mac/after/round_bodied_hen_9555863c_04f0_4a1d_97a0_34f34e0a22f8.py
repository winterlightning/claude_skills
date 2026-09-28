"""Rebuilt the hen with smooth head and belly arcs, a clear beak and tail, and two separate short feet.
Symbol plan: Smooth broad hen body with rounded head, beak, tail and two separate feet; Lucide bird informs flowing neck and body. Tiny comb seam omitted.
Final reduction: Tiny comb and inner wing seam omitted; fine toes reduced to short feet.
References: Lucide bird original and atomic-debug: smooth body and neck.
Keyshape reason: Horizontal bird silhouette.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='9555863c-04f0-4a1d-97a0-34f34e0a22f8'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__round-bodied-hen/20260924T152553Z-thuan-mac/reference/broiler_9555863c-04f0-4a1d-97a0-34f34e0a22f8.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='round-bodied-hen'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/reference"
    aliases=()
    keywords=('round', 'bodied', 'hen')
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
        path('hen',(4,12),[(12,20),(24,20),(24,16),((32,8),8,8,True),((40,16),8,8,True),(44,20),(40,24),((28,36),12,12,True),(20,36),((4,20),16,16,True),(4,12)],True)
        line('foot-left',(20,36),(20,40));line('foot-right',(28,36),(28,40));join('foot-left','hen');join('foot-right','hen')
