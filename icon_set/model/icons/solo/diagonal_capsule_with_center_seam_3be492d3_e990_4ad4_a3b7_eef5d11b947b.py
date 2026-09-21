'Diagonal Capsule with Center Seam.\nSymbol plan: An elongated capsule lies diagonally from lower left to upper right with matching rounded ends. A straight crosswise seam divides the body into two plain halves near the middle.\nConstruction: Lucide pill: two equal semicircular ends and a crosswise seam.\nReduction: Retain the source parts and arrangement.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3be492d3-e990-4ad4-a3b7-eef5d11b947b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/emery_3be492d3-e990-4ad4-a3b7-eef5d11b947b.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'diagonal-capsule-with-center-seam'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('capsule', 'pill', 'medicine', 'seam', 'pharmacy', 'tablet', 'health')
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
        line('left',(8,26),(24,10));arc('tip',(24,10),(40,22),10)
        line('right',(40,22),(24,38));arc('heel',(24,38),(8,26),10)
        con('capsule','left','tip','right','heel',closed=True)
        line('seam',(16,18),(32,30));self.relate('connect','seam','capsule')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
