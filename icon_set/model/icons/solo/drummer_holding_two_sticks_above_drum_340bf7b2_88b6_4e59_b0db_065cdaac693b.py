'Drummer Holding Two Sticks Above Drum.\nSymbol plan: A round headed drummer sits behind a small cylindrical drum with an elliptical top. Two sticks angle upward beside the shoulders, with one round hand visible on the right.\nConstruction: Human full_body_ref.png: circular heads, coherent torso/limbs, exact 8u centerline / 4u ink head-to-neck clearance. Lucide drum: broad cylindrical outline.\nReduction: Two sticks and a broad drum body retain the percussion action.\nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '340bf7b2-88b6-4e59-b0db-065cdaac693b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/drummer_340bf7b2-88b6-4e59-b0db-065cdaac693b.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'drummer-holding-two-sticks-above-drum'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('drummer', 'drum', 'sticks', 'music', 'person', 'percussion', 'playing')
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
        circle('head',24,12,6);line('torso',(24,26),(24,34));line('arms',(10,26),(38,26))
        line('stick-left',(10,26),(6,20));line('stick-right',(38,26),(42,20))
        rect('drum',16,34,16,8,4);self.relate('connect','torso','drum');self.relate('connect','arms','torso');self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
