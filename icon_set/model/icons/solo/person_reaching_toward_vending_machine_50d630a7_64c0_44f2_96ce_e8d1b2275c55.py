"Person Using Vending Machine.\nSymbol plan: Four product boxes reduce to one product stroke and one delivery slot; keep the reaching hand and full machine.\nConstruction: human_ref/full_body_ref.png: circular heads and coherent limbs; Lucide object construction where relevant.\nKeyshape SQUARE: exact SOLO48 contract envelope, selected for this subject's proportions.\nSource UUID and original reference preserved."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '50d630a7-64c0-44f2-96ce-e8d1b2275c55'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/eat vending machine_50d630a7-64c0-44f2-96ce-e8d1b2275c55.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'person-reaching-toward-vending-machine'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('person', 'vending', 'machine', 'products', 'shopping', 'dispenser', 'reach')
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
        circle('head',11,11,5)
        line('torso',(11,24),(11,31));poly('legs',(6,42),(11,31),(16,42))
        poly('arm',(11,24),(20,28),(26,28))
        poly('machine',(26,28),(26,6),(42,6),(42,42),(26,42),(26,28),closed=False)
        line('product',(34,15),(34,18));line('slot',(34,32),(34,34))
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
