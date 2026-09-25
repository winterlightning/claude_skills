from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ce1ed58e-e672-4d3c-afbe-79946ffec09f'
SOURCE_PATH = 'pictographic-primitives/holidays/hand_ce1ed58e-e672-4d3c-afbe-79946ffec09f.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'open-palm-hand-ce1ed58e-e672-4d3c-afbe-79946ffec09f'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('hand',)
    def build(self):
        # Lucide hand: upright fingers, staggered true circular caps, rounded palm.
        # SQUARE centerline extrema6,6..42,42. Four fingers use a shared8-unit pitch.
        members=[]
        here=(10,28)
        for i,y in enumerate((14,10,14,18)):
            x=10+i*8
            self.add_line(f"finger-side-{i}",here,(x,y));members.append(f"finger-side-{i}")
            self.add_arc(f"tip-{i}",(x,y),(x+8,y),radius_x=4);members.append(f"tip-{i}")
            here=(x+8,y)
        self.path("palm",here,[(42,29),((42,37),(37,42),(29,42)),(25,42),((19,42),(16,39),(12,34)),(6,26),((6,25),(8,26),(10,28))])
        self.contours[:]=[c for c in self.contours if c.contour_id!="palm"]
        self.add_contour("outline",*members,*[f"palm-{i}" for i in range(6)],closed=True)
        for x,y in ((18,14),(26,14),(34,18)):
            self.add_line(f"crease-{x}",(x,y),(x,26));self.relate("connect",f"crease-{x}","outline")

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
