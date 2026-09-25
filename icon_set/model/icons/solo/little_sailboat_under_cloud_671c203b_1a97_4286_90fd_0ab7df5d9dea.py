'Little Sailboat under Cloud.\nSymbol plan: A small sailboat has a trapezoidal hull and one triangular sail rising above its center. Two rows of waves run below, with a rounded cloud in the upper right sky.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: One flat waterline replaces two crowded waves; keep the separate cloud and sail.\nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '671c203b-1a97-4286-90fd-0ab7df5d9dea'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/business boat success_671c203b-1a97-4286-90fd-0ab7df5d9dea.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'little-sailboat-under-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('sailboat', 'boat', 'waves', 'cloud', 'sail', 'water', 'scene')
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
        poly('hull',(6,26),(14,34),(34,34),(42,26),(6,26))
        poly('sail',(10,26),(18,10),(24,26))
        bez('cloud',(32,16),((28,16),(28,6),(34,6)),((38,6),(38,10),(38,10)),((42,10),(42,12),(42,14)),((42,18),(36,16),(32,16)))
        bez('wave',(6,42),((12,42),(18,42),(24,42)),((30,42),(36,42),(42,42)))
        self.relate('connect','sail','hull')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
