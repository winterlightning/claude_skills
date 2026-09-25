# Final reduction: Omit secondary crest band, rear tab and tiny inner ear hole. Retain helmet silhouette and small circular earplate.
'Crested Helmet with Round Ear Plate.\nSymbol plan: A helmet faces left with a projecting brow, deep face opening, and flat lower edge. A large circular ear plate occupies the side beneath a broad raised crest and smaller rear tab.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Omit secondary crest band, rear tab, and tiny inner ear hole while retaining helmet outline and earplate.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c86ab490-6c39-41d4-af82-d4ab926f58b6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/megaman 1_c86ab490-6c39-41d4-af82-d4ab926f58b6.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'crested-helmet-with-round-ear-plate'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ()
    keywords = ('helmet', 'crest', 'armor', 'headwear', 'earplate', 'profile', 'protection')
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
        bez('crown',(6,20),((8,9),(17,6),(24,6)),((34,6),(42,16),(42,24)))
        poly('body',(42,24),(38,34),(38,42),(12,42),(14,26),(6,26),(6,20))
        con('helmet','crown',*['body-'+str(i) for i in range(1,7)],closed=True)
        circle('ear',26,29,3)
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
