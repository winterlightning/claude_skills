'Tumbling Figure with Raised Legs.\nSymbol plan: A plain human figure tilts headfirst toward the lower right, with a round head beside an angled torso. Two legs stretch upward in a wide V, while one arm reaches down toward the lower left.\nConstruction: Human full_body_ref.png: circular heads, coherent torso/limbs, exact 8u centerline / 4u ink head-to-neck clearance.\nReduction: Keep inverted torso and V-shaped legs; head follows a horizontal neck bend.\nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd6f4580b-3c39-42da-abe7-0d859e33509b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/somersault_d6f4580b-3c39-42da-abe7-0d859e33509b.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'tumbling-figure-with-raised-legs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('person', 'tumble', 'somersault', 'acrobat', 'body', 'movement')
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
        circle('head',36,30,6);line('torso',(22,30),(18,30));line('lower-torso',(18,30),(16,24));poly('legs',(6,6),(16,24),(24,6));poly('arm',(22,30),(16,34),(14,42));self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
