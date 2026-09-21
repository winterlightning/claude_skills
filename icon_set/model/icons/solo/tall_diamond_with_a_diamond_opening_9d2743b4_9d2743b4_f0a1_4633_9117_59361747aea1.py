'Tall Diamond with a Diamond Opening.\nSymbol plan: A tall pointed diamond encloses a much smaller matching diamond at its center. Both shapes share a vertical axis, leaving a broad uninterrupted border between their sloping edges.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Retain the source parts and arrangement.\nKeyshape VRECT_M: ink extremes (8, 2, 40, 46).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9d2743b4-f0a1-4633-9117-59361747aea1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/aov rov logo 3 game aov rov logo_9d2743b4-f0a1-4633-9117-59361747aea1.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'tall-diamond-with-a-diamond-opening-9d2743b4'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('diamond', 'rhombus', 'geometric', 'outline', 'opening', 'shape', 'mark')
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
        poly('outer',(24,4),(40,24),(24,44),(8,24),closed=True)
        poly('inner',(24,17),(29,24),(24,31),(19,24),closed=True)
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
