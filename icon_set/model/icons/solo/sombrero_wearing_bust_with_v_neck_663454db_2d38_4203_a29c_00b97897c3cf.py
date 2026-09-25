"Person wearing Sombrero.\nSymbol plan: Broad brim and round crown retained; omit the crowded V collar.\nConstruction: human_ref/user.svg: circular jaw and rounded shoulders; source sombrero silhouette.\nKeyshape HRECT_L: exact SOLO48 contract envelope, selected for this subject's proportions.\nSource UUID and original reference preserved."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '663454db-2d38-4203-a29c-00b97897c3cf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/mariachi_663454db-2d38-4203-a29c-00b97897c3cf.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'sombrero-wearing-bust-with-v-neck'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    human_construction = "bust"
    category = "primitives-generate"
    aliases = ()
    keywords = ('sombrero', 'hat', 'person', 'bust', 'headwear', 'portrait', 'clothing')
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
        arc('crown',(16,16),(32,16),8)
        line('brim-left',(4,16),(16,16));line('brim-mid',(16,16),(32,16));line('brim-right',(32,16),(44,16))
        arc('jaw',(32,16),(16,16),8)
        arc('shoulders',(8,40),(40,40),16,12)
        self.relate('connect','jaw','shoulders')

        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
