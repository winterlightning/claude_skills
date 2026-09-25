"""Open drop interrupted by lower-right ring, retaining both concentric boundaries. Lucide droplet contributes smooth tapered side. HRECT_L bounds; no invented forensic symbol.
Redraw authorized 2026-09-22. Source interpretation follows visible composition.
Earlier draft, if any, is preserved. Shared parameters own repeated geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2f1ae9d4-7c42-400d-8760-d69f1f5f0abd'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_26/luminal evidence pinger print blood_2f1ae9d4-7c42-400d-8760-d69f1f5f0abd.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'blood-drop-with-evidence-ring'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = "primitives-generate"
    aliases = ('Blood Drop Target',)
    keywords = ('blood', 'drop', 'with', 'evidence', 'ring')
    def build(self):
        def curve(n,start,*segments): self.add_bezier(n,start,*segments)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def join(*n): self.relate('connect',*n)
        curve('drop',(20,14),((20,13),(18,10),(16,8)),((10,15),(4,22),(4,28)),((4,36),(8,40),(14,40)))
        circle('ring-outer',33,29,11)
        circle('ring-inner',33,29,2)
