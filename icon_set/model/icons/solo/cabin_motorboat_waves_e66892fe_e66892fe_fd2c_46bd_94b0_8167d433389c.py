"Cabin Motorboat on Waves.\nSymbol plan: A motorboat faces right with a raised cabin, sloping windscreen, and curved pointed bow. Two wavy water lines pass beneath the hull, with the upper wave partly overlapping the boat's lower edge.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: One clear water wave replaces two crowded overlapping waves.\nKeyshape HRECT_L: ink extremes (2, 6, 46, 42)."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e66892fe-fd2c-46bd-94b0-8167d433389c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/powerboat_e66892fe-fd2c-46bd-94b0-8167d433389c.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'cabin-motorboat-waves-e66892fe'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('motorboat', 'boat', 'waves', 'water', 'cabin', 'transport')
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
        poly('hull',(4,20),(44,20),(36,30),(12,30),(4,20))
        poly('cabin',(14,20),(14,8),(28,8),(36,20))
        bez('wave',(4,40),((12,40),(12,38),(20,38)),((28,38),(28,40),(36,40)),((40,40),(42,38),(44,38)))
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
