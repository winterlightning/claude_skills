'Symmetric Claw Gripper.\nSymbol plan: A claw gripper hangs below a shallow rounded mount. Two large curved outer jaws taper inward around a central opening, with smaller pointed contours facing each other inside.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Retain the source parts and arrangement.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8a8418ac-5b0f-416a-b52c-e5ff21929487'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/claw_8a8418ac-5b0f-416a-b52c-e5ff21929487.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'symmetric-claw-gripper'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('claw', 'gripper', 'jaws', 'mechanical', 'tool', 'grab', 'machine')
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
        rect('mount',16,6,16,8)
        bez('left',(16,14),((10,14),(6,22),(6,28)),((6,34),(10,39),(16,42)),((12,32),(14,27),(18,22)))
        bez('right',(30,22),((34,27),(36,32),(32,42)),((38,39),(42,34),(42,28)),((42,22),(38,14),(32,14)))
        poly('inner',(18,22),(24,30),(30,22))
        con('jaws','left','inner-1','inner-2','right')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
