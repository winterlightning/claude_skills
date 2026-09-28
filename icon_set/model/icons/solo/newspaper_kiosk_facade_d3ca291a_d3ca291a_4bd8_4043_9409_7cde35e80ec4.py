'Newspaper Kiosk Facade.\nSymbol plan: A kiosk has a broad signboard above a rectangular booth and small lower door. A wide inset display occupies the upper half, divided into panes with short horizontal marks inside.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Omit tiny window stripes; retain sign, display pane and lower door.\nKeyshape VRECT_L: ink extremes (6, 2, 42, 46).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd3ca291a-4bd8-4043-9409-7cde35e80ec4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/newsstand_d3ca291a-4bd8-4043-9409-7cde35e80ec4.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'newspaper-kiosk-facade-d3ca291a'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('kiosk', 'newspaper', 'booth', 'shop', 'newsstand', 'building')
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
        rect('sign',8,4,32,8,2)
        poly('booth',(10,12),(10,44),(38,44),(38,12))
        rect('window',18,20,12,8)
        poly('door',(18,44),(18,36),(30,36),(30,44))
        self.relate('connect','sign','booth');self.relate('connect','door','booth')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
