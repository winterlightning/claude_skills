'Sleeper Beneath a Raised Blanket.\nSymbol plan: A round head rests at the left end of a side-view bed. A long raised blanket contour covers the body to the right, above a straight mattress band and short supporting legs.\nConstruction: Human full_body_ref.png: circular heads, coherent torso/limbs, exact 8u centerline / 4u ink head-to-neck clearance. Lucide bed: horizontal mattress and upright posts.\nReduction: One mattress line and a raised blanket preserve the sleeper; head r4 at (16,20) to blanket shoulder (28,20) leaves exactly 4u visible ink.\nKeyshape HRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '787c5c08-ffab-47fa-80a9-73b145ee0e1b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bed single_787c5c08-ffab-47fa-80a9-73b145ee0e1b.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'sleeper-beneath-a-raised-blanket'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('sleeper', 'bed', 'blanket', 'head', 'mattress', 'sleep', 'rest')
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
        circle('head',16,20,4);line('headboard',(4,8),(4,40));line('footboard',(44,28),(44,40));line('bed',(4,32),(44,32))
        line('blanket-side',(28,20),(28,32));bez('blanket',(28,20),((36,20),(44,22),(44,28)));self.relate('connect','blanket-side','bed')
        self.relate('connect','bed','headboard');self.relate('connect','bed','footboard');self.relate('connect','blanket','footboard')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
