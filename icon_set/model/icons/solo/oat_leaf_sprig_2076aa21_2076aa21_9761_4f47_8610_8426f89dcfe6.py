'Oat Leaf Sprig.\nSymbol plan: A slender upright stem carries four long pointed leaves alternating to either side and at the top. Each leaf has a broad curved body tapering into a sharp tip without interior veins.\nConstruction: Lucide sprout: pointed leaves built from mirrored curved sides.\nReduction: Retain the source parts and arrangement.\nKeyshape VRECT_L: ink extremes (6, 2, 42, 46).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2076aa21-9761-4f47-8610-8426f89dcfe6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/oats_2076aa21-9761-4f47-8610-8426f89dcfe6.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'oat-leaf-sprig-2076aa21'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('oat', 'plant', 'leaves', 'sprig', 'botanical', 'stem')
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
        line('stem-top',(24,4),(24,16));line('stem-middle',(24,16),(24,36));line('stem-base',(24,36),(24,44))
        for i,(y,side) in enumerate(((4,1),(4,-1),(24,1),(24,-1))):
         x=24+side*16
         bez('leaf'+str(i),(24,y+12),((x,y+12),(x,y+4),(x,y)),((x-side*8,y),(24,y+6),(24,y+12)))
         self.relate('connect','leaf'+str(i),'stem-top' if y==4 else 'stem-middle')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
