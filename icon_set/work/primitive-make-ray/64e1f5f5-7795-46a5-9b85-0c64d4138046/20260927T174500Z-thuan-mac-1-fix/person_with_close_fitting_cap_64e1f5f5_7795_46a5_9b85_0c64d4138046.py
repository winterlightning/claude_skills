"Person Wearing a Cap.\nSymbol plan: Cap seam retained; broad circular shoulders meet jaw ink.\nConstruction: human_ref/user.svg; Lucide user-round circular jaw and shoulders.\nKeyshape VRECT_L: exact SOLO48 contract envelope, selected for this subject's proportions.\nSource UUID and original reference preserved."
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '64e1f5f5-7795-46a5-9b85-0c64d4138046'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-with-close-fitting-cap/20260927T174057Z-thuan-mac-1/reference/crewman_64e1f5f5-7795-46a5-9b85-0c64d4138046.svg'
AUTHOR = "gpt-6-astra"

class BatchIcon(Solo48):
    icon_id = 'person-with-close-fitting-cap'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    human_construction = "bust"
    human_construction = "bust"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('person', 'cap', 'headwear', 'profile', 'bust', 'shoulders', 'portrait')
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
        arc('cap',(12,16),(36,16),12)
        bez('cap-seam',(12,16),((18,18),(30,18),(36,16)))
        arc('jaw',(36,16),(12,16),12)
        # cap seam is the visible brim
        arc('shoulders',(8,44),(40,44),16,12)
        self.relate('connect','jaw','shoulders')

        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
