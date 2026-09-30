'Crested Dinosaur in Left Facing Profile.\nSymbol plan: A crested dinosaur faces left with an elongated snout and a narrow crest sweeping back above its head. Its curved body carries short forelimbs, a bent hind leg, and a pointed trailing tail.\nConstruction: Reference-specific coherent contours; no useful exact Lucide match.\nReduction: Broad crest and neck retain the dinosaur identity; one hind leg and one short forelimb replace tiny overlapping limbs.\nKeyshape HRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2d6c89c4-e968-4d8b-8072-8bb25e0843ff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/dinosaur raptor 2_2d6c89c4-e968-4d8b-8072-8bb25e0843ff.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'crested-dinosaur-in-left-facing-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('dinosaur', 'crest', 'parasaurolophus', 'prehistoric', 'animal', 'tail', 'profile')
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
        poly('crest',(4,16),(12,10),(18,8),(14,18))
        bez('back',(14,18),((18,30),(24,18),(32,24)),((36,26),(36,32),(44,32)))
        bez('tail',(44,32),((38,34),(34,32),(30,30)))
        poly('leg',(30,30),(30,40),(20,40))
        bez('belly',(20,40),((20,34),(16,32),(14,32)),((10,32),(12,24),(12,24)))
        poly('throat',(12,24),(4,24),(4,16))
        line('arm',(12,32),(8,36));self.relate('connect','arm','belly')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
