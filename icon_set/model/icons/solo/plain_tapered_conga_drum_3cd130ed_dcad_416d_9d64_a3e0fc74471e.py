'Plain Tapered Conga Drum.\nSymbol plan: A tall conga drum has an oval playing surface and a broad band below its rim. Its body bulges slightly through the middle before tapering toward a rounded base.\nConstruction: Lucide drum: elliptical top with coherent curved body sides.\nReduction: Omit the secondary narrow rim band.\nKeyshape VRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3cd130ed-dcad-416d-9d64-a3e0fc74471e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/conga_3cd130ed-dcad-416d-9d64-a3e0fc74471e.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'plain-tapered-conga-drum'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('conga', 'drum', 'percussion', 'music', 'instrument', 'rim', 'body')
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
        arc('rim-top',(8,10),(40,10),16,6);arc('rim-bottom',(40,10),(8,10),16,6);con('rim','rim-top','rim-bottom',closed=True)
        bez('left',(8,10),((8,22),(10,36),(16,44)))
        line('base',(16,44),(32,44))
        bez('right',(32,44),((38,36),(40,22),(40,10)))
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
