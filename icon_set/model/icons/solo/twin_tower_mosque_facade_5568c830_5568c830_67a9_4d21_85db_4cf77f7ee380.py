'Twin-Tower Mosque Facade.\nSymbol plan: A mosque facade has two tall rounded towers flanking a lower central wall. Slim spires rise from both towers, horizontal bands cross their upper sections, and a pointed arched entrance opens below.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Retain the source parts and arrangement.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5568c830-67a9-4d21-85db-4cf77f7ee380'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/nasir ol molk mosque iran_5568c830-67a9-4d21-85db-4cf77f7ee380.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'twin-tower-mosque-facade-5568c830'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('mosque', 'towers', 'facade', 'architecture', 'building', 'entrance')
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
        poly('left',(6,42),(6,16));arc('dome-a',(6,16),(18,16),6)
        poly('wall',(18,16),(18,26),(30,26),(30,16));arc('dome-b',(30,16),(42,16),6)
        poly('right',(42,16),(42,42),(6,42))
        line('spire-a',(12,6),(12,10));line('spire-b',(36,6),(36,10))
        poly('door',(20,42),(20,36),(24,32),(28,36),(28,42))
        line('band-a',(6,24),(18,24));line('band-b',(30,24),(42,24))
        self.relate('connect','door','right');self.relate('connect','band-a','left');self.relate('connect','band-a','wall');self.relate('connect','band-b','right');self.relate('connect','band-b','wall');self.relate('connect','spire-a','dome-a');self.relate('connect','spire-b','dome-b')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
