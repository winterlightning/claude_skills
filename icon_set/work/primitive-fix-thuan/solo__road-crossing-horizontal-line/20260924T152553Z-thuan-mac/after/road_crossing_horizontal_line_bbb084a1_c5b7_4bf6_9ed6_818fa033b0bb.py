"""Removed the bends in the road edges and derived the taper symmetrically around the crossing.
Symbol plan: Mirrored straight tapering road sides, a full width overpass and two center dashes; remove kinks in rejected road edges. No useful exact Lucide match.
Final reduction: Top and bottom framing lines omitted as in the prior highway reduction.
References: No useful exact Lucide match.
Keyshape reason: Wide crossing with vertical taper.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='bbb084a1-c5b7-4bf6-9ed6-818fa033b0bb'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__road-crossing-horizontal-line/20260924T152553Z-thuan-mac/reference/highway_bbb084a1-c5b7-4bf6-9ed6-818fa033b0bb.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='road-crossing-horizontal-line'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/reference"
    aliases=()
    keywords=('road', 'crossing', 'horizontal', 'line')
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
        poly('left',(8,40),(12,24),(16,8))
        poly('right',(40,40),(36,24),(32,8))
        poly('bridge',(4,24),(12,24),(36,24),(44,24))
        join('bridge','left');join('bridge','right')
        line('dash-top',(24,8),(24,16));line('dash-bottom',(24,32),(24,40))
