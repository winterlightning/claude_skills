"Person Holding a Small Bowl.\nSymbol plan: A round-headed figure has one arm bent across the lower torso, with the hand resting against a small rounded bowl. The opposite arm hangs straight beside the body's outer contour.\nConstruction: Human full_body_ref.png: circular heads, coherent torso/limbs, exact 8u centerline / 4u ink head-to-neck clearance.\nReduction: A bent arm supports a broad semicircular bowl beside the cropped torso.\nKeyshape VRECT_L."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '144ab7e4-5b62-44f3-80ef-97d4f5319804'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/beggar_144ab7e4-5b62-44f3-80ef-97d4f5319804.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'person-holding-a-small-bowl'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('person', 'bowl', 'holding', 'hand', 'donation', 'standing', 'figure')
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
        circle('head',16,10,6);line('torso',(16,24),(16,44));poly('left-arm',(8,32),(8,24),(16,24));line('right-arm',(16,28),(26,34))
        arc('bowl',(26,34),(40,34),7,s=False);line('rim',(40,34),(26,34));con('bowl-shape','bowl','rim',closed=True)
        self.relate('connect','right-arm','torso');self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
