'Outboard Motor with Broad Propeller.\nSymbol plan: An outboard motor has a rounded rectangular engine cover and a short handle projecting left. A long lower shaft curves at its foot beside a broad two ended propeller.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Single broad propeller curve replaces the thin divided blade.\nKeyshape VRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4b6bf1a5-cf3b-49b9-ad1b-b0f03c95708f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/boat engine 2_4b6bf1a5-cf3b-49b9-ad1b-b0f03c95708f.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'outboard-motor-with-broad-propeller'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('motor', 'outboard', 'boat', 'engine', 'propeller', 'marine', 'equipment')
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
        rect('engine',16,4,24,16,4)
        line('grip',(8,12),(16,12))
        poly('shaft',(18,20),(18,38));arc('foot',(18,38),(24,44),6,s=False)
        poly('shaft-back',(24,44),(28,44),(28,20))
        line('axle',(28,34),(40,34));arc('prop',(40,28),(40,42),3,7,s=False)
        self.relate('connect','engine','grip');self.relate('connect','engine','shaft');self.relate('connect','engine','shaft-back');self.relate('connect','axle','shaft-back');self.relate('connect','prop','axle')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
