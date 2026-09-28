'Pair of Plain Round Maracas.\nSymbol plan: Two maracas sit side by side at opposing slight angles, each with a broad round head and narrow handle. The right maraca sits higher, and both handles end in rounded tips.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Single strokes replace narrow handles; preserve opposing lean and different heights.\nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6f216462-042e-4789-af84-8030d0a69cf4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/maracas 1_6f216462-042e-4789-af84-8030d0a69cf4.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'pair-of-plain-round-maracas'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "music"
    categories = ("music", "primitive", "primitives")
    aliases = ()
    keywords = ('maracas', 'shakers', 'percussion', 'music', 'instrument', 'handles', 'pair')
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
        circle('head-left',13,17,7);circle('head-right',35,13,7)
        line('handle-left',(13,24),(19,42));line('handle-right',(35,20),(29,38))
        self.relate('connect','head-left','handle-left');self.relate('connect','head-right','handle-right')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
