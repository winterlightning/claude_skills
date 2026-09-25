"""A rider pedaling a bicycle.
Plan: SQUARE leaves upper space for the rider and lower space for paired wheels.
Reduction: Removed duplicate triangular frame tubes and crowded upper bar; retained open frame rails, front fork, bent leg, and both wheels.
Construction: Shared full_body_ref.png for round head and coherent limbs; Lucide bike for cycling pose and round wheels.
Layout: Forward-facing asymmetric pose. Head center (26,10), radius4; actual torso start (26,22): 22-(10+4)=8 centerline, exactly4 visible ink gap; torso is vertical at the neck and head is on that axis."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '816c0a6d-a6b1-4041-9b3e-aa2bb963535f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/bicycle person_816c0a6d-a6b1-4041-9b3e-aa2bb963535f.svg'
AUTHOR = "gpt-6"

class BatchIcon(Solo48):
    icon_id = 'cyclist-on-a-fully-framed-bicycle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('cyclist', 'bicycle', 'rider', 'frame', 'wheels', 'transport', 'pedaling')
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
        circle('head',26,10,4);line('torso',(26,22),(26,24));line('lower-torso',(26,24),(20,28))
        poly('arms',(26,22),(36,23),(42,22));poly('leg',(20,28),(24,32),(24,38))
        circle('rear',10,38,4);circle('front',38,38,4);line('fork',(36,23),(38,34));self.relate('connect','fork','front');self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        poly('frame',(10,34),(20,28),(38,34));self.relate('connect','frame','rear');self.relate('connect','frame','front');self.relate('connect','frame','leg');self.relate('connect','frame','fork')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
