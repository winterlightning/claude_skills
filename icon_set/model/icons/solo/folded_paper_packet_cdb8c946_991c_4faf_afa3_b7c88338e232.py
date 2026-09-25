'Folded Paper Packet.\nSymbol plan: A tall paper packet leans slightly to the right with a broad blank front and a narrow folded side. Horizontal seams cross the top and bottom, and the lower right corner forms a small gusset.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: One lower side fold replaces the narrow gusset.\nKeyshape VRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cdb8c946-991c-4faf-afa3-b7c88338e232'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/packet_cdb8c946-991c-4faf-afa3-b7c88338e232.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'folded-paper-packet'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('paper', 'packet', 'bag', 'package', 'fold', 'gusset')
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry,sweep=s)
        def bez(n,a,*s): self.add_bezier(n,a,*s)
        def con(n,*p,closed=False):
            self.contours[:] = [c for c in self.contours if not set(c.members)&set(p)]
            self.add_contour(n,*p,closed=closed)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r);arc(n+'b',(x+r,y),(x-r,y),r)
            con(n,n+'a',n+'b',closed=True)
        def rect(n,x,y,w,h,r=0):
            if not r: poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True);return
            ps=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for j in range(8):
                if j%2: arc(n+str(j),ps[j],ps[(j+1)%8],r)
                else: line(n+str(j),ps[j],ps[(j+1)%8])
            con(n,*(n+str(j) for j in range(8)),closed=True)
        poly('packet',(14,4),(40,4),(36,44),(8,44),(14,4))
        line('top-seam',(13,12),(39,12));line('base-seam',(9,36),(37,36))
        line('side-fold',(26,44),(28,24))
        self.relate('connect','top-seam','packet');self.relate('connect','base-seam','packet');self.relate('connect','side-fold','packet')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
