'Twin Peaks Inside a Rounded Hill Emblem.\nSymbol plan: A broad rounded hill outline encloses two angular mountain peaks of unequal height. Their sloping sides meet the curved lower boundary, joining the inner landscape to the outer shape.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Retain the source parts and arrangement.\nKeyshape HRECT_M: ink extremes (2, 8, 46, 40).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7acafe9e-8c82-4fc5-aa6b-a6d51b2fb48b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/basecamp logo_7acafe9e-8c82-4fc5-aa6b-a6d51b2fb48b.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'twin-peaks-inside-a-rounded-hill-emblem-7acafe9e'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('mountains', 'peaks', 'hill', 'landscape', 'emblem', 'basecamp', 'outline')
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
        bez('hill',(4,38),((4,10),(12,10),(24,10)),((36,10),(44,10),(44,38)))
        line('base',(4,38),(44,38))
        poly('peaks',(12,38),(20,24),(24,34),(32,24),(36,38))
        self.relate('connect','peaks','base')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
