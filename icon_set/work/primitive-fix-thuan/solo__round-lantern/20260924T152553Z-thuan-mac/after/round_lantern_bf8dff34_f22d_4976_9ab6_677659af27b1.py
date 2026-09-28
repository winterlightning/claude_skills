"""Integrated the handle into a continuous lantern outline and rebuilt its ribs and pedestal at exact nodes.
Symbol plan: Circular lantern globe divided by centered ribs; arched top handle and separate base. Circular joins split at exact nodes. No useful Lucide lamp match for this globe lantern.
Final reduction: Separate upper cap band omitted; handle base retained.
References: No useful Lucide lamp match for this round lantern.
Keyshape reason: Upright handled globe and pedestal.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='bf8dff34-f22d-4976-9ab6-677659af27b1'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__round-lantern/20260924T152553Z-thuan-mac/reference/lamp 1_bf8dff34-f22d-4976-9ab6-677659af27b1.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='round-lantern'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/reference"
    aliases=()
    keywords=('round', 'lantern')
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
        path('outline',(16,16),[(16,12),((24,4),8,8,True),((32,12),8,8,True),(32,16),((40,28),8,12,True),((32,40),8,12,True),(32,44),(24,44),(16,44),(16,40),((8,28),8,12,True),((16,16),8,12,True)],True)
        poly('handle-base',(16,16),(24,16),(32,16));join('handle-base','outline')
        poly('vertical',(24,16),(24,28),(24,44));poly('horizontal',(8,28),(24,28),(40,28));join('vertical','outline');join('horizontal','outline');join('vertical','horizontal');join('vertical','handle-base')
