"""Speaking profile with complete empty speech balloon at upper right. Source profile direction retained; Lucide message-square informs tail. HRECT_L wide composition.
Redraw authorized 2026-09-22. Source interpretation follows visible composition.
Earlier draft, if any, is preserved. Shared parameters own repeated geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd3d86e97-b873-48ff-bd6b-fc4456184a6e'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_25/linguist_d3d86e97-b873-48ff-bd6b-fc4456184a6e.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'speaking-profile-with-empty-bubble'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = "Uncategorized"
    aliases = ('Speaking Person with Speech Bubble',)
    keywords = ('speaking', 'profile', 'with', 'empty', 'bubble')
    def build(self):
        def curve(n,start,*segments): self.add_bezier(n,start,*segments)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def join(*n): self.relate('connect',*n)
        curve('skull',(12,40),((12,33),(4,28),(4,18)),((4,8),(18,8),(22,8)))
        poly('face',(22,8),(22,20),(26,26),(22,28),(22,34),(18,34),(18,40))
        join('skull','face')
        poly('speech',(34,24),(34,10),(44,10),(44,24),(40,24),(34,30),(34,24),closed=True)
