from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='44d3d80b-4240-42cf-9ac4-2237f7c5d0aa'
SOURCE_PATH='pictographic-primitives/travel/plane 1_44d3d80b-4240-42cf-9ac4-2237f7c5d0aa.svg'
AUTHOR="gpt-6"
PARENT_RESULT='icon_set/work/primitive-make-ray/44d3d80b-4240-42cf-9ac4-2237f7c5d0aa/20260925-fresh-c5fdae55/result.json'
class Drawing(Solo48):
    icon_id='plane-1-solo'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "travel"
    categories = ("travel", "primitives")
    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,l,t,r,b,rad=3):
        points=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        for i,a in enumerate(points):
            z=points[(i+1)%8]
            if i%2:self.add_arc(n+str(i),a,z,radius_x=rad)
            else:self.add_line(n+str(i),a,z)
        self.add_contour(n,*(n+str(i) for i in range(8)),closed=True)
    def build(self):
        # Arrowheads point along the terminal tangent: left down, right up.
        self.add_bezier('upper-right',(38,12),((35,7),(30,4),(24,4)))
        self.add_bezier('upper-left',(24,4),((14,4),(8,14),(8,28)))
        self.add_contour('upper-orbit','upper-right','upper-left')
        self.add_polyline('arrow-left',(4,24),(8,28),(12,24));self.relate('connect','upper-orbit','arrow-left')
        self.add_bezier('lower-left',(10,36),((13,41),(18,44),(24,44)))
        self.add_bezier('lower-right',(24,44),((34,44),(40,34),(40,20)))
        self.add_contour('lower-orbit','lower-left','lower-right')
        self.add_polyline('arrow-right',(36,24),(40,20),(44,24));self.relate('connect','lower-orbit','arrow-right')
        self.add_bezier('plane-tail',(18,30),((20,32),(21,32),(24,29)))
        self.add_polyline('plane-body',(24,29),(26,26),(28,22));self.relate('connect','plane-tail','plane-body')
        self.add_line('plane-wing',(18,17),(26,26));self.relate('connect','plane-body','plane-wing')

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': 'ffb6f8f189e819c765ed78257cd0bb57d5be66884acfbe493d4a93d71ed6d897', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': '44d3d80b-4240-42cf-9ac4-2237f7c5d0aa'}
