# Final repair: Compact cloud to exact square envelope; lower middle roof for spacing.
'Three Buildings beneath Cloud\nPlan: Three stepped buildings, pitched middle roof and upper-left cloud.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Drop windows to keep three buildings and cloud legible.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0291328f-6b9e-4cc3-80d5-84c234b92ad3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-buildings-beneath-cloud/20260927T173930Z-thuan-mac-1/reference/building cloudy_0291328f-6b9e-4cc3-80d5-84c234b92ad3.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'three-buildings-beneath-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('three', 'buildings', 'beneath', 'cloud')

    def build(self):

        def path(name, start, steps, closed=False):
            members, point = [], start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[((x+rx,y),rx,ry,True),((x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r):
            ellipse(name,x,y,r,r)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)

        self.add_polyline('skyline',(6,42),(6,34),(18,34),(18,30),(26,24),(34,30),(34,6),(42,6),(42,42),(6,42),closed=True)
        self.add_line('join-low',(18,34),(18,42));self.add_line('join-high',(34,30),(34,42))
        self.relate('connect','join-low','skyline');self.relate('connect','join-high','skyline')
        self.add_bezier('cloud-left',(10,16),((7,16),(7,10),(12,10)))
        self.add_bezier('cloud-top',(12,10),((13,5),(19,5),(20,10)))
        self.add_bezier('cloud-right',(20,10),((25,10),(25,16),(20,16)))
        self.add_line('cloud-base',(20,16),(10,16))
        self.add_contour('cloud','cloud-left','cloud-top','cloud-right','cloud-base',closed=True)
