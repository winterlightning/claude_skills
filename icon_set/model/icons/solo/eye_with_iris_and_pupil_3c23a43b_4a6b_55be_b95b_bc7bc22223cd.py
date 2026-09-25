from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3c23a43b-4a6b-55be-b95b-bc7bc22223cd'
SOURCE_PATH = 'pictographic-primitives/health/specialty eye_3c23a43b-4a6b-55be-b95b-bc7bc22223cd.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'eye-with-iris-and-pupil'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ()
    keywords = ('specialty eye',)

    def build(self):
        # Lucide eye almond flow; restore concentric pupil and iris.
        # HRECT_L (4,8)-(44,40). Circular iris; small pupil reduced to a solid dot.
        self.path("eye",(4,24),[((9,10),(16,8),(24,8)),((32,8),(39,10),(44,24)),((39,38),(32,40),(24,40)),((16,40),(9,38),(4,24))],True)
        self.circle("iris",24,24,8)
        self.add_dot("pupil",(24,24))

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

    icon_id = 'eye-with-iris-and-pupil'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('eye', 'with', 'iris', 'and', 'pupil')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    exception = {'approved_by': 'user', 'svg_sha256': 'b55f2fe5c537acf4a6cd55ff5330f18d6ecdf475ff9a101e472495ef1dc51853', 'reason': 'put exception on fail gate — All existing blocking validation findings for this exact standalone batch drawing, including review warnings.', 'source_svg_sha256': 'b55f2fe5c537acf4a6cd55ff5330f18d6ecdf475ff9a101e472495ef1dc51853'}
