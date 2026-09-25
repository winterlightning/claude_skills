'Mustard Squeeze Bottle.\nSymbol plan: A tall squeeze bottle has a rounded rectangular body and a short cylindrical collar. A narrow tapered nozzle rises from the center of the collar, ending in a small rounded tip.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Retain the source parts and arrangement.\nKeyshape VRECT_M: ink extremes (8, 2, 40, 46).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7c962d05-9c47-401c-91bd-8dc4600a8dc0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/mustard_7c962d05-9c47-401c-91bd-8dc4600a8dc0.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'mustard-squeeze-bottle-7c962d05'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('mustard', 'bottle', 'condiment', 'nozzle', 'squeeze', 'food')
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
        poly('nozzle',(18,20),(20,4),(28,4),(30,20))
        rect('collar',16,20,16,8,2)
        bez('bottle',(16,28),((10,30),(10,34),(10,38)),((10,44),(14,44),(24,44)),((34,44),(38,44),(38,38)),((38,34),(38,30),(32,28)))
        self.relate('connect','nozzle','collar');self.relate('connect','bottle','collar')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
