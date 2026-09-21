'Curved-Head Mining Pickaxe.\nSymbol plan: A pickaxe lies diagonally with a long rounded handle rising from the lower left. A broad curved metal head crosses the handle near the top, tapering into two sharp opposing points.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Omit small handle cap beyond the metal head.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e33dc96e-25d1-4d85-b9dd-23dd6dfe5491'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pickax_e33dc96e-25d1-4d85-b9dd-23dd6dfe5491.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'curved-head-mining-pickaxe'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('pickaxe', 'mining', 'tool', 'handle', 'metal', 'digging')
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
        bez('head-top',(10,6),((28,6),(42,20),(42,38)))
        poly('head-bottom',(42,38),(30,26),(22,18),(10,6))
        con('head','head-top','head-bottom-1','head-bottom-2','head-bottom-3',closed=True)
        line('handle-left',(22,18),(8,32))
        bez('heel',(8,32),((6,34),(6,35),(6,36)),((6,40),(8,42),(12,42)),((14,42),(15,41),(16,40)))
        line('handle-right',(16,40),(30,26))
        con('handle','handle-left','heel','handle-right')
        self.relate('connect','head','handle')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
