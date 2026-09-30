'Piping Nozzle Above Icing Dollop.\nSymbol plan: A pastry nozzle points down and left above a rounded dollop with a curled pointed peak. The nozzle joins a wider piping bag extending out toward the upper right.\nConstruction: Reference-specific coherent contours; no useful exact Lucide match.\nReduction: Nozzle reduced to a short connected stroke; retain the bag and separate icing peak.\nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'aff563ce-3eaf-4937-9894-dfe356ba0aa4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/cookies decirating 2_aff563ce-3eaf-4937-9894-dfe356ba0aa4.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'piping-nozzle-above-icing-dollop'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('piping', 'icing', 'nozzle', 'pastry', 'baking', 'dollop', 'cream')
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
        poly('bag',(30,6),(42,14),(28,24),(20,18),closed=True)
        line('nozzle',(24,21),(20,26));self.relate('connect','nozzle','bag')
        bez('icing',(6,38),((6,32),(10,34),(12,30)),((12,36),(26,32),(26,38)),((26,42),(18,42),(16,42)),((14,42),(6,42),(6,38)))
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
