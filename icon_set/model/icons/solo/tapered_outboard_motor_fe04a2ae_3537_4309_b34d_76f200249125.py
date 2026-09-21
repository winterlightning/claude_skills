'Tapered Outboard Motor.\nSymbol plan: A boat motor appears in profile with a large rounded engine cover and a small grip extending left. Its tapered lower housing ends beside a short shaft and curved propeller.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Retain the tapered lower casing and a broad open propeller curve.\nKeyshape VRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fe04a2ae-3537-4309-b34d-76f200249125'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/boat engine 1_fe04a2ae-3537-4309-b34d-76f200249125.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'tapered-outboard-motor'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('motor', 'outboard', 'engine', 'boat', 'propeller', 'marine', 'transport')
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
        rect('engine',16,4,24,16,4)
        line('grip',(8,12),(16,12))
        bez('shaft',(20,20),((20,32),(20,44),(25,44)),((28,44),(27,31),(32,20)))
        line('axle',(30,34),(40,34));arc('prop',(40,28),(40,42),3,7,s=False)
        self.relate('connect','engine','grip');self.relate('connect','engine','shaft');self.relate('connect','axle','shaft');self.relate('connect','prop','axle')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
