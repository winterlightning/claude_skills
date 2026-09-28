'Diagonal Glue Stick.\nSymbol plan: A glue stick tilts from lower left to upper right with a long rounded casing and a blank rectangular label. A seam separates the upper cap, while a rounded base projects below.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Omit the blank inset label; retain both cap and base seams.\nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a49a67dc-9de8-43c4-9895-a4590f891c0e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/paper glue 1_a49a67dc-9de8-43c4-9895-a4590f891c0e.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'diagonal-glue-stick'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "office"
    categories = ("office", "primitive", "primitives")
    aliases = ()
    keywords = ('glue', 'stick', 'adhesive', 'stationery', 'cap', 'label')
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
        line('left',(8,28),(28,8))
        bez('top-a',(28,8),((30,6),(32,6),(34,6)))
        arc('top-b',(34,6),(42,14),8)
        bez('top-c',(42,14),((42,16),(42,18),(40,20)))
        line('right',(40,20),(20,40))
        bez('base-a',(20,40),((18,42),(16,42),(14,42)))
        arc('base-b',(14,42),(6,34),8)
        bez('base-c',(6,34),((6,32),(6,30),(8,28)))
        con('glue','left','top-a','top-b','top-c','right','base-a','base-b','base-c',closed=True)
        line('cap-seam',(22,14),(34,26));line('base-seam',(14,22),(26,34))
        self.relate('connect','cap-seam','glue');self.relate('connect','base-seam','glue')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
