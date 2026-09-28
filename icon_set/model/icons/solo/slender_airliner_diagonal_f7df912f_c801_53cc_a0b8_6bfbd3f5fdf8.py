from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f7df912f-c801-53cc-a0b8-6bfbd3f5fdf8'
SOURCE_PATH = 'pictographic-primitives/travel/crafts model plane_f7df912f-c801-53cc-a0b8-6bfbd3f5fdf8.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'slender-airliner-diagonal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "travel"
    categories = ("travel", "primitives")
    aliases = ()
    keywords = ('crafts model plane',)
    def build(self):
        # Smooth nose, swept main wings, and a unified tail avoid tiny crossed pockets.
        self.path("outline",(40,6),[((41,6),(42,7),(42,8)),((42,13),(37,19),(34,22)),(40,37),(37,42),(27,29),(20,36),(22,42),(17,42),(14,39),(8,42),((6,42),(6,41),(6,39)),(9,35),(6,32),(6,28),(12,30),(19,23),(6,11),(10,8),(26,16),((32,10),(36,6),(40,6))],True)

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

    icon_id = 'slender-airliner-diagonal'
    category = 'travel'
    categories = ('travel', 'primitives')
    aliases = ()
    keywords = ('airplane', 'plane', 'airliner', 'aircraft', 'flight', 'aviation', 'model', 'travel')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    exception = {'approved_by': 'user', 'svg_sha256': '311b29e24b3532befb16355190d27d4282a1cdc7eb37ba2722b8e3b712435a95', 'reason': 'put not pass as eception, im ok with it — All existing blocking validation findings for this exact standalone batch drawing, including review warnings.', 'source_svg_sha256': '311b29e24b3532befb16355190d27d4282a1cdc7eb37ba2722b8e3b712435a95'}
