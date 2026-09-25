from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '83968c0b-0769-4e90-a1c4-33974d290536'
SOURCE_PATH = 'pictographic-primitives/protection/helmet_83968c0b-0769-4e90-a1c4-33974d290536.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'helmet-83968c0b'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "protection"
    categories = ("protection", "primitives")
    aliases = ()
    keywords = ('helmet',)

    def build(self):
        # Lucide hard-hat: two crown panels, raised central ridge and broad brim.
        # HRECT_L centerline bounds (4,8)-(44,40).
        self.add_polyline("ridge",(20,24),(20,8),(28,8),(28,24))
        self.path("left-shell",(8,32),[(8,26),((8,19),(12,13),(20,12))]);self.relate("connect","left-shell","ridge")
        self.path("right-shell",(28,12),[((36,13),(40,19),(40,26)),(40,32)]);self.relate("connect","right-shell","ridge")
        self.box("brim",4,32,40,8,2)
        self.relate("connect","brim","left-shell");self.relate("connect","brim","right-shell")

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

    icon_id = 'helmet-83968c0b'
    category = 'protection'
    categories = ('protection', 'primitives')
    aliases = ()
    keywords = ('helmet', 'protection')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
