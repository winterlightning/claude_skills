'Eight Tooth Gear with Circular Hub.\nSymbol plan: A gear has eight broad teeth spaced around a round body. Two centered circles define a raised hub and small axle opening, with the teeth arranged evenly around the outer edge.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Reduce nested hub rings to one axle opening.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd53b2910-ce8c-4ea5-adbc-c7f5b0619e60'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/machinery_d53b2910-ce8c-4ea5-adbc-c7f5b0619e60.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'eight-tooth-gear-with-circular-hub'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('gear', 'cog', 'teeth', 'hub', 'axle', 'machine', 'mechanical')
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
        pts=[(20, 6), (28, 6), (29, 13), (34, 8), (40, 14), (35, 19), (42, 20), (42, 28), (35, 29), (40, 34), (34, 40), (29, 35), (28, 42), (20, 42), (19, 35), (14, 40), (8, 34), (13, 29), (6, 28), (6, 20), (13, 19), (8, 14), (14, 8), (19, 13)]
        poly('gear',*pts,closed=True)
        circle('hub',24,24,3)
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
