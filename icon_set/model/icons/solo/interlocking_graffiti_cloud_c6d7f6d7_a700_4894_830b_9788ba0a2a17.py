"""Abstract interlocking rounded cloud; Lucide cloud informs broad smooth lobes. HRECT_L broad cloud envelope.
Redraw authorized 2026-09-22. Source interpretation follows visible composition.
Earlier draft, if any, is preserved. Shared parameters own repeated geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c6d7f6d7-a700-4894-830b-9788ba0a2a17'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_21/graffiti_c6d7f6d7-a700-4894-830b-9788ba0a2a17.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'interlocking-graffiti-cloud'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = "Uncategorized"
    aliases = ('Stylized Graffiti Cloud',)
    keywords = ('interlocking', 'graffiti', 'cloud')
    def build(self):
        def curve(n,start,*segments): self.add_bezier(n,start,*segments)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def join(*n): self.relate('connect',*n)
        curve('cloud',(12,24),((6,20),(5,8),(14,8)),((19,8),(20,11),(22,14)),((23,6),(32,6),(32,16)),((41,10),(44,18),(38,24)),((42,24),(44,25),(44,29)),((44,33),(40,34),(36,34)),((38,38),(35,40),(31,40)),((28,40),(26,38),(26,34)),((25,38),(23,40),(20,40)),((16,40),(14,38),(14,34)),((5,39),(4,34),(4,30)),((4,26),(8,24),(12,24)))
        curve('seam',(14,34),((23,32),(24,25),(20,21)))
        join('cloud','seam')
