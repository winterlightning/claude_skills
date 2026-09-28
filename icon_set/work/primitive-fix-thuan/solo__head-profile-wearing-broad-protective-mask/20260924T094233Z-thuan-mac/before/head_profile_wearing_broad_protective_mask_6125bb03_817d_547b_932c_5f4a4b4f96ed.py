"""Head Wearing Protective Face Mask.
Symbol plan: Left-facing masked head; large mask boundary joins the head outline and rear strap.
Reference construction: human_ref/user.svg.
VRECT_L visible extremes: (6, 2, 42, 46); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6125bb03-817d-547b-932c-5f4a4b4f96ed'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/air pollution mask_6125bb03-817d-547b-932c-5f4a4b4f96ed.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'head-profile-wearing-broad-protective-mask'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/ecology"
    aliases = ()
    keywords = ('mask', 'head', 'profile', 'protection', 'face', 'health', 'air', 'pollution')
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=sweep)
        def contour(n,*parts,closed=False):
            self.contours[:] = [c for c in self.contours if not set(c.members) & set(parts)]
            self.add_contour(n,*parts,closed=closed)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)
        def rect(n,x,y,w,h,r=0):
            if not r:
                poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
                return
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if i%2: arc(n+str(i),a,b,r)
                else: line(n+str(i),a,b)
            contour(n,*(n+str(i) for i in range(8)),closed=True)
        arc('crown',(8,20),(40,20),16)
        line('forehead',(8,20),(8,24))
        poly('neck-right',(40,20),(40,24),(40,32),(34,38),(34,44))
        poly('mask',(8,24),(8,32),(12,38),(22,38),(40,32))
        poly('strap',(8,24),(22,24),(40,24))
        line('neck-left',(22,38),(22,44))
        line('mask-side',(22,24),(22,38))
        self.add_dot('eye',(22,15))
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
