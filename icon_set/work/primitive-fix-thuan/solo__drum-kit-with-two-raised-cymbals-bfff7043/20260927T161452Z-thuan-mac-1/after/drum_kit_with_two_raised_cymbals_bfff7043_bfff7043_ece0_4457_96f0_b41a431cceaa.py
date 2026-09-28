'Drum Kit with Two Raised Cymbals.\nSymbol plan: A large round bass drum sits beneath two small tilted drums. Two tall cymbal stands flank the kit, each bending outward to a slanted cymbal and ending in short splayed feet.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Upright toms and single-stroke cymbals reduce the crowded stage silhouette.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'bfff7043-ece0-4457-96f0-b41a431cceaa'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__drum-kit-with-two-raised-cymbals-bfff7043/20260927T161452Z-thuan-mac-1/reference/modern music drums_bfff7043-ece0-4457-96f0-b41a431cceaa.svg'
AUTHOR = "gpt-6"

class BatchIcon(Solo48):
    icon_id = 'drum-kit-with-two-raised-cymbals-bfff7043'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('drums', 'kit', 'cymbals', 'percussion', 'music', 'instrument', 'stands')
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
        # Two full-height stands and a larger bass drum restore the source's
        # kit silhouette; tiny toms become two clear marks at SOLO48.
        circle('bass',24,34,8)
        poly('cymbal-a',(6,6),(12,8),(18,6));line('stem-a',(6,6),(6,42))
        poly('cymbal-b',(30,6),(36,8),(42,6));line('stem-b',(42,6),(42,42))
        line('tom-a',(15,17),(19,17))
        line('tom-b',(29,17),(33,17))
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
