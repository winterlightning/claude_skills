'Curved Palm Tree Between Sand Dunes.\nSymbol plan: A slender palm trunk curves upward from a low sand dune to a crown of spreading arched fronds. Another rolling dune passes behind the trunk across the middle of the scene.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Four broad fronds replace fine leaf subdivisions.\nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a9c44c76-68f4-4e82-a0ad-c3c667877bef'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/desert_a9c44c76-68f4-4e82-a0ad-c3c667877bef.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'curved-palm-tree-between-sand-dunes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('palm', 'tree', 'dune', 'sand', 'desert', 'fronds', 'landscape')
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
        bez('trunk',(28,42),((34,30),(30,19),(24,14)))
        bez('frond-a',(24,14),((20,6),(10,6),(6,6)))
        bez('frond-b',(24,14),((28,6),(38,6),(42,6)))
        bez('frond-c',(24,14),((12,12),(6,18),(6,22)))
        bez('frond-d',(24,14),((33,12),(42,18),(42,22)))
        bez('dune',(6,32),((16,26),(24,32),(42,32)))
        bez('front-dune',(14,42),((25,38),(32,40),(42,42)))
        self.relate('connect','trunk','dune');self.relate('connect','trunk','front-dune')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
