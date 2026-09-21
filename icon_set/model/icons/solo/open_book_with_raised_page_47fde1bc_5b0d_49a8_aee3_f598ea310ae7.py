'Open Book with Raised Page.\nSymbol plan: An open book has curved pages spreading from a central vertical spine. A raised page on the right overlaps another page behind it, creating a stepped outer edge.\nConstruction: Lucide book-open: mirrored flowing page contours and central spine, with raised right page.\nReduction: \nKeyshape HRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '47fde1bc-5b0d-49a8-aee3-f598ea310ae7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/book flip page_47fde1bc-5b0d-49a8-aee3-f598ea310ae7.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'open-book-with-raised-page'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('book', 'pages', 'open', 'reading', 'literature', 'spine', 'paper')
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
        bez('page-left-top',(4,8),((14,8),(20,12),(24,16)))
        line('spine',(24,16),(24,40))
        bez('page-left-bottom',(24,40),((18,34),(10,34),(4,34)))
        line('left',(4,34),(4,8))
        bez('page-right-top',(24,16),((28,10),(32,8),(36,8)))
        line('page-edge',(36,8),(36,30))
        bez('right-bottom',(36,30),((30,30),(26,36),(24,40)))
        poly('back',(36,16),(44,16),(44,38),(24,40))
        self.relate('connect','back','page-edge')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
