'Cardboard Box with Spread Flaps.\nSymbol plan: An open cardboard box appears in perspective with four flaps spreading outward around its opening. Two tall side panels meet at a central vertical corner beneath the front flaps.\nConstruction: Lucide package-open: shared flap corners and central box corner.\nReduction: \nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '312fedf7-9c1f-4186-95b0-9064c0a4e997'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/box open_312fedf7-9c1f-4186-95b0-9064c0a4e997.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'cardboard-box-with-spread-flaps'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('box', 'cardboard', 'open', 'flaps', 'package', 'packing', 'container')
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
        poly('opening',(10,16),(24,22),(38,16),(24,10),(10,16))
        poly('left-front',(10,16),(6,26),(20,30),(24,22))
        poly('right-front',(24,22),(28,30),(42,26),(38,16))
        poly('left-rear',(10,16),(6,6),(24,10))
        poly('right-rear',(24,10),(42,6),(38,16))
        poly('box',(10,28),(10,36),(24,42),(38,36),(38,28))
        line('corner',(24,22),(24,42))
        self.relate('connect','box','left-front');self.relate('connect','box','right-front');self.relate('connect','corner','box')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
