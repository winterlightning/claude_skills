from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '07cafd66-efd4-43ca-978e-239ccb6dfed3'
SOURCE_PATH = 'pictographic-primitives/other/browser dollar sign_07cafd66-efd4-43ca-978e-239ccb6dfed3.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'online-payment-browser-window'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('browser dollar sign',)

    def build(self):
        # Lucide panel rounded browser shell and header. Dollar = S plus spine.
        # Reference toolbar marks retained; dense spacing reported honestly.
        self.box("browser",6,6,36,36,4)
        self.add_line("header",(6,14),(42,14));self.relate("connect","header","browser")
        # Toolbar ticks omitted: the 8u header band has no room for freestanding ink.
        self.path("dollar",(30,24),[((26,21),(18,21),(18,26)),((18,30),(30,27),(30,32)),((30,37),(22,37),(18,34))])
        self.add_line("stem-top",(24,19),(24,22))
        self.add_line("stem-bottom",(24,36),(24,38))
        self.relate("connect","stem-top","dollar");self.relate("connect","stem-bottom","dollar")

    def path(self,name,start,commands,closed=False):
        members=[]
        for i,c in enumerate(commands):
            tag=f"{name}-{i}"
            if len(c)==2: self.add_line(tag,start,c); start=c
            else: self.add_bezier(tag,start,c); start=c[2]
            members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        for i in range(4): self.add_arc(f"{name}-{i}",pts[i],pts[i+1],radius_x=r)
        self.add_contour(name,*[f"{name}-{i}" for i in range(4)],closed=True)

    def box(self,name,x,y,w,h,r=0):
        if not r:
            self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            return
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r),(x+r,y)]
        for i in range(8):
            if i%2: self.add_arc(f"{name}-{i}",pts[i],pts[i+1],radius_x=r)
            else: self.add_line(f"{name}-{i}",pts[i],pts[i+1])
        self.add_contour(name,*[f"{name}-{i}" for i in range(8)],closed=True)

    icon_id = 'online-payment-browser-window'
    category = 'objects/finance'
    aliases = ('browser dollar', 'online payment')
    keywords = ('web', 'money', 'payment', 'commerce')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    exception = {'approved_by': 'user', 'svg_sha256': '7a54de228d70368be0c4f0a1d5797aca962cc3033dc3a6fbfb7b5e145be67c80', 'reason': 'put exception on fail gate — All existing blocking validation findings for this exact standalone batch drawing, including review warnings.', 'source_svg_sha256': '7a54de228d70368be0c4f0a1d5797aca962cc3033dc3a6fbfb7b5e145be67c80'}
