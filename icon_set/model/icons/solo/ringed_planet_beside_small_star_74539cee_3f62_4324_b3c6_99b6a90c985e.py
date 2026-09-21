"Planet with Ring and Star.\nSymbol plan: Open diagonal orbit preserves the ringed globe without a tiny return loop; separate star remains.\nConstruction: Lucide original and atomic-debug: bath, truck, notebook, piano, orbit, sprout and pill-bottle; coherent arcs, shared joins and repeated dimensions.\nKeyshape SQUARE: exact SOLO48 contract envelope, selected for this subject's proportions.\nSource UUID and original reference preserved."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '74539cee-3f62-4324-b3c6-99b6a90c985e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/mars_74539cee-3f62-4324-b3c6-99b6a90c985e.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'ringed-planet-beside-small-star'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('planet', 'ring', 'star', 'space', 'astronomy', 'orbit', 'sky')
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
        circle('planet',20,28,14)
        bez('orbit',(6,32),((12,36),(34,26),(42,22)))
        poly('star',(38,6),(38,14));line('cross',(34,10),(42,10));self.relate('connect','star','cross')
        self.relate('connect','planet','orbit')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
