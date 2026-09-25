# Final reduction: Recompose the capsule upright and use two dots rather than small inclusion rings; retain six projections.
'Diagonal Bacterium with Two Inner Circles.\nSymbol plan: A rounded capsule-shaped bacterium tilts from lower left to upper right. Short straight projections radiate from its edge, and two small circular inclusions lie along its central length.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Upright capsule composition opens space for the two inclusions; six projections retain cell identity.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'df4d94f3-62a3-40bb-bee9-f07c0c7fdb90'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/bacterium_df4d94f3-62a3-40bb-bee9-f07c0c7fdb90.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'upright-bacterium-with-two-inclusions'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('bacterium', 'cell', 'microbe', 'capsule', 'projections', 'biology', 'circles')
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
        rect('cell',14,6,20,36,10)
        self.add_dot('inclusion-a',(24,17));self.add_dot('inclusion-b',(24,31))
        for i,y in enumerate((14,24,34)):
         line('left'+str(i),(6,y),(14,y));line('right'+str(i),(34,y),(42,y))
         self.relate('connect','cell','left'+str(i));self.relate('connect','cell','right'+str(i))
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
