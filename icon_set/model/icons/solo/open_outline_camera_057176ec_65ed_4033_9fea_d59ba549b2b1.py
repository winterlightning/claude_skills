'Open Outline Camera.\nSymbol plan: A camera outline has rounded shoulders, a raised top and a large circular lens. A broad gap interrupts the lower left portion of its otherwise rectangular body.\nConstruction: Lucide pill/rounded corners: tangent quarter arcs; preserve open camera body.\nReduction: Retain the source parts and arrangement.\nKeyshape HRECT_L: ink extremes (2, 6, 46, 42).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '057176ec-65ed-4033-9fea-d59ba549b2b1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/camera double_057176ec-65ed-4033-9fea-d59ba549b2b1.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'open-outline-camera'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('camera', 'lens', 'photography', 'outline', 'open', 'device', 'body')
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
        poly('start',(4,28),(4,18))
        arc('tl',(4,18),(10,12),6)
        poly('top',(10,12),(16,12),(20,8),(28,8),(32,12),(38,12))
        arc('tr',(38,12),(44,18),6)
        line('right',(44,18),(44,34));arc('br',(44,34),(38,40),6)
        line('bottom',(38,40),(26,40))
        con('body','start-1','tl',*['top-'+str(i) for i in range(1,6)],'tr','right','br','bottom')
        circle('lens',24,25,7)
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
