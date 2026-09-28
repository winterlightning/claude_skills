'Diagonal Oboe.\nSymbol plan: A long oboe runs diagonally from a flared lower left bell toward a narrow upper right mouthpiece. Three small tone-hole marks follow the slim body, which ends in a short projecting reed.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Two tone-hole dots replace three close rings; broad bell seam retained.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '73aaaaa4-5952-463a-a503-f7716b6e5ad7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-oboe-73aaaaa4/20260927T164353Z-thuan-mac-1/reference/oboe_73aaaaa4-5952-463a-a503-f7716b6e5ad7.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'diagonal-oboe-73aaaaa4'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('oboe', 'instrument', 'woodwind', 'reed', 'music', 'bell')
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
        # A tapered wooden body opens into the broad lower-left bell.
        poly('body',(6,34),(11,32),(32,8),(36,8),(40,12),(40,16),
             (18,37),(16,42),(6,34),closed=True)
        line('reed',(40,12),(42,6))
        self.relate('connect','reed','body')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
