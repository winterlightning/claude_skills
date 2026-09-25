from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9d24ac7b-c494-5a05-b347-45c5044a4d57'
SOURCE_PATH = 'pictographic-primitives/transportation/car_9d24ac7b-c494-5a05-b347-45c5044a4d57.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'atv-side-view'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('car',)
    def build(self):
        # Reviewer: curved vehicle body instead of straight top bar. Source is a low ATV.
        # Preserve dipped saddle, rising front cowling, circular wheels and handlebar.
        self.path("body",(4,22),[(4,12),((4,10),(5,10),(7,10)),(13,10),((16,10),(15,14),(19,14)),(24,14),((27,14),(29,10),(32,10)),(38,10),((42,10),(44,14),(44,20))])
        self.add_line("handlebar",(28,12),(25,8));self.relate("connect","handlebar","body")
        self.path("chassis",(4,22),[((11,22),(17,22),(20,22)),(28,22),((34,19),(38,18),(44,20))]);self.relate("connect","chassis","body")
        for x in (11,37):self.circle(f"wheel-{x}",x,35,5)

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

    icon_id = 'atv-side-view'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('atv', 'quad', 'quad bike', 'off-road', 'vehicle', 'four wheeler', 'offroad', 'side view')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
