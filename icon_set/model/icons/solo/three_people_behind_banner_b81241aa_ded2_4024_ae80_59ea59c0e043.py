'Three People behind Banner.\nSymbol plan: Three people stand side by side behind a wide blank rectangular banner. Their round heads and curved shoulders rise above it, while three tapered lower bodies extend beneath the sign.\nConstruction: Human full_body_ref.png: round heads and simple limbs; head r3 with exact 8u centerline torso gap.\nReduction: Three heads and lower bodies remain; the shared sign replaces hidden arm details.\nKeyshape HRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b81241aa-ded2-4024-ae80-59ea59c0e043'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/protester 1_b81241aa-ded2-4024-ae80-59ea59c0e043.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'three-people-behind-banner'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ()
    keywords = ('people', 'banner', 'protest', 'group', 'sign', 'figures')
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
        for i,x in enumerate((8,24,40)):
         circle('head'+str(i),x,11,3)
         line('torso'+str(i),(x,22),(x,26));self.mark_human_figure('person'+str(i),head='head'+str(i),torso='torso'+str(i),torso_junction='start')
         line('legs'+str(i),(x,34),(x,40))
        rect('banner',4,26,40,8)
        for i in range(3):self.relate('connect','torso'+str(i),'banner');self.relate('connect','legs'+str(i),'banner')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
