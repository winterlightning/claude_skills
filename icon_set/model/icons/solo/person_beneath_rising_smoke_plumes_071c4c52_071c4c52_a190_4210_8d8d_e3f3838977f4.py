'Person Beneath Rising Smoke Plumes.\nSymbol plan: A small round-headed bust stands beneath two broad groups of curling smoke-like contours. The plumes rise and spread to either side, with scalloped inner curves and detached outer arcs.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Two large curled smoke plumes retain the mirrored source composition.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '071c4c52-a190-4210-8d8d-e3f3838977f4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/ashura day of atonement tenth day of muharram_071c4c52-a190-4210-8d8d-e3f3838977f4.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'person-beneath-rising-smoke-plumes-071c4c52'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    human_construction = "bust"
    category = "objects/reference"
    aliases = ()
    keywords = ('person', 'smoke', 'plumes', 'curves', 'bust', 'rising', 'figure')
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
        circle('head',24,31,3)
        arc('bust-left',(15,42),(24,38),9,4)
        arc('bust-right',(24,38),(33,42),9,4)
        self.relate('connect','head','bust-left');self.relate('connect','head','bust-right')
        bez('smoke-left',(16,22),((6,22),(6,18),(6,14)),((6,10),(9,6),(12,6)),((18,6),(20,10),(20,14)))
        bez('smoke-right',(32,22),((42,22),(42,18),(42,14)),((42,10),(39,6),(36,6)),((30,6),(28,10),(28,14)))
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
