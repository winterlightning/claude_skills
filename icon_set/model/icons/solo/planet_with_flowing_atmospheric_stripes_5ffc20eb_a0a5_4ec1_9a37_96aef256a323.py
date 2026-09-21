"Planet Venus with Atmospheric Layers.\nSymbol plan: Two atmospheric curves preserve the S-shaped flow; omit tight third nesting.\nConstruction: Lucide original and atomic-debug: bath, truck, notebook, piano, orbit, sprout and pill-bottle; coherent arcs, shared joins and repeated dimensions.\nKeyshape CIRCLE: exact SOLO48 contract envelope, selected for this subject's proportions.\nSource UUID and original reference preserved."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5ffc20eb-a0a5-4ec1-9a37-96aef256a323'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/astronomy planet venus_5ffc20eb-a0a5-4ec1-9a37-96aef256a323.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'planet-with-flowing-atmospheric-stripes'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('planet', 'venus', 'stripes', 'atmosphere', 'curves', 'astronomy', 'space')
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
        circle('planet',24,24,20)
        bez('layer',(4,24),((9,12),(30,10),(30,20)),((30,28),(16,22),(16,36)))
        line('layer-end',(16,36),(12,40))
        bez('lower',(24,44),((24,32),(30,28),(40,36)))
        self.relate('connect','planet','layer');self.relate('connect','planet','layer-end');self.relate('connect','planet','lower')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
