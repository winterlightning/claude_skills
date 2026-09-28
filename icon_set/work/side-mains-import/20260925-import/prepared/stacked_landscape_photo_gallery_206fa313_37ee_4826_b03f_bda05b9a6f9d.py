from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '206fa313-37ee-4826-b03f-bda05b9a6f9d'
SOURCE_PATH = 'pictographic-primitives/other/double images_206fa313-37ee-4826-b03f-bda05b9a6f9d.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'stacked-landscape-photo-gallery'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('double images',)
    def build(self):
        # Lucide images layering; source has two peaks entirely inside the front photo.
        self.path("rear",(14,33),[(10,33),((7.791,33),(6,31.209),(6,29)),(6,10),((6,7.791),(7.791,6),(10,6)),(29,6),((31.209,6),(33,7.791),(33,10)),(33,14)])
        self.box("front",14,14,28,28,4);self.relate("connect","rear","front")
        self.add_polyline("mountains",(22,34),(27,24),(30,29),(32,27),(34,34),closed=True)

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

    icon_id = 'stacked-landscape-photo-gallery'
    category = 'objects'
    aliases = ()
    keywords = ('stacked', 'landscape', 'photo', 'gallery')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    exception = {'approved_by': 'user', 'svg_sha256': '8cec1fdaf0b98142922cf3203ebb0f012e3730aea19928dd5f37988ab83d89ec', 'reason': 'put not pass as eception, im ok with it — All existing blocking validation findings for this exact standalone batch drawing, including review warnings.', 'source_svg_sha256': '8cec1fdaf0b98142922cf3203ebb0f012e3730aea19928dd5f37988ab83d89ec'}
