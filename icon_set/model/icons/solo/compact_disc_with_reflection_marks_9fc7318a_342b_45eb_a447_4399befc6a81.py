'Compact Disc with Reflection Marks.\nSymbol plan: A compact disc has a large circular perimeter around a smaller hub and center hole. Two short diagonal reflection marks sit on opposite sides of the inner ring.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: One center opening and two reflection dots preserve the diagonal arrangement.\nKeyshape CIRCLE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9fc7318a-342b-45eb-a447-4399befc6a81'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/compact disc_9fc7318a-342b-45eb-a447-4399befc6a81.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'compact-disc-with-reflection-marks'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('disc', 'cd', 'optical', 'media', 'round', 'hole', 'reflection')
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
        circle('disc',24,24,20);circle('hub',24,24,3)
        self.add_dot('reflection-a',(32,16));self.add_dot('reflection-b',(16,32))
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
