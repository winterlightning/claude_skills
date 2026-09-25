'Open Sack with Sugar Mound.\nSymbol plan: A rounded sack has a thick rolled rim across its open top. A pointed mound of sugar rises above the opening, while the bag widens toward its curved base.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: \nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9b5a459d-7ebe-4532-aa9e-808c5c2d51de'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/carbohydrate sugar bag_9b5a459d-7ebe-4532-aa9e-808c5c2d51de.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'open-sack-with-sugar-mound'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('sack', 'sugar', 'bag', 'mound', 'food', 'ingredient', 'storage')
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
        rect('rim',6,18,36,8,4)
        bez('sugar',(12,18),((16,10),(20,6),(24,6)),((28,6),(32,10),(36,18)))
        bez('sack',(10,26),((6,42),(12,42),(24,42)),((36,42),(42,42),(38,26)))
        self.relate('connect','sugar','rim');self.relate('connect','sack','rim')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
