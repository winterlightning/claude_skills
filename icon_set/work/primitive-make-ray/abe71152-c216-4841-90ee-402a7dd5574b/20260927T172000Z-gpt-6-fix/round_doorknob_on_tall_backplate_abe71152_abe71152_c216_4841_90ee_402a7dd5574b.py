"Round Doorknob on Tall Backplate.\nSymbol plan: A large round doorknob projects from the upper half of a tall rounded rectangular backplate. A smaller circular fitting sits below it, and the knob overlaps the plate's right edge.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Retain the source parts and arrangement.\nKeyshape VRECT_L: ink extremes (6, 2, 42, 46)."
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'abe71152-c216-4841-90ee-402a7dd5574b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-doorknob-on-tall-backplate-abe71152/20260927T171905Z-thuan-mac-1/reference/doorknob_abe71152-c216-4841-90ee-402a7dd5574b.svg'
AUTHOR = "gpt-6"

class BatchIcon(Solo48):
    icon_id = 'round-doorknob-on-tall-backplate-abe71152'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('doorknob', 'door', 'handle', 'backplate', 'round', 'hardware', 'lock')
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
        line('plate-top',(12,4),(20,4))
        arc('plate-top-corner',(20,4),(24,8),4)
        line('plate-upper-right',(24,8),(24,14))
        self.add_arc('knob-outer',(24,14),(24,30),radius_x=10,large_arc=True,sweep=True)
        line('plate-lower-right-1',(24,30),(26,34))
        line('plate-lower-right-2',(26,34),(26,40))
        arc('plate-bottom-corner',(26,40),(22,44),4)
        line('plate-bottom',(22,44),(12,44))
        arc('plate-lower-left',(12,44),(8,40),4)
        line('plate-left',(8,40),(8,8))
        arc('plate-upper-left',(8,8),(12,4),4)
        con('plate-and-knob','plate-top','plate-top-corner','plate-upper-right',
            'knob-outer','plate-lower-right-1','plate-lower-right-2','plate-bottom-corner','plate-bottom',
            'plate-lower-left','plate-left','plate-upper-left',closed=True)
        self.add_arc('knob-inner',(24,30),(24,14),radius_x=10,sweep=True)
        self.relate('connect','knob-inner','plate-and-knob')
        self.add_dot('screw',(17,35))
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
