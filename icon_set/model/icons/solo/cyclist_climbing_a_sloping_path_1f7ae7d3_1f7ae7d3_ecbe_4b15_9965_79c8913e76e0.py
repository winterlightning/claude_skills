'Cyclist Climbing a Sloping Path.\nSymbol plan: A round-headed rider leans forward above two bicycle wheels at different heights. Bent arms reach toward the higher front wheel, and a straight ground line rises from lower left to upper right.\nConstruction: human_ref/full_body_ref.png and Lucide bike: circular wheels and leaning pose.\nReduction: Wheel height difference carries the climb; omit ramp and crowded frame triangle.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1f7ae7d3-ecbe-4b15-9965-79c8913e76e0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/biking mountain_1f7ae7d3-ecbe-4b15-9965-79c8913e76e0.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'cyclist-climbing-a-sloping-path-1f7ae7d3'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('cyclist', 'bicycle', 'uphill', 'slope', 'rider', 'wheels', 'mountain')
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
        circle('head',30,10,4)
        bez('torso',(30,22),((30,24),(26,24),(23,27)))
        poly('arms',(30,22),(36,22),(42,22))
        poly('leg',(23,27),(24,33),(24,38))
        circle('back-wheel',10,38,4);circle('front-wheel',38,38,4)
        line('bike',(13,35),(23,27));line('fork',(38,34),(42,22))
        self.relate('connect','bike','back-wheel');self.relate('connect','fork','front-wheel')
        self.mark_human_figure('rider',head='head',torso='torso',torso_junction='start')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
