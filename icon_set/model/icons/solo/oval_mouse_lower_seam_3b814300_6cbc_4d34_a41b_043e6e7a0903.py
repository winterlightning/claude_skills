'Oval Mouse with Lower Seam.\nSymbol plan: An upright computer mouse has a long oval body with rounded top and bottom ends. A single straight seam rises from the lower edge toward the center, leaving the upper half blank.\nConstruction: Lucide mouse: symmetric capsule contour, with reference-specific lower seam.\nReduction: Retain the source parts and arrangement.\nKeyshape VRECT_M: ink extremes (8, 2, 40, 46).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3b814300-6cbc-4d34-a41b-043e6e7a0903'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/pod_3b814300-6cbc-4d34-a41b-043e6e7a0903.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'oval-mouse-lower-seam'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('mouse', 'computer', 'device', 'oval', 'input', 'desktop')
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
        rect('mouse',10,4,28,40,14)
        line('seam',(24,44),(24,24));self.relate('connect','mouse','seam')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
