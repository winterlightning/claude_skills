'Paneled Underwear Briefs.\nSymbol plan: A pair of briefs faces forward beneath a broad waistband. Curved seams descend toward a narrow central crotch, framed by two high rounded leg openings at the sides.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Omit redundant paneled seams to keep generous leg openings.\nKeyshape HRECT_L: ink extremes (2, 6, 46, 42).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9b44cc61-6847-480b-a308-1c8b5598d3b7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/briefs_9b44cc61-6847-480b-a308-1c8b5598d3b7.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'paneled-underwear-briefs'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('briefs', 'underwear', 'clothing', 'waistband', 'seams', 'garment', 'bottoms')
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
        poly('top',(4,24),(4,8),(44,8),(44,24))
        bez('right-leg',(44,24),((36,24),(32,30),(30,40)))
        line('crotch',(30,40),(18,40))
        bez('left-leg',(18,40),((16,30),(12,24),(4,24)))
        con('briefs','top-1','top-2','top-3','right-leg','crotch','left-leg',closed=True)
        line('waist',(4,16),(44,16));self.relate('connect','waist','briefs')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
