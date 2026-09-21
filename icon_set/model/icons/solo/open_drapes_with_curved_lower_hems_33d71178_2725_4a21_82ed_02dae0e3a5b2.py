'Open Drapes with Curved Lower Hems.\nSymbol plan: Two curtains hang from a shared top edge and gather toward opposite sides around mid height. Their curved inner edges reveal a wide empty opening, while gently curved hems close the panels below.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Omit duplicate outer fold lines; retain gathered curtains and ties.\nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '33d71178-2725-4a21-82ed-02dae0e3a5b2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/drapes_33d71178-2725-4a21-82ed-02dae0e3a5b2.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'open-drapes-with-curved-lower-hems'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('curtains', 'drapes', 'window', 'fabric', 'panels', 'opening', 'interior')
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
        line('rod',(6,6),(42,6))
        bez('left-inner',(20,6),((20,16),(14,25),(10,26)),((16,34),(14,42),(6,42)))
        line('left-side',(6,42),(6,6))
        bez('right-inner',(28,6),((28,16),(34,25),(38,26)),((32,34),(34,42),(42,42)))
        line('right-side',(42,42),(42,6))
        line('tie-left',(6,26),(10,26));line('tie-right',(38,26),(42,26))
        self.relate('connect','rod','left-inner');self.relate('connect','rod','right-inner');self.relate('connect','tie-left','left-side');self.relate('connect','tie-left','left-inner');self.relate('connect','tie-right','right-side');self.relate('connect','tie-right','right-inner')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
