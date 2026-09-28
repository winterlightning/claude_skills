'Central Hub with Four Nodes.\nSymbol plan: A central circular hub connects by four diagonal spokes to matching outer nodes. The outer circles occupy the corners of a square arrangement around the plain central junction.\nConstruction: Lucide network: centered hub and symmetrically placed linked nodes.\nReduction: Retain the source parts and arrangement.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '516ab5ea-7a01-421d-ad0d-96fc5bb3ab45'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/coding apps website big data complexity_516ab5ea-7a01-421d-ad0d-96fc5bb3ab45.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'central-hub-with-four-nodes-516ab5ea'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('hub', 'network', 'nodes', 'connections', 'spokes', 'diagram', 'central')
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
        circle('hub',24,24,6)
        for i,(x,y,dx,dy) in enumerate(((10,10,1,1),(38,10,-1,1),(10,38,1,-1),(38,38,-1,-1))):
         circle('node'+str(i),x,y,4)
         line('spoke'+str(i),(x+dx*3,y+dy*3),(24-dx*4,24-dy*4))
         self.relate('connect','spoke'+str(i),'hub');self.relate('connect','spoke'+str(i),'node'+str(i))
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
