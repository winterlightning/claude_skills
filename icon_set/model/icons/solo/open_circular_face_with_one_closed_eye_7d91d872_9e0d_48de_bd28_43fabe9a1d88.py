'Open Circular Face with One Closed Eye.\nSymbol plan: An almost circular face outline has a wide gap at its lower right and a single small curved closed eye above center. No mouth or second eye is visible in the reference.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Preserve the open lower-right outline and single closed eye; do not invent a mouth.\nKeyshape CIRCLE: ink extremes (2, 2, 46, 46).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7d91d872-9e0d-48de-bd28-43fabe9a1d88'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/smiley kiss heart_7d91d872-9e0d-48de-bd28-43fabe9a1d88.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'open-circular-face-with-one-closed-eye'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('face', 'eye', 'expression', 'circle', 'smiley', 'wink')
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
        arc('top',(4,24),(44,24),20)
        arc('left-bottom',(24,44),(4,24),20)
        con('face','left-bottom','top')
        arc('eye',(20,20),(28,20),4,3)
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
