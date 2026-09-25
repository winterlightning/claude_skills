from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'de85edfc-1420-4097-b674-118748dbeac1'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone small squares_de85edfc-1420-4097-b674-118748dbeac1.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'smartphone-with-app-icons'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('mobile phone small squares',)
    def build(self):
        # Lucide smartphone shell; restore two app squares down the left side.
        self.box("phone",8,4,32,40,4)
        self.add_line("bezel",(8,38),(40,38));self.relate("connect","bezel","phone")
        for y in (12,24):self.box(f"app-{y}",16,y,6,6,0)

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

    icon_id = 'smartphone-with-app-icons'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('smartphone', 'with', 'app', 'icons')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    exception = {'approved_by': 'user', 'svg_sha256': '16139b3cff35ebf3c2118c2639148fc4f59acd80b6d703626af5efe52cd333d2', 'reason': 'put not pass as eception, im ok with it — All existing blocking validation findings for this exact standalone batch drawing, including review warnings.', 'source_svg_sha256': '16139b3cff35ebf3c2118c2639148fc4f59acd80b6d703626af5efe52cd333d2'}
