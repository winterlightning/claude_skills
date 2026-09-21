'Five-Leaf Oregano Sprig.\nSymbol plan: A straight herb stem carries two pairs of pointed oval leaves and one upright terminal leaf. Short diagonal branches connect the side leaves to the stem, alternating around its central vertical line.\nConstruction: Lucide sprout: paired curved sides and shared branch contacts.\nReduction: Five broad leaves retained; the small terminal leaf is rounded to keep its opening clear.\nKeyshape VRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '37f4b89d-a50b-4a62-9fea-09a94fc37e35'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/oregano_37f4b89d-a50b-4a62-9fea-09a94fc37e35.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'five-leaf-oregano-sprig'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('oregano', 'herb', 'leaves', 'plant', 'stem', 'botanical')
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
        circle('terminal',24,8,4)
        self.relate('connect','terminal','stem-a')
        line('stem-a',(24,12),(24,26));line('stem-b',(24,26),(24,44))
        for i,(y,side) in enumerate(((16,-1),(16,1),(34,-1),(34,1))):
         x=24+side*16
         bez('leaf'+str(i),(24,y+10),((x,y+10),(x,y+4),(x,y)),((x-side*8,y),(24+side*6,y+6),(24,y+10)))
         self.relate('connect','leaf'+str(i),'stem-a' if y==16 else 'stem-b')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
