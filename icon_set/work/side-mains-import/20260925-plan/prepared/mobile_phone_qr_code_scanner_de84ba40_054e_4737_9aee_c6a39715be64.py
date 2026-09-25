from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'de84ba40-054e-4737-9aee-c6a39715be64'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone qr code_de84ba40-054e-4737-9aee-c6a39715be64.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'mobile-phone-qr-code-scanner'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('mobile phone qr code',)

    def build(self):
        # Lucide smartphone shell. Preserve both open QR squares and both Ls.
        self.box("phone",8,4,32,40,4)
        self.add_line("footer",(8,38),(40,38));self.relate("connect","footer","phone")
        self.box("finder-nw",15,12,7,7)
        self.box("finder-se",26,23,7,7)
        self.add_polyline("corner-ne",(29,12),(33,12),(33,16))
        self.add_polyline("corner-sw",(15,26),(15,30),(19,30))

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

    icon_id = 'mobile-phone-qr-code-scanner'
    category = 'objects/device'
    aliases = ('qr phone', 'mobile qr code')
    keywords = ('smartphone', 'qr', 'scan', 'payment')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    exception = {'approved_by': 'user', 'svg_sha256': '85de685b9639cc15d62da61d0f319f87dca780cd1e8a2bd10bbd75659568fcfc', 'reason': 'put exception on fail gate — All existing blocking validation findings for this exact standalone batch drawing, including review warnings.'}
